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
    
# --- PÁGINA 1: EL SANTUARIO INTERIOR (Acceso y Ambiente) ---
def santuario_interior():
    st.title("🚪 EL SANTUARIO INTERIOR: Cierre y Ambiente")
    st.markdown(
        """
        <p>Esta cámara opera como el punto de acceso seguro y el núcleo de control ambiental. La interacción 
        se canaliza a través de métodos de **Acceso Visual** y **Comando Arcano (Voz/Texto)**, garantizando que 
        solo los cazadores iniciados puedan manipular el velo de la realidad.</p>
        """, unsafe_allow_html=True
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="interface-card">', unsafe_allow_html=True)
        st.subheader("1. La Runa de Identidad (Acceso Visual)")
        st.write("Modalidad: **Imagen/Visual**")
        st.write("Simulación de un portal de reconocimiento de cazadores. Utiliza la 'Vision App' para validar el glifo o rostro del solicitante y permitir el acceso.")
        
        if st.button("ACCEDER VÍA GLIFO VISUAL", key="access_vision"):
            st.markdown(f"**Activando Artefacto:** [Vision: Revelación]({URL_MAP['vision app']})")
            st.markdown('<p style="color: #FF6666;">*(Se abre el Artefacto en una nueva pestaña para el reconocimiento del glifo de acceso)*</p>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


    with col2:
        st.markdown('<div class="interface-card">', unsafe_allow_html=True)
        st.subheader("2. Comandos Arcanos (Control Ambiental)")
        st.write("Modalidad: **Voz/Texto**")
        st.write("Permite ajustar los 'Fluid Lamps' (simulación de luces) y la 'Heater Coil' (temperatura) mediante comandos escritos o de voz decodificados.")
        
        comando = st.text_input("Ingresar Comando (Ej: 'Activar las Runas de Calidez')", key="voice_command")
        
        if st.button("EJECUTAR COMANDO DE AMBIENTE", key="execute_voice"):
            if comando:
                st.info(f"Comando '{comando}' enviado al núcleo de ambiente. (Simulación: Esto usaría el **Ctrl Voice** para parsear el intent y enviarlo al dispositivo físico).")
            else:
                st.warning("Ingrese un comando arcano válido.")

        st.markdown(f"**Artefacto de Decodificación:** [Control Voz]({URL_MAP['crtl voice']})")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("## Interacción con el Mundo Físico")
    st.markdown(
        """
        El 'Santuario Interior' interactúa con la simulación física (WOKWI) para el control de:
        - **Acceso:** Si la identidad visual es correcta, se activa un 'Servo Lock' (simulado) en WOKWI para abrir la puerta.
        - **Ambiente:** Los comandos de voz/texto controlan un 'LED Array' (luces) y un 'Termistor' (temperatura) en el entorno físico.
        """
    )


# --- PÁGINA 2: EL ALTAR DE LA INFERENCIA (Monitoreo y Acción) ---
def altar_inferencia():
    st.title("👁️ EL ALTAR DE LA INFERENCIA: Monitoreo y Defensa")
    st.markdown(
        """
        <p>El Altar es el centro de monitoreo remoto y el punto de partida para acciones de defensa externas. 
        Permite la revisión de las huellas dejadas por las bestias y la activación de contramedidas.</p>
        """, unsafe_allow_html=True
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="interface-card">', unsafe_allow_html=True)
        st.subheader("3. Registro de la Locura (Historial de Eventos)")
        st.write("Modalidad: **Data/Historial de Logs**")
        st.write("Monitorea los registros de accesos fallidos y detecciones de anomalías. Es vital para rastrear la actividad de entidades desconocidas.")
        
        if st.button("CONSULTAR REGISTRO CRÍTICO", key="view_hist"):
            st.markdown(f"**Activando Artefacto:** [Hist. Inferencia]({URL_MAP['hist inf']})")
            st.markdown('<p style="color: #FF6666;">*(Se abre el Artefacto en una nueva pestaña para el análisis de logs y anomalías)*</p>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="interface-card">', unsafe_allow_html=True)
        st.subheader("4. El Lamento del Vacío (Acción Remota)")
        st.write("Modalidad: **Controles/MQTT**")
        st.write("Simulación de envío de una 'Runa de Alarma' o 'Bloqueo Exterior' a través de MQTT al punto de entrada más vulnerable.")
        
        accion = st.selectbox("Seleccionar Runa de Acción Remota", ["Activar Escudo de Niebla (LOW)", "Sellar Portal Temporal (HIGH)"], key="mqtt_action")
        
        if st.button("ENVIAR COMANDO REMOTO (MQTT)", key="send_mqtt"):
            if accion == "Activar Escudo de Niebla (LOW)":
                st.success("Comando MQTT 'Activar Niebla' enviado al entorno físico (Tópico: /vigilia/defensa).")
            else:
                st.error("Comando MQTT 'Sello Portal' enviado al entorno físico (Tópico: /vigilia/defensa).")

        st.markdown(f"**Artefacto de Envío:** [Control MQTT]({URL_MAP['send cmqtt']})")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("## Interacción con el Mundo Físico")
    st.markdown(
        """
        El 'Altar de la Inferencia' utiliza el protocolo **MQTT** para controlar dispositivos externos simulados en WOKWI:
        - **Acción Remota:** Los comandos MQTT definidos aquí son recibidos por el microcontrolador en WOKWI, que activa una 'Sirena de Alarma' o un 'Bloqueo Lógico' (simulado con un LED o display).
        """
    )

# --- EJECUCIÓN DEL CONTROLADOR DE PÁGINAS ---
if st.session_state.page == "santuario":
    santuario_interior()
elif st.session_state.page == "altar":
    altar_inferencia()

