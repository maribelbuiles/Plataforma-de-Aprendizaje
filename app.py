import streamlit as st

# Configuración de página
st.set_page_config(page_title="Cadena de Abastecimiento Kikes", page_icon="📦")

# --- ESTILOS CSS CREATIVOS Y CORPORATIVOS ---
st.markdown("""
    <style>
        /* Fondo suave */
        .stApp { background-color: #f4fcf4; }
        
        /* Encabezado dinámico */
        .header-box {
            background: linear-gradient(135deg, #008a3e 0%, #006a2e 100%);
            padding: 30px;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 25px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }
        
        /* Botones estilo Kikes */
        .stButton>button {
            width: 100%;
            border-radius: 50px;
            background-color: #008a3e;
            color: white;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover { background-color: #005a26; transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# --- LÓGICA DE INGRESO ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    # Mostrar Logo
    try:
        col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
        with col_img2:
            st.image("logo.png", use_container_width=True)
    except:
        st.warning("Asegúrate de que el logo se llame 'logo.png'")

    st.markdown("<div class='header-box'><h1>Plataforma de Cadena de Abastecimiento</h1></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            st.subheader("Acceso al Personal")
            cedula_input = st.text_input("Número de Cédula del Empleado:")
            submit = st.form_submit_button("Ingresar al Flujo Logístico")
            
            if submit:
                if cedula_input.strip().isdigit():
                    st.session_state['cedula'] = cedula_input.strip()
                    st.rerun()
                else:
                    st.error("Por favor, ingrese un número de cédula válido.")
else:
    # --- MENÚ NAVEGACIÓN ---
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

    # --- CONTENIDO DE MÓDULOS ---
    if modulo == "Equipo de Canastas Aptas":
        st.header("✅ Equipo de Canastas Aptas")
        st.write("Gestionando la disponibilidad de activos en la cadena (GL-P-02).")
        
    elif modulo == "Equipo de Canastas No Aptas":
        st.header("⚠️ Equipo de Canastas No Aptas")
        st.write("Procedimiento de retiro y gestión de activos dañados.")
        
    elif modulo == "Lavado y Desinfección":
        st.header("🧼 Lavado y Desinfección")
        st.write("Estandarización de limpieza GL-P-01 para garantizar la inocuidad.")