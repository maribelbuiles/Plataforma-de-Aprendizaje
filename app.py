import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Plataforma de Capacitación", page_icon="🎓")

# --- SISTEMA DE INGRESO ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    st.title("🎓 Acceso a la Plataforma")
    st.write("Bienvenido. Por favor, identifíquese para iniciar.")
    
    with st.form("login_form"):
        # Campo actualizado según tu solicitud
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