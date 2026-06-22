import streamlit as st
import os
import base64
import pandas as pd

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

        /* 🎯 CSS PARA FORZAR NITIDEZ EXTREMA EN DISPOSITIVOS Y PANTALLAS */
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

        /* 🔍 OPTIMIZACIÓN DE FUENTE EXCLUYENDO SELECTORES UNIVERSALES PARA NO ROMPER FUENTES DE ICONOS DE STREAMLIT */
        html, body, p, h1, h2, h3, h4, h5, h6, label, input, button, select, textarea {
            font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
            -webkit-font-smoothing: antialiased !important;
            -moz-osx-font-smoothing: grayscale !important;
            text-rendering: optimizeLegibility !important;
        }

        /* 📉 REDUCIR EL TAMAÑO Y ESPACIADO DE LAS OPCIONES ANIDADAS EN EL SIDEBAR */
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(2),
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(3),
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(5),
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(6),
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(8),
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(9) {
            margin-top: -5px !important;
            margin-bottom: -5px !important;
        }
        
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(2) p,
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(3) p,
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(5) p,
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(6) p,
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(8) p,
        div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > div:nth-child(9) p {
            font-size: 14px !important;
            color: #444444 !important;
        }

        /* 📐 CONTENEDOR AJUSTADO PARA EVITAR CUALQUIER DISTORSIÓN Y MANTENER PROPORCIÓN DE LETRAS */
        .uniform-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 250px; /* Altura fija ideal para visualización limpia */
            width: 100%;
            background-color: transparent;
            overflow: hidden;
            margin-bottom: 10px;
        }

        .uniform-img {
            max-height: 100% !important;
            max-width: 100% !important;
            object-fit: contain !important; /* Protege la imagen contra cualquier tipo de estiramiento o distorsión */
            image-rendering: -webkit-optimize-contrast !important;
            image-rendering: high-quality !important; 
            -webkit-transform: translateZ(0); 
            transform: translateZ(0);
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

# Función para convertir imagen local a Base64 (necesario para el certificado HTML)
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Función para renderizar diapositivas con alta nitidez y soporte de fallback inteligente
def st_image_nitida_multiple(posibles_nombres, subtitulo_opcional=""):
    for nombre in posibles_nombres:
        if os.path.exists(nombre):
            if subtitulo_opcional:
                st.markdown(f"<p style='text-align: center; color: #1b5e20; font-weight: bold; font-size: 15px; margin-top: 10px;'>{subtitulo_opcional}</p>", unsafe_allow_html=True)
            _, col_img, _ = st.columns([1, 4, 1]) 
            with col_img: 
                st.image(nombre, use_container_width=True)
            break

# --- CONTROL DEL ESTADO DE SESIÓN ---
if 'cedula' not in st.session_state: 
    st.session_state['cedula'] = None
if 'aprobado_m1' not in st.session_state: st.session_state['aprobado_m1'] = False
if 'aprobado_m2' not in st.session_state: st.session_state['aprobado_m2'] = False
if 'aprobado_m3' not in st.session_state: st.session_state['aprobado_m3'] = False
if 'score_m1' not in st.session_state: st.session_state['score_m1'] = 0
if 'score_m2' not in st.session_state: st.session_state['score_m2'] = 0
if 'score_m3' not in st.session_state: st.session_state['score_m3'] = 0

# Identificación de logo
logo_path = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)

if st.session_state['cedula'] is None:
    if logo_path:
        _, col_l, _ = st.columns([3, 1, 3])
        with col_l: 
            st.image(logo_path, use_container_width=True)
            
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1></div>", unsafe_allow_html=True)
    _, col_f, _ = st.columns([1, 1.5, 1])
    with col_f:
        with st.form("login"):
            ced = st.text_input("Número de Cédula del Empleado:")
            if st.form_submit_button("Ingresar a la Capacitación"):
                input_cedula = ced.strip()
                if input_cedula.isdigit() and len(input_cedula) >= 5:
                    st.session_state['cedula'] = input_cedula
                    st.rerun()
                else: 
                    st.error("Por favor, ingrese un número de cédula válido (mínimo 5 dígitos).")
