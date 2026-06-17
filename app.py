import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS
st.set_page_config(page_title="Ruta de Aprendizaje Kikes", page_icon="📦", layout="wide")

st.markdown("""
    <style>
        /* Fondo y tipografía */
        .stApp { background-color: #f7fbf7; }
        
        /* Banner Principal */
        .main-banner {
            background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        /* Forzar Nitidez en Imágenes */
        img {
            image-rendering: -webkit-optimize-contrast; /* Chrome/Safari */
            image-rendering: crisp-edges;
            border-radius: 10px;
        }

        /* Estilo de Tarjetas */
        .info-card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid #008a3e;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        /* Botones */
        .stButton>button {
            border-radius: 30px;
            background-color: #008a3e;
            color: white;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover { background-color: #006a2e; transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# 2. LOGO Y ACCESO
if 'cedula' not in st.session_state: st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    # Búsqueda de logo inteligente
    logo = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)
    if logo:
        _, col_l, _ = st.columns([2.8, 1, 2.8])
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
                else: st.error("Por favor, ingrese un número de cédula válido.")
else:
    # 3. SIDEBAR (Navegación)
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

    # 4. CONTENIDO MÓDULO 1 (POR PESTAÑAS)
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 style='color: #008a3e;'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        
        # Creación de Pestañas idénticas a las diapositivas
        tabs = st.tabs(["🌎 Cobertura", "🕒 Historia", "🔍 Partes", "📐 Dimensiones", "🔄 Sistemas", "🚛 Cargue", "🚫 Prohibiciones"])

        with tabs[0]:
            st.subheader("Cobertura Nacional Kikes")
            if os.path.exists("mapa.png"): st.image("mapa.png", use_container_width=True)
            st.markdown("<div class='info-card'>Red logística nacional conectando Plantas, CEDI y Centros de Distribución.</div>", unsafe_allow_html=True)

        with tabs[1]:
            st.subheader("Cronología de la Canasta Ovoid")
            if os.path.exists("cronologia.png"): st.image("cronologia.png", use_container_width=True)
            st.write("Evolución constante desde el diseño en 2019 hasta la operación total en 2023.")

        with tabs[2]:
            st.subheader("Partes de la Canasta Ovoid")
            if os.path.exists("partes.png"): st.image("partes.png", use_container_width=True)
            st.markdown("<div class='info-card'>9 Componentes diseñados para máxima resistencia y protección biológica.</div>", unsafe_allow_html=True)

        with tabs[3]:
            st.subheader("Ficha Técnica: Componentes y Dimensiones")
            if os.path.exists("dimensiones.png"): st.image("dimensiones.png", use_container_width=True)
            st.write("Especificaciones para: Canasta (AFCA022), Estiba (AFES013), Gancho (MDGA105) y Separador (AFSE003).")

        with tabs[4]:
            st.subheader("Sistemas de Apilado y Anidado")
            if os.path.exists("sistemas.png"): st.image("sistemas.png", use_container_width=True)
            st.success("✅ **Apilar (con producto):** Identificadores en sentido opuesto. | ✅ **Anidar (vacía):** Identificadores al mismo costado.")

        with tabs[5]:
            st.subheader("Tablas de Cargue y Autoventa")
            if os.path.exists("cargue_vehiculos.png"): st.image("cargue_vehiculos.png", use_container_width=True)
            st.info("Configuraciones de niveles según el tipo de vehículo: Minitruck, Dongfeng y Motocarros.")

        with tabs[6]:
            st.subheader("🚫 Usos Indebidos del Equipo")
            if os.path.exists("usos_prohibidos.png"): st.image("usos_prohibidos.png", use_container_width=True)
            st.error("Garantizar la vida útil del equipo es responsabilidad de todos los colaboradores.")

    # 5. SISTEMA DE EVALUACIÓN (80% PARA APROBAR)
    elif "Evaluación" in modulo:
        st.markdown(f"<h2 style='color: #008a3e;'>{modulo}</h2>", unsafe_allow_html=True)
        with st.form("quiz"):
            st.write("### Examen Técnico Operativo")
            p1 = st.radio("¿Sentido del identificador al anidar canastas VACÍAS?", ["Costado opuesto", "Mismo costado"])
            p2 = st.radio("¿Peso máximo permitido por canasta cargada?", ["15.5 kg", "17.25 kg", "20 kg"])
            p3 = st.radio("¿Cuántas canastas carga un Minitruck TM?", ["75", "100", "48"])
            p4 = st.radio("¿Se permite usar la canasta como escalera?", ["Sí", "No"])
            p5 = st.radio("¿Cuántos niveles de canastas vacías se anidan por estiba?", ["11", "16", "24"])
            
            if st.form_submit_button("Finalizar Evaluación"):
                score = 0
                if p1 == "Mismo costado": score += 20
                if p2 == "17.25 kg": score += 20
                if p3 == "75": score += 20
                if p4 == "No": score += 20
                if p5 == "16": score += 20
                
                if score >= 80:
                    st.success(f"¡APROBADO! Puntaje obtenido: {score}%")
                    st.balloons()
                    st.download_button("📜 Descargar Certificado", f"CERTIFICADO DE APROBACIÓN\n\nEmpleado: {st.session_state['cedula']}\nMódulo: {modulo}\nEstado: Aprobado", f"Certificado_{st.session_state['cedula']}.txt")
                else:
                    st.error(f"Puntaje: {score}%. Requieres mínimo 80% para aprobar. Repasa el material e intenta de nuevo.")

    else:
        st.write("Módulo informativo.")