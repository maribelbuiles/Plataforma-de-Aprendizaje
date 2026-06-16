import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Plataforma de Capacitación", page_icon="🎓")

# --- SISTEMA DE INGRESO ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    st.title("🎓 Acceso a Capacitación")
    st.write("Por favor, ingrese su número de cédula para continuar.")
    
    with st.form("login_form"):
        cedula_input = st.text_input("Número de cédula:")
        submit = st.form_submit_button("Ingresar")
        
        if submit:
            if cedula_input.strip().isdigit():
                st.session_state['cedula'] = cedula_input.strip()
                st.rerun()
            else:
                st.error("Ingrese solo números.")
else:
    # --- MENÚ DE NAVEGACIÓN ---
    st.sidebar.title(f"Usuario: {st.session_state['cedula']}")
    modulo = st.sidebar.radio("Seleccione el módulo:", [
        "Equipo de Canastas Aptas", 
        "Equipo de Canastas No Aptas", 
        "Lavado y Desinfección"
    ])
    
    if st.sidebar.button("Salir"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- CONTENIDO ---
    if modulo == "Equipo de Canastas Aptas":
        st.header("1. Equipo de Canastas Aptas")
        st.write("Contenido sobre canastas aptas basado en GL-P-02...")
        
    elif modulo == "Equipo de Canastas No Aptas":
        st.header("2. Equipo de Canastas No Aptas")
        st.write("Contenido sobre identificación de daños...")
        
    elif modulo == "Lavado y Desinfección":
        st.header("3. Lavado y Desinfección")
        st.write("Procedimiento de limpieza según GL-P-01...")