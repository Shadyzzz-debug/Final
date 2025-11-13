import streamlit as st

# --- CONFIGURACIÓN MQTT (Coherente con Wokwi) ---
# Tópicos utilizados por el ESP32 en Wokwi
TOPIC_ACCESO = "/vigilia/acceso"
TOPIC_LUZ = "/vigilia/ambiente/luz"
TOPIC_DEFENSA = "/vigilia/defensa"
TOPIC_LOGS = "/vigilia/logs/estado" # Tópico de lectura de temperatura (Publicación del ESP32)

# --- ESTÉTICA GÓTICA UNIFICADA ---
BASE_CSS = """
<style>
/* ---------------------------------------------------- */
/* AMBIENTE DE PESADILLA (Bloodborne Theme) */
/* ---------------------------------------------------- */
.stApp {
    background-color: #0F0F1A;  
    color: #E0E0E0;  
    font-family: 'Times New Roman', serif;  
}

/* Título Principal */
h1 {
    color: #9C7E4F; /* Bronce envejecido */
    text-align: center;
    border-bottom: 5px double #B22222; /* Línea de doble filo */
    padding-bottom: 15px;
    margin-bottom: 50px;
    font-size: 3em;
    letter-spacing: 4px;
    font-weight: 700;
    text-shadow: 0 0 10px rgba(178, 34, 34, 0.5);
}

/* Subtítulos de Secciones */
h3 {
    color: #D3D3D3; /* Plata mate */
    margin-top: 20px;
    border-left: 6px solid #4F4A5E; /* Acento de piedra oscura */
    padding-left: 15px;
    font-size: 1.5em;
    min-height: 40px; 
}

/* Contenedores de Interfaz (Tarjetas de Obsidiana) */
.interface-card {
    background-color: #1A1A2A;  
    border: 2px solid #383850;
    border-radius: 12px;  
    padding: 20px;
    margin-bottom: 25px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.7);  
    min-height: 350px; 
}

/* Botones de Comando */
.stButton>button {
    background-color: #B22222; /* Rojo Sangre */
    color: #E0E0E0;
    font-weight: bold;
    border: 2px solid #FF6666;
    border-radius: 8px;
    padding: 10px 15px;
    transition: background-color 0.3s, transform 0.2s;
    width: 100%;
    margin-top: 10px;
}

.stButton>button:hover {
    background-color: #9C7E4F; /* Bronce sobre Sangre */
    color: #0F0F1A;
    transform: translateY(-2px);
}

/* Panel de Comandos MQTT */
.mqtt-log {
    background-color: #383850; 
    padding: 12px; 
    border-radius: 8px; 
    margin-top: 20px; 
    border: 2px solid #9C7E4F;
}
.mqtt-log p {
    margin: 4px 0;
}
.mqtt-log code {
    color: #FF6666; 
    font-weight: bold;
    background-color: #2A2A3A;
    padding: 2px 5px;
    border-radius: 3px;
}
</style>
"""
st.markdown(BASE_CSS, unsafe_allow_html=True)

# --- ESTRUCTURA DE COMANDO Y RESPUESTA ---

# Se usa st.session_state para almacenar la última acción y mostrarla en un panel unificado.
if 'last_command' not in st.session_state:
    st.session_state.last_command = {
        "topic": "N/A", 
        "payload": "N/A", 
        "action": "Esperando Primer Comando"
    }

def update_mqtt_command(topic, payload, action):
    """Actualiza el estado para reflejar el comando MQTT que debe ser enviado."""
    st.session_state.last_command = {
        "topic": topic, 
        "payload": payload, 
        "action": action
    }

# --- DISEÑO UNIFICADO DE PÁGINA ---

st.title("🛡️ NEXO DE LA VIGILIA: Estación de Mando Unificada")

st.markdown("""
El ESP32, guardián del Santuario, opera bajo estos comandos. 
Esta interfaz genera el Tópico y el Payload exacto. Debe utilizar un cliente MQTT externo 
(como el Artefacto **send cmqtt** o cualquier otro cliente MQTT) con el broker `broker.hivemq.com` 
para enviar el comando que aparece en el **Panel de Acción Arcano**.
""")
st.markdown("---")


# ------------------------------------------------
# C1: ACCESO (Servo) | C2: ILUMINACIÓN (LED RGB)
# C3: REGISTRO (Logs) | C4: DEFENSA (Buzzer)
# ------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

