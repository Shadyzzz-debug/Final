import streamlit as st
import paho.mqtt.client as mqtt
import time
import json
import threading

# --- CONFIGURACIÓN MQTT ---
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
TOPIC_ACCESO = "/vigilia/acceso"
TOPIC_LUZ = "/vigilia/ambiente/luz"
TOPIC_DEFENSA = "/vigilia/defensa"
TOPIC_LOGS = "/vigilia/logs/estado" # Tópico donde el ESP32 publica la temperatura

# --- ESTADO Y MANEJO DE CONEXIÓN ---
client = mqtt.Client()
last_temperature = "Esperando datos..."

def on_connect(client, userdata, flags, rc):
    """Callback que se llama cuando el cliente se conecta al broker."""
    if rc == 0:
        st.toast("✅ Conexión MQTT exitosa a HiveMQ.")
        client.subscribe(TOPIC_LOGS)
    else:
        st.error(f"❌ Fallo en la conexión MQTT. Código de error: {rc}")

def on_message(client, userdata, msg):
    """Callback que se llama cuando se recibe un mensaje suscrito."""
    global last_temperature
    
    if msg.topic == TOPIC_LOGS:
        # El ESP32 publica el estado de la temperatura (ej: "T=25.50C")
        try:
            payload_str = msg.payload.decode('utf-8')
            if payload_str.startswith("T="):
                last_temperature = payload_str.split('=')[1]
            else:
                last_temperature = payload_str # Para mensajes de estado (Online, etc.)
        except Exception:
            last_temperature = "Error de decodificación"

def mqtt_loop_start():
    """Inicia el hilo de MQTT para mantener la conexión activa."""
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        # Inicia el hilo en segundo plano que maneja la red, reconexión y callbacks.
        client.loop_start() 
    except Exception as e:
        st.error(f"Fallo al intentar conectar MQTT: {e}")

# Asegurar que el cliente MQTT se inicialice y conecte solo una vez
if 'mqtt_client_started' not in st.session_state:
    st.session_state.mqtt_client_started = True
    mqtt_loop_start()

# --- FUNCIONES DE PUBLICACIÓN ---
def publish_command(topic, payload):
    """Función auxiliar para publicar comandos."""
    client.publish(topic, payload, qos=0)
    st.toast(f"Comando publicado en {topic}: {payload}")

# --- INTERFAZ STREAMLIT ---

st.set_page_config(page_title="Vigilancia Arcana | Control", layout="wide")

st.title("🛡️ Centro de Control de Vigilancia Arcana (MQTT)")
st.caption(f"Broker: `{MQTT_BROKER}` | Tópico de Logs: `{TOPIC_LOGS}`")

# Placeholder para la visualización de la temperatura en tiempo real
temp_placeholder = st.empty()


# --- Columna 1: ACCESO Y DEFENSA ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🔑 Control de Acceso (Servo)")
    st.subheader(f"Tópico: `{TOPIC_ACCESO}`")
    
    acceso_status = st.toggle("Bloqueo de Puerta", value=False, help="Controla el Servo Motor (Cerradura). OFF=Cerrado (0°), ON=Abierto (180°).")

    if acceso_status:
        st.success("✅ PUERTA ABIERTA (Comando: 1)")
        publish_command(TOPIC_ACCESO, "1")
    else:
        st.warning("🔒 PUERTA CERRADA (Comando: 0)")
        publish_command(TOPIC_ACCESO, "0")

    st.markdown("---")
    
    st.header("🚨 Sistema de Defensa (Buzzer)")
    st.subheader(f"Tópico: `{TOPIC_DEFENSA}`")

    defensa_status = st.button("🔴 Activar Alarma Sonora", type="primary", use_container_width=True)
    desactivar_defensa = st.button("🟢 Desactivar Alarma", use_container_width=True)

    if defensa_status:
        publish_command(TOPIC_DEFENSA, "HIGH")
    
    if desactivar_defensa:
        publish_command(TOPIC_DEFENSA, "LOW")
        
    st.info("La alarma se activará por 5 segundos con el comando 'HIGH'.")


# --- Columna 2: AMBIENTE (Luz RGB) y LOGS ---
with col2:
    st.header("💡 Control de Ambiente (RGB)")
    st.subheader(f"Tópico: `{TOPIC_LUZ}`")
    
    luz_comando = st.selectbox(
        "Selecciona el Modo de Iluminación",
        options=["Por Defecto", "CALIDEZ", "REPOSO"],
        index=0,
        help="Envía comandos de texto para cambiar el color del LED RGB."
    )

    if luz_comando == "CALIDEZ":
        st.markdown("Color: Naranja Cálido.")
    elif luz_comando == "REPOSO":
        st.markdown("Color: Azul Oscuro.")
    else:
        st.markdown("Color: Blanco Suave.")
        
    publish_command(TOPIC_LUZ, luz_comando)
    
    st.markdown("---")
    
    st.header("🌡️ Monitoreo (Temperatura)")
    
    # Mostrar la última temperatura recibida
    temp_placeholder.metric(
        label="Temperatura del Santuario", 
        value=last_temperature
    )

    st.markdown("---")
    
    # Un pequeño truco para forzar la actualización de la interfaz y el placeholder de temperatura
    st.button("Actualizar Logs/Temperatura (Manual)", help="Fuerza la re-ejecución del script para mostrar el último dato de MQTT.", use_container_width=True)

