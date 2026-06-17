import streamlit as st
import os

# 1. CONFIGURACIÓN VISUAL
st.set_page_config(page_title="Ruta de Aprendizaje Kikes", page_icon="📦", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #f7fbf7; }
        .slide-container {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 40px;
            border-left: 8px solid #008a3e;
        }
        .main-banner {
            background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        h2 { color: #008a3e; font-family: 'Arial Black'; }
        .stButton>button { border-radius: 30px; background-color: #008a3e; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 2. LÓGICA DE INGRESO Y LOGO
if 'cedula' not in st.session_state: st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    logo_path = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)
    if logo_path:
        _, col_img, _ = st.columns([2.8, 1, 2.8])
        with col_img: st.image(logo_path, use_container_width=True)
            
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1></div>", unsafe_allow_html=True)
    _, col_form, _ = st.columns([1, 1.5, 1])
    with col_form:
        with st.form("login"):
            ced = st.text_input("Número de Cédula del Empleado:")
            if st.form_submit_button("Ingresar a la Capacitación"):
                if ced.isdigit() and len(ced) >= 5:
                    st.session_state['cedula'] = ced
                    st.rerun()
                else: st.error("Ingrese una cédula válida.")
else:
    # 3. NAVEGACIÓN (MAPA DE RUTA)
    st.sidebar.markdown(f"### 👤 Empleado: `{st.session_state['cedula']}`")
    modulo = st.sidebar.radio("🗺️ Mapa de Ruta Pro", [
        "Módulo 1: Equipo de Canastas Aptas", 
        "📝 Evaluación Módulo 1",
        "Módulo 2: Equipo de Canastas No Aptas", 
        "📝 Evaluación Módulo 2",
        "Módulo 3: Lavado y Desinfección",
        "📝 Evaluación Módulo 3"
    ])
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.rerun()

    # 4. CONTENIDO MÓDULO 1 (Organizado como Diapositivas)
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 class='module-title'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        
        # --- DIAPOSITIVA 1: COBERTURA ---
        with st.container():
            st.markdown("<div class='slide-container'>", unsafe_allow_html=True)
            col1, col2 = st.columns([1.2, 1])
            with col1:
                if os.path.exists("mapa.png"): st.image("mapa.png", use_container_width=True)
            with col2:
                st.subheader("Cobertura Nacional")
                st.write("Nuestra red logística conecta plantas y CEDI en todo el país: Santa Marta, Barranquilla, Bucaramanga, Bogotá, Cali y más.")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- DIAPOSITIVA 2: CRONOLOGÍA ---
        with st.container():
            st.markdown("<div class='slide-container'>", unsafe_allow_html=True)
            st.subheader("Cronología de la Canasta Ovoid")
            if os.path.exists("cronologia.png"): st.image("cronologia.png", use_container_width=True)
            st.write("Desde el diseño en 2019 hasta la operación total en 2023, la Canasta Ovoid ha evolucionado para proteger nuestro producto.")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- DIAPOSITIVA 3: PARTES ---
        with st.container():
            st.markdown("<div class='slide-container'>", unsafe_allow_html=True)
            st.subheader("Partes de la Canasta Ovoid")
            if os.path.exists("partes.png"): st.image("partes.png", use_container_width=True)
            st.info("9 componentes clave: Desde el piso tipo bandeja hasta la identidad visual Kikes.")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- DIAPOSITIVA 4: DIMENSIONES ---
        with st.container():
            st.markdown("<div class='slide-container'>", unsafe_allow_html=True)
            st.subheader("Equipo Ovoid: Componentes y Dimensiones")
            if os.path.exists("dimensiones.png"): st.image("dimensiones.png", use_container_width=True)
            st.write("**Fichas Técnicas:** Canasta (AFCA022), Estiba (AFES013), Gancho (MDGA105) y Separador (AFSE003).")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- DIAPOSITIVA 5: SISTEMAS (APILAR/ANIDAR) ---
        with st.container():
            st.markdown("<div class='slide-container'>", unsafe_allow_html=True)
            st.subheader("Sistemas de Posicionamiento")
            if os.path.exists("sistemas.png"): st.image("sistemas.png", use_container_width=True)
            st.success("✅ **Apilar (con producto):** Sentido opuesto. | ✅ **Anidar (vacía):** Mismo costado.")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- DIAPOSITIVA 6: CARGUE Y VEHÍCULOS ---
        with st.container():
            st.markdown("<div class='slide-container'>", unsafe_allow_html=True)
            st.subheader("Cargue por Tipo de Vehículo")
            if os.path.exists("cargue_vehiculos.png"): st.image("cargue_vehiculos.png", use_container_width=True)
            st.write("Optimización para Minitruck, Dongfeng y Motocarros Ayco/Vaisand.")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- DIAPOSITIVA 7: USOS INDEBIDOS ---
        with st.container():
            st.markdown("<div class='slide-container'>", unsafe_allow_html=True)
            st.subheader("🚫 Usos Indebidos")
            if os.path.exists("usos_prohibidos.png"): st.image("usos_prohibidos.png", use_container_width=True)
            st.error("Cuidar el equipo es responsabilidad de todos. Evite sanciones por mal uso.")
            st.markdown("</div>", unsafe_allow_html=True)

    # 5. EVALUACIÓN Y CERTIFICADO
    elif "Evaluación" in modulo:
        st.markdown(f"<h2 class='module-title'>{modulo}</h2>", unsafe_allow_html=True)
        with st.form("quiz_final"):
            st.write("### Valida tus conocimientos")
            p1 = st.radio("¿Cuál es la configuración correcta para anidar canastas vacías?", ["Lado opuesto", "Mismo costado"])
            p2 = st.radio("¿Cuántas canastas carga un vehículo Dongfeng según la tabla?", ["75", "100", "48"])
            p3 = st.radio("¿Cuál es el peso máximo de una canasta cargada?", ["15.5 kg", "17.25 kg", "20 kg"])
            p4 = st.radio("¿Cuántos niveles de canastas vacías se anidan por estiba?", ["8", "11", "16"])
            p5 = st.radio("¿Se puede usar la canasta como silla provisional?", ["Sí", "No"])
            
            if st.form_submit_button("Calificar Evaluación"):
                score = 0
                if p1 == "Mismo costado": score += 20
                if p2 == "100": score += 20
                if p3 == "17.25 kg": score += 20
                if p4 == "16": score += 20
                if p5 == "No": score += 20
                
                if score >= 80:
                    st.success(f"¡APROBADO! Puntaje: {score}%")
                    st.balloons()
                    # Simulación de certificado
                    st.download_button("📜 Descargar Certificado", f"Certificado de Logística Kikes\n\nEl estudiante con cédula {st.session_state['cedula']}\nha aprobado satisfactoriamente el Módulo 1.", f"Certificado_Modulo1_{st.session_state['cedula']}.txt")
                else:
                    st.error(f"Puntaje insuficiente: {score}%. Debes repasar las diapositivas y obtener mínimo 80%.")

    else:
        st.write("Módulo en construcción con la misma estructura visual.")