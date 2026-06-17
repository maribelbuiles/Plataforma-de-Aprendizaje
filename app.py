import streamlit as st
import os

# 1. Configuración y Estilo Kikes
st.set_page_config(page_title="Abastecimiento Kikes", page_icon="📦", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #f7fbf7; }
        .main-banner { background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin-bottom: 20px; }
        .module-title { color: #008a3e; font-family: 'Arial Black'; border-bottom: 3px solid #008a3e; }
        .stButton>button { width: 100%; border-radius: 30px; background-color: #008a3e; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 2. Lógica de Ingreso
if 'cedula' not in st.session_state: st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    logo = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)
    if logo:
        _, col, _ = st.columns([2.5, 1, 2.5])
        with col: st.image(logo, use_container_width=True)
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1></div>", unsafe_allow_html=True)
    _, col_f, _ = st.columns([1, 1.8, 1])
    with col_f:
        with st.form("login"):
            ced = st.text_input("Número de Cédula:")
            if st.form_submit_button("Ingresar"):
                if ced.isdigit() and len(ced) >= 5:
                    st.session_state['cedula'] = ced
                    st.rerun()
else:
    # 3. Menú Lateral (Mapa de Ruta)
    modulo = st.sidebar.radio("🗺️ Mapa de Ruta Pro", [
        "Módulo 1: Equipo de Canastas Aptas", "📝 Evaluación Módulo 1",
        "Módulo 2: Equipo de Canastas No Aptas", "📝 Evaluación Módulo 2",
        "Módulo 3: Lavado y Desinfección", "📝 Evaluación Módulo 3"
    ])
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.rerun()

    # 4. Contenido Módulo 1 (Toda la información del adjunto)
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 class='module-title'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        t1, t2, t3, t4 = st.tabs(["📋 Generalidades", "📐 Dimensiones", "🔄 Sistemas", "🚛 Capacidades"])
        
        with t1:
            st.subheader("Cronología y Partes")
            st.write("**Historia:** 2019 (Diseño) → 2020 (Piloto) → 2021 (Barranquilla) → 2023 (Operación Total).")
            st.write("**Componentes:** 1. Piso Bandeja | 2. Hendiduras | 3. Resistencia | 4. Apilado/Anidado | 5. Identificador | 6. Estructura | 7. Marcación | 8. Manija | 9. Identidad Visual.")
        
        with t2:
            st.subheader("Ficha Técnica")
            st.info("**Canasta Kikes (AFCA022):** 63x32x23 cm | **Estiba Ovoid (AFES013):** 124x65x10.5 cm")
            st.info("**Separador (AFSE003):** 124x66x2 cm | **Gancho (MDGA105):** 8x8.6x3 cm")
        
        with t3:
            st.subheader("Uso Correcto")
            st.success("**Apilar (Con Producto):** Identificadores en sentido OPUESTO.")
            st.success("**Anidar (Vacío):** Identificadores al MISMO COSTADO.")
            st.warning("**🚫 Prohibido:** No usar como silla, no arrastrar con gancho, no usar para basura o elementos ajenos.")
        
        with t4:
            st.subheader("Cargue y Almacenamiento")
            st.write("**Arrume Vacío:** Arrume de 16 niveles por estiba Ovoid.")
            st.write("**Capacidad Huevos:** A-AA-B-M-L (240 sueltos), XL (180 sueltos), JUMBO (120 sueltos).")
            st.write("**Vehículos:** Minitruck (75 canastas), Dongfeng (100), Motocarros (48).")

    # 5. Sistema de Evaluaciones y Certificados
    elif "Evaluación" in modulo:
        st.markdown(f"<h2 class='module-title'>{modulo}</h2>", unsafe_allow_html=True)
        with st.form("quiz"):
            st.write("Examen técnico: Responda correctamente (80% para aprobar).")
            # Preguntas de ejemplo basadas en el contenido
            p1 = st.radio("¿Niveles de canastas vacías por estiba?", ["8", "16", "24"])
            p2 = st.radio("¿Identificadores al anidar vacías?", ["Mismo costado", "Lado opuesto"])
            p3 = st.radio("¿Presión de hidrolavadora?", ["1500 PSI", "1700 PSI"])
            if st.form_submit_button("Finalizar"):
                score = 0
                if p1 == "16": score += 34
                if p2 == "Mismo costado": score += 33
                if p3 == "1700 PSI": score += 33
                
                if score >= 80:
                    st.success(f"¡APROBADO! Puntaje: {score}%")
                    st.download_button("📜 Descargar Certificado", f"Certificado: {st.session_state['cedula']} aprobó {modulo}", f"Certificado_{modulo}.txt")
                else:
                    st.error(f"Reprobado ({score}%). Necesitas 80%.")

    # Otros módulos (resumidos para ligereza)
    else:
        st.markdown(f"<h2 class='module-title'>{modulo}</h2>", unsafe_allow_html=True)
        st.write("Información detallada en los manuales GL-P-01 y GL-P-02.")