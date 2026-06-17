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

        /* CSS PARA FORZAR NITIDEZ EXTREMA */
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

# 2. LOGO Y ACCESO
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
            ced = st.text_input("Ingrese su Cédula para comenzar:")
            if st.form_submit_button("Ingresar a la Capacitación"):
                if ced.isdigit() and len(ced) >= 5:
                    st.session_state['cedula'] = ced
                    st.rerun()
                else: st.error("Cédula no válida.")
else:
    # 3. SIDEBAR
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

    # 4. CONTENIDO MÓDULO 1
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 style='color: #008a3e;'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        
        # Pestañas actualizadas (sin Cobertura)
        tabs = st.tabs(["🕒 Historia", "🔍 Partes", "📐 Dimensiones", "🔄 Sistemas", "🚛 Cargue", "🚫 Prohibiciones"])

        def st_image_nitida(path):
            if os.path.exists(path):
                _, col_img, _ = st.columns([0.5, 5, 0.5]) 
                with col_img:
                    st.image(path, use_container_width=True)

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

    # 5. EVALUACIÓN
    elif "Evaluación" in modulo:
        st.markdown(f"<h2 style='color: #008a3e;'>{modulo}</h2>", unsafe_allow_html=True)
        with st.form("quiz"):
            p1 = st.radio("¿Sentido del identificador al anidar canastas VACÍAS?", ["Costado opuesto", "Mismo costado"])
            p2 = st.radio("¿Peso máximo permitido por canasta cargada?", ["15.5 kg", "17.25 kg", "20 kg"])
            p3 = st.radio("¿Cuántas canastas carga un Minitruck TM?", ["75", "100", "48"])
            p4 = st.radio("¿Se permite usar la canasta como escalera?", ["Sí", "No"])
            p5 = st.radio("¿Cuántos niveles de canastas vacías se anidan por estiba?", ["11", "16", "24"])
            
            if st.form_submit_button("Finalizar Evaluación"):
                score = ( (p1=="Mismo costado") + (p2=="17.25 kg") + (p3=="75") + (p4=="No") + (p5=="16") ) * 20
                if score >= 80:
                    st.success(f"¡APROBADO! Puntaje: {score}%")
                    st.balloons()
                    st.download_button("📜 Descargar Certificado", f"Aprobado por: {st.session_state['cedula']}", f"Cert_Mod1.txt")
                else:
                    st.error(f"Puntaje: {score}%. Requieres 80%.")
    else:
        st.write("Módulo informativo en construcción.")