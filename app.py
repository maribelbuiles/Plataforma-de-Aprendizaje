import streamlit as st
import os

# Configuración de la interfaz
st.set_page_config(page_title="Plataforma de Cadena de Abastecimiento", page_icon="📦", layout="wide")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
        .stApp { background-color: #f7fbf7; }
        .main-banner { background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%); padding: 35px; border-radius: 15px; color: white; text-align: center; margin-bottom: 25px; }
        .module-title { color: #008a3e; font-family: 'Arial Black', sans-serif; border-bottom: 3px solid #008a3e; padding-bottom: 5px; }
        .stButton>button { width: 100%; border-radius: 30px; height: 3.2em; background-color: #008a3e; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

if 'cedula' not in st.session_state: st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    logo_path = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)
    if logo_path:
        _, col_img2, _ = st.columns([2.5, 1, 2.5])
        with col_img2: st.image(logo_path, use_container_width=True)
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
    st.sidebar.markdown(f"### 👤 Empleado: `{st.session_state['cedula']}`")
    modulo = st.sidebar.radio("Navegación:", [
        "Módulo 1: Equipo de Canastas Aptas", "📝 Evaluación Módulo 1",
        "Módulo 2: Equipo de Canastas No Aptas", "📝 Evaluación Módulo 2",
        "Módulo 3: Lavado y Desinfección de Canastas", "📝 Evaluación Módulo 3"
    ])
    
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- LÓGICA DE EVALUACIONES ---
    if "Evaluación" in modulo:
        st.markdown(f"<h2 class='module-title'>{modulo}</h2>", unsafe_allow_html=True)
        st.write("Responda correctamente para obtener su certificado (Min 80%).")
        
        with st.form("quiz_form"):
            # Simulamos 5 preguntas (cada una vale 20%)
            q1 = st.radio("1. ¿Cuántos niveles de canastas lleva el arrume?", ["8", "16", "24"])
            q2 = st.radio("2. ¿Qué presión en PSI se usa para el preenjuague?", ["1500", "1700", "2000"])
            q3 = st.radio("3. ¿Está permitido enjuagar el desinfectante Biosanit?", ["Sí", "No"])
            q4 = st.radio("4. ¿Se debe usar gancho para arrastrar arrumes?", ["Sí", "No"])
            q5 = st.radio("5. ¿Cuál es el tiempo mínimo de secado?", ["2 horas", "4 horas", "8 horas"])
            
            if st.form_submit_button("Enviar Evaluación"):
                score = 0
                if q1 == "16": score += 20
                if q2 == "1700": score += 20
                if q3 == "No": score += 20
                if q4 == "No": score += 20
                if q5 == "4 horas": score += 20
                
                if score >= 80:
                    st.success(f"¡Felicitaciones! Aprobaste con {score}%.")
                    st.balloons()
                    st.download_button("📥 Descargar Certificado", data=f"Certificado de aprobación: {modulo} para Cédula {st.session_state['cedula']}", file_name="certificado.txt")
                else:
                    st.error(f"Puntaje insuficiente: {score}%. Debes obtener al menos 80%. Intenta nuevamente.")

    # --- CONTENIDO DE MÓDULOS (PREVIO) ---
    elif modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 class='module-title'>📦 Módulo 1: Control y Uso de Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        st.info("✅ **Arrume de 16 niveles por estiba Ovoid.**")