else:
    # Definición de opciones de menú exactamente idénticas en aspecto usando caracteres invisibles únicos
    opt_m1 = "Módulo 1: Equipo de Canastas Aptas"
    opt_e1 = "    📝 Evaluación"
    opt_c1 = "    🎓 Certificado"
    
    opt_m2 = "Módulo 2: Equipo de Canastas No Aptas"
    opt_e2 = "    📝 Evaluación\u200b"
    opt_c2 = "    🎓 Certificado\u200b"
    
    opt_m3 = "Módulo 3: Lavado y Desinfección"
    opt_e3 = "    📝 Evaluación\u200b\u200b"
    opt_c3 = "    🎓 Certificado\u200b\u200b"

    # --- NAVEGACIÓN ANIDADA ---
    st.sidebar.markdown(f"### 👤 Empleado: `{st.session_state['cedula']}`")
    modulo = st.sidebar.radio("🗺️ Mapa de Ruta Pro", [
        opt_m1, opt_e1, opt_c1,
        opt_m2, opt_e2, opt_c2,
        opt_m3, opt_e3, opt_c3
    ])
    
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.session_state['aprobado_m1'] = False
        st.session_state['aprobado_m2'] = False
        st.session_state['aprobado_m3'] = False
        st.session_state['score_m1'] = 0
        st.session_state['score_m2'] = 0
        st.session_state['score_m3'] = 0
        st.rerun()

    # --- CONTENIDO MÓDULO 1 ---
    if modulo == opt_m1:
        st.markdown("<h2 style='color: #008a3e;'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        
        tabs = st.tabs([
            "🕒 Cronología", 
            "🔍 Partes", 
            "📐 Dimensiones", 
            "🔄 Sistemas", 
            "🚫 Usos Indebidos", 
            "🥚 Carga y Huevos", 
            "🏗️ Estibado y Armado", 
            "🏢 Almacenamiento"
        ])

        # Pestaña 1: Cronología
        with tabs[0]:
            st.subheader("Cronología de la Canasta Ovoid")
            col_izq, col_der = st.columns([2.2, 1])
            with col_izq:
                for nombre in ["Slide4.PNG", "Slide4.png", "cronologia.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; -webkit-transform: translateZ(0); transform: translateZ(0); border-radius: 8px;">', unsafe_allow_html=True)
                        break
            with col_der:
                if os.path.exists("Video.mp4"):
                    st.video("Video.mp4")
                else:
                    for nombre in ["Slide3.PNG", "Slide3.png", "introduccion_cronologia.png"]:
                        if os.path.exists(nombre):
                            img_base64 = get_base64_image(nombre)
                            st.markdown(f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px;">', unsafe_allow_html=True)
                            break

        # Pestaña 2: Partes
        with tabs[1]:
            st.subheader("Partes de la Canasta Ovoid")
            st_image_nitida_multiple(["Partes.png", "Slide5.PNG", "Slide5.png", "partes.png", "image_3a2949.jpg"])
            if os.path.exists("Partes2.png"):
                st_image_nitida_multiple(["Partes2.png"])

        # Pestaña 3: Ficha Técnica
        with tabs[2]:
            st.subheader("Ficha Técnica: Componentes y Dimensiones")
            
            # --- CANASTA ---
            col_comp, col_dim = st.columns(2)
            with col_comp:
                for nombre in ["Canasta Kikes.png", "Slide6.PNG", "Slide6.png", "canasta_kikes_ficha.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        break
            with col_dim:
                for nombre in ["Dimensiones Canasta Kikes.png", "Dimensiones Canasta.png", "Dimensiones Canasta Ovoid.png", "Slide11.PNG", "Slide11.png", "dimensiones_canasta.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        break
            st.markdown("---")
            
            # Se anexa la estiba completa en tamaño proporcional buscando todas las extensiones posibles (.jpg, .png, etc.)
            st_image_nitida_multiple(["Estiba Ovoid.jpg", "Estiba Ovoid.png", "Slide7.PNG", "Slide7.png", "estiba_ovoid_ficha.png"])

            # --- ESTIBA ---
            col_comp, col_dim = st.columns(2)
            with col_comp:
                for nombre in ["Estiba Ovoid.jpg", "Estiba Ovoid.png", "Slide7.PNG", "Slide7.png", "estiba_ovoid_ficha.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        break
            with col_dim:
                for nombre in ["Dimensiones Estiba Ovoid.png", "Slide10.PNG", "Slide10.png", "dimensiones_estiba.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        break
            st.markdown("---")
            
            # --- GANCHO METÁLICO ---
            col_comp, col_dim = st.columns(2)
            with col_comp:
                for nombre in ["Gancho Metálico.png", "Slide8.PNG", "Slide8.png", "gancho_metalico_ficha.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        break
            with col_dim:
                for nombre in ["Dimensiones Gancho Metálico.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        break
            st.markdown("---")
            
            # --- SEPARADOR OVOID ---
            col_comp, col_dim = st.columns(2)
            with col_comp:
                for nombre in ["Separador Ovoid.png", "Slide9.PNG", "Slide9.png", "separador_ovoid_ficha.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        break
            with col_dim:
                for nombre in ["Dimensiones Separador Ovoid.png", "Slide12.PNG", "Slide12.png", "dimensiones_separador.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        break

        # Pestaña 4: Sistemas
        with tabs[3]:
            st.subheader("Sistemas de la Canasta Ovoid")
            for nombre in ["Sistemas Canasta Ovoid.png", "Slide13.PNG", "Slide13.png", "sistemas_canasta.png"]:
                if os.path.exists(nombre):
                    img_base64 = get_base64_image(nombre)
                    st.markdown(f'<div class="uniform-container" style="height: 380px;"><img src="data:image/png;base64,{img_base64}" class="uniform-img" style="image-rendering: crisp-edges !important;"></div>', unsafe_allow_html=True)
                    break
            for nombre in ["Slide14.PNG", "Slide14.png", "identificador_posicion_guia.png"]:
                if os.path.exists(nombre):
                    img_base64 = get_base6