# --- COLUMNA 1: ACCESO (Servo Motor) ---
with col1:
    st.markdown('<div class="interface-card">', unsafe_allow_html=True)
    st.markdown("<h3>1. Runa de Identidad (Acceso)</h3>", unsafe_allow_html=True)
    st.write("Controla la cerradura electromecánica (`PIN_SERVO: 18`) enviando `1` (abrir) o `0` (cerrar).")
    st.markdown("---")
    
    if st.button("ABRIR CERRADURA (180°)", key="open_lock"):
        update_mqtt_command(TOPIC_ACCESO, "1", "ACCESO CONCEDIDO (Abrir Servo)")

    if st.button("CERRAR CERRADURA (0°)", key="close_lock"):
        update_mqtt_command(TOPIC_ACCESO, "0", "ACCESO REVOCADO (Cerrar Servo)")
    
    st.markdown('</div>', unsafe_allow_html=True)


# --- COLUMNA 2: ILUMINACIÓN (LED RGB) ---
with col2:
    st.markdown('<div class="interface-card">', unsafe_allow_html=True)
    st.markdown("<h3>2. Comandos Arcanos (Luz)</h3>", unsafe_allow_html=True)
    st.write("Ajusta las lámparas de ambiente (`Pines 21, 22, 23`).")
    st.markdown("---")
    
    if st.button("MODO CALIDEZ (Naranja)", key="mode_calidez"):
        update_mqtt_command(TOPIC_LUZ, "CALIDEZ", "ILUMINACIÓN: MODO CALIDEZ")

    if st.button("MODO REPOSO (Azul Oscuro)", key="mode_reposo"):
        update_mqtt_command(TOPIC_LUZ, "REPOSO", "ILUMINACIÓN: MODO REPOSO")
        
    if st.button("MODO POR DEFECTO (Blanco)", key="mode_default"):
        update_mqtt_command(TOPIC_LUZ, "Por Defecto", "ILUMINACIÓN: MODO POR DEFECTO")
        
    st.markdown('</div>', unsafe_allow_html=True)


# --- COLUMNA 3: REGISTRO (Temperatura/Logs) ---
with col3:
    st.markdown('<div class="interface-card">', unsafe_allow_html=True)
    st.markdown("<h3>3. Altar de la Inferencia (Logs)</h3>", unsafe_allow_html=True)
    st.write("El ESP32 publica la temperatura (`PIN_TEMP: 36`) cada 10 segundos en este tópico de monitoreo.")
    st.markdown("---")
    st.markdown(f"""
        <p style='color: #D3D3D3; font-weight: bold;'>
            Tópico de Monitoreo:
        </p>
        <div style='background-color: #2A2A3A; padding: 10px; border-radius: 6px; border: 1px solid #4F4A5E;'>
            <code style='color: #9C7E4F; font-size: 0.9em;'>{TOPIC_LOGS}</code>
        </div>
        """, unsafe_allow_html=True)
    st.info("Para ver la temperatura (`T=XX.XXC`) en tiempo real, **suscríbase** al tópico anterior utilizando un cliente MQTT externo.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- COLUMNA 4: DEFENSA (Buzzer) ---
with col4:
    st.markdown('<div class="interface-card">', unsafe_allow_html=True)
    st.markdown("<h3>4. El Lamento del Vacío (Alarma)</h3>", unsafe_allow_html=True)
    st.write("Activa la sirena de defensa (`PIN_BUZZER: 19`) enviando `HIGH` o `LOW`.")
    st.markdown("---")
    
    if st.button("ACTIVAR LAMENTO (Alarma)", key="activate_alarm"):
        update_mqtt_command(TOPIC_DEFENSA, "HIGH", "DEFENSA: ALARMA ACTIVADA")
        
    if st.button("SILENCIAR LAMENTO (Desactivar)", key="deactivate_alarm"):
        update_mqtt_command(TOPIC_DEFENSA, "LOW", "DEFENSA: ALARMA DESACTIVADA")
        
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- PANEL DE ACCIÓN ARCANA (Panel de Logs/Comandos Unificado) ---
st.markdown('<h2 style="color: #FF6666; text-align: center; border-bottom: none;">PANEL DE ACCIÓN ARCANA (Comando a Publicar)</h2>', unsafe_allow_html=True)

current_command = st.session_state.last_command

st.markdown(f"""
<div class="mqtt-log">
    <p style="font-weight: bold; color: #E0E0E0;">Última Acción Seleccionada: <span style="color: #9C7E4F;">{current_command['action']}</span></p>
    <p>Tópico de Publicación: <code>{current_command['topic']}</code></p>
    <p>Payload a Enviar: <code>{current_command['payload']}</code></p>
</div>
""", unsafe_allow_html=True)

st.warning("⚠️ **INSTRUCCIÓN VITAL:** Copie el Tópico y el Payload y péguelos en su cliente MQTT externo para que el ESP32 en Wokwi ejecute la acción. El broker es **broker.hivemq.com** (Puerto 1883).")
