import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Plataforma de Abastecimiento Kikes", page_icon="📦")

# Estilos CSS con colores corporativos verdes
st.markdown("""
    <style>
        .stApp { background-color: #f9fbf9; }
        .header-supply {
            background-color: #008a3e; /* Color verde corporativo */
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            background-color: #008a3e;
            color: white;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover { background-color: #006a2e; }
    </style>
""", unsafe_allow_html=True)

# --- SISTEMA DE INGRESO ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    # Encabezado con logo
    st.markdown("<div class='header-supply'><h1>Logística Kikes</h1><p>Cadena de Abastecimiento</p></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><h3>Acceso al Personal</h3>", unsafe_allow_html=True)
        with st.form("login_form"):
            cedula_input = st.text_input("Número de Cédula del Empleado:")
            submit = st.form_submit_button("Ingresar al Sistema")
            
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
    modulo = st.sidebar.radio("Navegación de Cadena:", [
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
        st.write("Gestionando la disponibilidad de activos en la cadena (GL-P-02).")
        
    elif modulo == "Equipo de Canastas No Aptas":
        st.header("⚠️ Equipo de Canastas No Aptas")
        st.write("Procedimiento de retiro y gestión de activos dañados.")
        
    elif modulo == "Lavado y Desinfección":
        st.header("🧼 Lavado y Desinfección")
        st.write("Estandarización de limpieza GL-P-01 para garantizar la inocuidad.")