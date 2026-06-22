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

        /* 🔍 OPTIMIZACIÓN DE FUENTE GENERAL PARA LETRA ULTRA NÍTIDA */
        html, body, p, h1, h2, h3, h4, h5, h6, label, input, button, select, textarea {
            font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
            -webkit-font-smoothing: antialiased !important;
            -moz-osx-font-smoothing: grayscale !important;
            text-rendering: optimizeLegibility !important;
        }

        /* 📉 OPTIMIZACIÓN DE ESPACIADO EN EL SIDEBAR */
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

        .stButton>button {
            border-radius: 30px;
            background-color: #008a3e;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Función para convertir imagen local a Base64 (necesario para forzar el renderizado HTML controlado)
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Función optimizada: Renderiza imágenes de tamaño MEDIANO (55% de ancho), CENTRADAS y con NITIDEZ forzada por HTML puro
def st_image_nitida_multiple(posibles_nombres, subtitulo_opcional=""):
    for nombre in posibles_nombres:
        if os.path.exists(nombre):
            if subtitulo_opcional:
                st.markdown(f"<p style='text-align: center; color: #1b5e20; font-weight: bold; font-size: 15px; margin-top: 10px;'>{subtitulo_opcional}</p>", unsafe_allow_html=True)
            try:
                img_base64 = get_base64_image(nombre)
                # Forzamos max-width: 55% para que sea de tamaño mediano y margin: 0 auto para centrado absoluto
                st.markdown(f"""
                    <div style="text-align: center; width: 100%; margin: 10px auto;">
                        <img src="data:image/jpeg;base64,{img_base64}" style="max-width: 55%; height: auto; display: inline-block; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px;">
                    </div>
                """, unsafe_allow_html=True)
            except:
                # Fallback tradicional si falla la codificación
                _, col_img, _ = st.columns([1.5, 3, 1.5])
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
    # Opciones del menú
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
                        st.markdown(f'<div style="text-align: center;"><img src="data:image/png;base64,{img_base64}" style="max-width: 90%; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px; display: inline-block;"></div>', unsafe_allow_html=True)
                        break
            with col_der:
                if os.path.exists("Video.mp4"):
                    st.video("Video.mp4")
                else:
                    for nombre in ["Slide3.PNG", "Slide3.png", "introduccion_cronologia.png"]:
                        if os.path.exists(nombre):
                            img_base64 = get_base64_image(nombre)
                            st.markdown(f'<div style="text-align: center;"><img src="data:image/png;base64,{img_base64}" style="max-width: 90%; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px; display: inline-block;"></div>', unsafe_allow_html=True)
                            break

        # Pestaña 2: Partes
        with tabs[1]:
            st.subheader("Partes de la Canasta Ovoid")
            st_image_nitida_multiple(["Partes.png", "Slide5.PNG", "Slide5.png", "partes.png", "image_3a2949.jpg"])
            if os.path.exists("Partes2.png"):
                st_image_nitida_multiple(["Partes2.png"])

        # Pestaña 3: Ficha Técnica (Dimensiones)
        with tabs[2]:
            st.subheader("Ficha Técnica: Componentes y Dimensiones")
            
            # --- CANASTA ---
            col_comp, col_dim = st.columns(2)
            with col_comp:
                for nombre in ["Canasta Kikes.png", "Slide6.PNG", "Slide6.png", "canasta_kikes_ficha.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div style="text-align: center;"><img src="data:image/png;base64,{img_base64}" style="max-width: 85%; max-height: 240px; object-fit: contain; image-rendering: -webkit-optimize-contrast; border-radius: 8px; display: inline-block;"></div>', unsafe_allow_html=True)
                        break
            with col_dim:
                for nombre in ["Dimensiones Canasta Kikes.png", "Dimensiones Canasta.png", "Dimensiones Canasta Ovoid.png", "Slide11.PNG", "Slide11.png", "dimensiones_canasta.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div style="text-align: center;"><img src="data:image/png;base64,{img_base64}" style="max-width: 85%; max-height: 240px; object-fit: contain; image-rendering: -webkit-optimize-contrast; border-radius: 8px; display: inline-block;"></div>',