import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Plataforma de Capacitación", page_icon="🎓")

# Estilos CSS para mejorar la creatividad visual
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f7f6;
        }
        .main-header {
            color: #004a99;
            text-align: center;
            font-family: sans-serif;
            margin-bottom: 20px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            height: 3em;
            background-color: #004a99;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- SISTEMA DE INGRESO ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    st.markdown("<h1 class='main-header'>🎓 Plataforma de Capacitación Logística</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Identifícate para acceder a los procedimientos oficiales.</p>", unsafe_allow_html=True)
    
    # Contenedor centrado para el formulario
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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
    st.sidebar.title(f"Empleado: {st.session_state['cedula']}")
    modulo = st.sidebar.radio("Seleccione el módulo:", [
        "Equipo de Canastas Aptas", 
        "Equipo de Canastas No Aptas", 
        "Lavado y Desinfección"
    ])
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- CONTENIDO ---
    if modulo == "Equipo de Canastas Aptas":
        st.header("Equipo de Canastas Aptas")
        st.write("Contenido sobre canastas aptas basado en el procedimiento GL-P-02.")
        
    elif modulo == "Equipo de Canastas No Aptas":
        st.header("Equipo de Canastas No Aptas")
        st.write("Criterios de retiro y manejo de canastas dañadas (GL-P-02).")
        
    elif modulo == "Lavado y Desinfección":
        st.header("Lavado y Desinfección")
        st.write("Procedimiento de limpieza según norma GL-P-01 (Uso de Biodex y Biosanit).")