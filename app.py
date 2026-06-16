import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gestión Logística - Kikes", page_icon="📦")

# Estilos CSS con tonos verdes corporativos y diseño moderno
st.markdown("""
    <style>
        .stApp {
            background-color: #f9fbf9;
        }
        .title-box {
            background-color: #2e7d32; 
            padding: 20px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 30px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 20px;
            height: 3em;
            background-color: #388e3c;
            color: white;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #2e7d32;
        }
    </style>
""", unsafe_allow_html=True)

# --- SISTEMA DE INGRESO ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    st.markdown("<div class='title-box'><h1>📦 Logística de Canastas</h1><p>Sistema de Capacitación y Abastecimiento</p></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("Acceso al Personal")
        with st.form("login_form"):
            cedula_input = st.text_input("Número de Cédula del Empleado:")
            submit = st.form_submit_button("Ingresar al Flujo Logístico")
            
            if submit:
                if cedula_input.strip().isdigit():
                    st.session_state['cedula'] = cedula_input.strip()
                    st.rerun()
                else:
                    st.error("Por favor, ingrese un número de cédula válido.")
else:
    # --- MENÚ DE NAVEGACIÓN ---
    st.sidebar.markdown(f"### 👤 Empleado: {st.session_state['cedula']}")
    st.sidebar.markdown("---")
    modulo = st.sidebar.radio("Navegación de Módulos:", [
        "Equipo de Canastas Aptas", 
        "Equipo de Canastas No Aptas", 
        "Lavado y Desinfección"
    ])
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- CONTENIDO ---
    if modulo == "Equipo de Canastas Aptas":
        st.header("✅ Equipo de Canastas Aptas")
        st.write("Optimización y flujo correcto del equipo de canastas según norma **GL-P-02**.")
        
    elif modulo == "Equipo de Canastas No Aptas":
        st.header("⚠️ Equipo de Canastas No Aptas")
        st.write("Protocolos de retiro y gestión de activos dañados para mantener la calidad.")
        
    elif modulo == "Lavado y Desinfección":
        st.header("🧼 Lavado y Desinfección")
        st.write("Estándares de limpieza **GL-P-01**: Asegurando la inocuidad en toda la cadena de abastecimiento.")