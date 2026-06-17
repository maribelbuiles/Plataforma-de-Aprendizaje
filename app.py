import streamlit as st
import os

# Configuración de la interfaz de la página
st.set_page_config(
    page_title="Plataforma de Cadena de Abastecimiento", 
    page_icon="📦", 
    layout="wide"
)

# --- ESTILOS CSS DINÁMICOS Y CREATIVOS (IDENTIDAD KIKES) ---
st.markdown("""
    <style>
        .stApp { background-color: #f7fbf7; }
        .main-banner {
            background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%);
            padding: 35px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .module-title {
            color: #008a3e;
            font-family: 'Arial Black', sans-serif;
            border-bottom: 3px solid #008a3e;
            padding-bottom: 5px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 30px;
            height: 3.2em;
            background-color: #008a3e;
            color: white;
            font-weight: bold;
            font-size: 16px;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-color: #006a2e;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTROL DEL ESTADO DE SESIÓN (INGRESO POR CÉDULA) ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    logo_path = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)
    if logo_path:
        _, col_img2, _ = st.columns([2.5, 1, 2.5])
        with col_img2:
            st.image(logo_path, use_container_width=True)
            
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1></div>", unsafe_allow_html=True)
    
    _, col_form, _ = st.columns([1, 1.8, 1])
    with col_form:
        with st.form("login_form"):
            cedula_input = st.text_input("Número de Cédula del Empleado:")
            if st.form_submit_button("Ingresar al Sistema"):
                if cedula_input.strip().isdigit() and len(cedula_input.strip()) >= 5:
                    st.session_state['cedula'] = cedula_input.strip()
                    st.rerun()
                else:
                    st.error("Por favor, ingrese un número de cédula válido.")
else:
    # --- INTERFAZ INTERNA (MENÚ LATERAL CON EVALUACIONES) ---
    st.sidebar.markdown(f"### 👤 Empleado: `{st.session_state['cedula']}`")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🗺️ Mapa de Ruta Pro")
    
    modulo = st.sidebar.radio(
        "Seleccione el Módulo o Evaluación:",
        [
            "Módulo 1: Equipo de Canastas Aptas", 
            "📝 Evaluación Módulo 1",
            "Módulo 2: Equipo de Canastas No Aptas", 
            "📝 Evaluación Módulo 2",
            "Módulo 3: Lavado y Desinfección de Canastas",
            "📝 Evaluación Módulo 3"
        ]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- DESARROLLO DE CONTENIDO TÉCNICO ---
    
    if "Evaluación" in modulo:
        st.markdown(f"<h2 class='module-title'>{modulo}</h2>", unsafe_allow_html=True)
        st.info("Próximamente disponible: Este espacio estará habilitado para la validación de conocimientos técnicos.")
    
    elif modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 class='module-title'>📦 Módulo 1: Control y Uso de Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        tab1, tab2, tab3 = st.tabs(["📋 Ficha Técnica", "🔄 Apilado y Anidado", "🚛 Armado de Estibas"])
        with tab1:
            st.write("Especificaciones técnicas (Código AFCA022).")
        with tab2:
            st.subheader("Criterios de Posicionamiento")
            st.info("✅ **Arrume de 16 niveles por estiba Ovoid.**")
        with tab3:
            st.write("Procedimiento de armado de estiba sencilla.")

    elif modulo == "Módulo 2: Equipo de Canastas No Aptas":
        st.markdown("<h2 class='module-title'>⚠️ Módulo 2: Identificación de No Aptitud</h2>", unsafe_allow_html=True)
        st.write("Criterios críticos de clasificación y disposición de activos.")

    elif modulo == "Módulo 3: Lavado y Desinfección de Canastas":
        st.markdown("<h2 class='module-title'>🧼 Módulo 3: Procedimiento de Higienización</h2>", unsafe_allow_html=True)
        st.write("Protocolo bajo Resolución 2674 de 2013.")