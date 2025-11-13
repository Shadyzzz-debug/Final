import streamlit as st

# --- URLs DE ARTEFACTOS (VERIFICADAS POR EL USUARIO) ---
# Estas URLs se utilizan como enlaces para simular la funcionalidad de los artefactos integrados.
URL_MAP = {
    "vision app": "https://visionapp-gw3qmdnaf3nhnqtvpagdjp.streamlit.app/",
    "crtl voice": "https://ctrlvoice-lgppyaas3uqbshewc8ienf.streamlit.app/",
    "hist inf": "https://histinf-2hkp6kecngkr3a7mpmjwjx.streamlit.app/",
    "send cmqtt": "https://sendcmqtt-kdphuxjy7rjprdxquajky9.streamlit.app/",
    "url_ia": "https://sites.google.com/view/aplicacionesdeia/inicio"
}

# --- CONFIGURACIÓN MQTT PARA WOKWI ---
TOPIC_ACCESO = "/vigilia/acceso"
TOPIC_LUZ = "/vigilia/ambiente/luz"
TOPIC_DEFENSA = "/vigilia/defensa"
TOPIC_LOGS = "/vigilia/logs/estado" # Tópico de lectura de temperatura

# --- ESTÉTICA GÓTICA (CSS UNIFICADO) ---
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
h2, h3 {
    color: #D3D3D3; /* Plata mate */
    margin-top: 30px;
    border-left: 6px solid #4F4A5E; /* Acento de piedra oscura */
    padding-left: 15px;
    font-size: 1.8em;
}

/* Contenedores de Interfaz (Tarjetas de Obsidiana) */
.interface-card {
    background-color: #1A1A2A;  
    border: 2px solid #383850;
    border-radius: 12px;  
    padding: 20px;
    margin-bottom: 25px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.7);  
    transition: box-shadow 0.3s;
    /* Responsive adjustment for columns */
    min-height: 250px; 
}

.interface-card:hover {
    box-shadow: 0 10px 20px rgba(156, 126, 79, 0.4); /* Brillo Arcano */
}

/* Botones de Comando */
.stButton>button {
    background-color: #B22222; /* Rojo Sangre */
    color: #E0E0E0;
    font-weight: bold;
    border: 2px solid #FF6666;
    border-radius: 8px;
    padding: 10px 20px;
    transition: background-color 0.3s, transform 0.2s;
    width: 100%; /* Full width for better mobile interaction */
    margin-top: 10px;
}

.stButton>button:hover {
    background-color: #9C7E4F; /* Bronce sobre Sangre */
    color: #0F0F1A;
    transform: translateY(-2px);
}

/* Enlaces (Runas de Conexión) */
a {
    color: #FF6666 !important;  
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s;
}

a:hover {
    color: #FFAAAA !important;
    text-shadow: 0 0 5px #FF6666;
    text-decoration: underline;
}

/* Sidebar */
.sidebar-title {
    color: #B22222 !important;  
    text-shadow: 1px 1px 5px #000000;
    font-size: 1.8em !important;
}

