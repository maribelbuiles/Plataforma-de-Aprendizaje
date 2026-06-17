import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS PARA MÁXIMA NITIDEZ
st.set_page_config(page_title="Ruta de Aprendizaje Kikes", page_icon="📦", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #f7fbf7; }
        
        .main-banner {
            background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }

        /* 🎯 CSS PARA FORZAR NITIDEZ EXTREMA (CRISP EDGES) */
        img {
            image-rendering: -webkit-optimize-contrast !important;
            image-rendering: crisp-edges !important;
            image-rendering: -moz-crisp-edges !important;
            image-rendering: -o-crisp-edges !important;
            image-rendering: high-quality !important;
            -ms-interpolation-mode: nearest-neighbor !important;
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 8px;
        }

        .stButton>button {
            border-radius: 30px;
            background-color: #008a3e;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTROL DEL ESTADO DE SESIÓN ---
if 'cedula' not in st.session_state: st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    logo = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)
    if logo:
        _, col_l, _ = st.columns([3, 1, 3])
        with col_l: st.image(logo, use_container_width=True)
            
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1></div>", unsafe_allow_html=True)
    _, col_f, _ = st.columns([1, 1.5, 1])
    with col_f:
        with st.form("login"):
            ced = st.text_input("Número de Cédula del Empleado:")
            if st.form_submit_button("Ingresar a la Capacitación"):
                if ced.isdigit() and len(ced) >= 5:
                    st.session_state['cedula'] = ced
                    st.rerun()
                else: st.error("Cédula no válida.")
else:
    # --- NAVEGACIÓN ---
    st.sidebar.markdown(f"### 👤 Empleado: `{st.session_state['cedula']}`")
    modulo = st.sidebar.radio("🗺️ Mapa de Ruta Pro", [
        "Módulo 1: Equipo de Canastas Aptas", 
        "📝 Evaluación Módulo 1",
        "Módulo 2: Equipo de Canastas No Aptas", 
        "Módulo 3: Lavado y Desinfección"
    ])
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- CONTENIDO MÓDULO 1 ---
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 style='color: #008a3e;'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        tabs = st.tabs(["🕒 Historia", "🔍 Partes", "📐 Dimensiones", "🔄 Sistemas", "🚛 Cargue", "🚫 Prohibiciones"])

        def st_image_nitida(path):
            if os.path.exists(path):
                _, col_img, _ = st.columns([1, 3, 1]) 
                with col_img: st.image(path, use_container_width=True)

        with tabs[0]:
            st.subheader("Cronología de la Canasta Ovoid")
            st_image_nitida("cronologia.png")
        with tabs[1]:
            st.subheader("Partes de la Canasta Ovoid")
            st_image_nitida("partes.png")
        with tabs[2]:
            st.subheader("Ficha Técnica: Dimensiones")
            st_image_nitida("dimensiones.png")
        with tabs[3]:
            st.subheader("Sistemas de Apilado y Anidado")
            st_image_nitida("sistemas.png")
        with tabs[4]:
            st.subheader("Tablas de Cargue y Autoventa")
            st_image_nitida("cargue_vehiculos.png")
        with tabs[5]:
            st.subheader("🚫 Usos Indebidos del Equipo")
            st_image_nitida("usos_prohibidos.png")

    # --- EVALUACIÓN (CORREGIDA PARA EL CERTIFICADO) ---
    elif "Evaluación" in modulo:
        st.markdown(f"<h2 style='color: #008a3e;'>{modulo}</h2>", unsafe_allow_html=True)
        
        # El formulario solo contiene las preguntas y el botón de envío
        with st.form("quiz"):
            p1 = st.radio("¿Sentido del identificador al anidar canastas VACÍAS?", ["Costado opuesto", "Mismo costado"])
            p2 = st.radio("¿Peso máximo permitido por canasta cargada?", ["15.5 kg", "17.25 kg", "20 kg"])
            p3 = st.radio("¿Cuántas canastas carga un Minitruck TM?", ["75", "100", "48"])
            p4 = st.radio("¿Se permite usar la canasta como escalera?", ["Sí", "No"])
            p5 = st.radio("¿Cuántas canastas vacías se anidan en un arrume por estiba Ovoid?", ["11", "16", "24"])
            
            submit_eval = st.form_submit_button("Finalizar Evaluación")

        # La lógica del resultado y el botón de descarga van FUERA del st.form
        if submit_eval:
            score = 0
            if p1 == "Mismo costado": score += 20
            if p2 == "17.25 kg": score += 20
            if p3 == "75": score += 20
            if p4 == "No": score += 20
            if p5 == "16": score += 20
            
            if score >= 80:
                st.success(f"¡APROBADO! Puntaje obtenido: {score}%")
                st.balloons()
                
                # Formateo del Certificado
                certificado_contenido = f"""
                ==========================================
                CERTIFICADO DE APROBACIÓN TÉCNICA
                ==========================================
                EMPLEADO: {st.session_state['cedula']}
                CURSO: {modulo}
                CALIFICACIÓN: {score}%
                ESTADO: APROBADO
                ==========================================
                """
                
                st.download_button(
                    label="📥 Descargar Certificado de Aprobación",
                    data=certificado_contenido,
                    file_name=f"Certificado_Modulo1_{st.session_state['cedula']}.txt",
                    mime="text/plain"
                )
            else:
                st.error(f"Puntaje insuficiente: {score}%. Debes obtener al menos un 80% para aprobar. Repasa el material e intenta de nuevo.")
    else:
        st.write("Módulo informativo.")