/* Inputs de Texto/Voz */
.stTextInput>div>div>input, .stTextArea>div>div>textarea {
    background-color: #2A2A3A;
    color: #E0E0E0;
    border: 1px solid #4F4A5E;
    border-radius: 6px;
}
</style>
"""
st.markdown(BASE_CSS, unsafe_allow_html=True)

# --- NAVEGACIÓN ---
def set_page(page_name):
    st.session_state.page = page_name

if 'page' not in st.session_state:
    st.session_state.page = "santuario"

# --- SIDEBAR DE NAVEGACIÓN ---
with st.sidebar:
    st.markdown('<h3 class="sidebar-title">📜 NEXO DE LA VIGILIA</h3>', unsafe_allow_html=True)
    st.write(
        "El Origen de la Vigilia, donde se administran los portales multimodales hacia el mundo físico."
    )
    st.markdown("---")
    
    # Botones de navegación
    if st.button("🚪 Santuario Interior (Acceso y Ambiente)"):
        set_page("santuario")
    
    if st.button("👁️ Altar de la Inferencia (Monitoreo y Acción)"):
        set_page("altar")

    st.markdown("---")
    # Enlace a la página principal de Artefactos (el índice anterior)
    st.write(f"Conexión a los pergaminos ancestrales: [Runa de Enlace]({URL_MAP['url_ia']})")
    
# --- FUNCIÓN DE PUBLICACIÓN SIMULADA ---
def show_mqtt_payload(topic, payload, action_name):
    st.markdown(f"""
        <div style="background-color: #383850; padding: 10px; border-radius: 6px; margin-top: 15px; border: 1px solid #9C7E4F;">
            <p style="font-weight: bold; color: #D3D3D3;">{action_name}: Comando MQTT Publicado (Simulado)</p>
            <p style="margin: 0;">Tópico: <code style="color: #FF6666;">{topic}</code></p>
            <p style="margin: 0;">Payload: <code style="color: #9C7E4F;">{payload}</code></p>
        </div>
        """, unsafe_allow_html=True)
    st.warning("Debe usar un cliente externo (como el Artefacto 'Control MQTT') para enviar este comando al broker.")

# --- PÁGINA 1: EL SANTUARIO INTERIOR (Acceso y Ambiente) ---
def santuario_interior():
    st.title("🚪 EL SANTUARIO INTERIOR: Cierre y Ambiente")
    
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="interface-card">', unsafe_allow_html=True)
        st.subheader("1. La Runa de Identidad (Acceso Visual)")
        st.write("Modalidad: **Imagen/Visual**")
        st.write("Simulación de un portal de reconocimiento de cazadores. La validación visual abriría la cerradura (`/vigilia/acceso`).")
        
        # Botones para simular el resultado de la validación visual
        st.markdown("---")
        st.markdown("**Control Manual del Acceso (Servo Lock)**")
        
        if st.button("ABRIR CERRADURA (Payload: 1)", key="open_lock"):
            show_mqtt_payload(TOPIC_ACCESO, "1", "ACCESO CONCEDIDO (Abrir Servo)")

        if st.button("CERRAR CERRADURA (Payload: 0)", key="close_lock"):
            show_mqtt_payload(TOPIC_ACCESO, "0", "ACCESO REVOCADO (Cerrar Servo)")

        st.markdown(f"**Artefacto de Decodificación Visual:** [Vision: Revelación]({URL_MAP['vision app']})")
        st.markdown('</div>', unsafe_allow_html=True)


    with col2:
        st.markdown('<div class="interface-card">', unsafe_allow_html=True)
        st.subheader("2. Comandos Arcanos (Control Ambiental)")
        st.write("Modalidad: **Control de Ambiente (LED RGB)**")
        st.write("Ajusta las 'Fluid Lamps' mediante comandos directos, enviando el Payload al tópico `/vigilia/ambiente/luz`.")
        
        st.markdown("---")
        st.markdown("**Configuración del Modo de Iluminación**")
        
        st.write("Seleccione el ambiente para el Santuario:")
        
        if st.button("MODO CALIDEZ (Payload: CALIDEZ)", key="mode_calidez"):
            show_mqtt_payload(TOPIC_LUZ, "CALIDEZ", "ILUMINACIÓN: MODO CALIDEZ (Naranja)")

        if st.button("MODO REPOSO (Payload: REPOSO)", key="mode_reposo"):
            show_mqtt_payload(TOPIC_LUZ, "REPOSO", "ILUMINACIÓN: MODO REPOSO (Azul Oscuro)")
            
        if st.button("MODO POR DEFECTO (Payload: Por Defecto)", key="mode_default"):
            show_mqtt_payload(TOPIC_LUZ, "Por Defecto", "ILUMINACIÓN: MODO POR DEFECTO (Blanco)")
            
        st.markdown(f"**Artefacto de Decodificación de Voz/Texto:** [Control Voz]({URL_MAP['crtl voice']})")
        st.markdown('</div>', unsafe_allow_html=True)


# --- PÁGINA 2: EL ALTAR DE LA INFERENCIA (Monitoreo y Acción) ---
def altar_inferencia():
    st.title("👁️ EL ALTAR DE LA INFERENCIA: Monitoreo y Defensa")
    
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="interface-card">', unsafe_allow_html=True)
        st.subheader("3. El Historial de Logs (Temperatura)")
        st.write("Modalidad: **Data/Historial de Logs**")
        st.write(f"Monitorea el registro crítico de eventos y la temperatura del entorno físico, recibida en el tópico: <code style='color: #9C7E4F;'>{TOPIC_LOGS}</code>.")
        st.write("El WOKWI publica datos de temperatura cada 10 segundos. Este panel **requeriría** un suscriptor MQTT continuo para mostrar los datos en tiempo real.")
        
        if st.button("CONSULTAR REGISTRO CRÍTICO", key="view_hist"):
            st.markdown(f"**Activando Artefacto:** [Hist. Inferencia]({URL_MAP['hist inf']})")
            st.markdown('<p style="color: #FF6666;">*(Se abre el Artefacto en una nueva pestaña para el análisis de logs)*</p>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="interface-card">', unsafe_allow_html=True)
        st.subheader("4. El Lamento del Vacío (Alarma/Defensa)")
        st.write("Modalidad: **Controles/Alarma (Buzzer)**")
        st.write("Activa la 'Sirena de Alarma' (Buzzer) del ESP32 enviando comandos de defensa al tópico `/vigilia/defensa`.")
        
        st.markdown("---")
        st.markdown("**Control Manual de la Alarma**")
        
        if st.button("ACTIVAR LAMENTO (Payload: HIGH)", key="activate_alarm"):
            show_mqtt_payload(TOPIC_DEFENSA, "HIGH", "DEFENSA: ALARMA ACTIVADA (HIGH)")
            
        if st.button("SILENCIAR LAMENTO (Payload: LOW)", key="deactivate_alarm"):
            show_mqtt_payload(TOPIC_DEFENSA, "LOW", "DEFENSA: ALARMA DESACTIVADA (LOW)")

        st.markdown(f"**Artefacto de Envío de Comandos:** [Control MQTT]({URL_MAP['send cmqtt']})")
        st.markdown('</div>', unsafe_allow_html=True)
        
# --- EJECUCIÓN DEL CONTROLADOR DE PÁGINAS ---
if st.session_state.page == "santuario":
    santuario_interior()
elif st.session_state.page == "altar":
    altar_inferencia()
