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
    imagen_encontrada = False
    for nombre in posibles_nombres:
        if os.path.exists(nombre):
            if subtitulo_opcional:
                st.markdown(f"<p style='text-align: center; color: #1b5e20; font-weight: bold; font-size: 15px; margin-top: 10px;'>{subtitulo_opcional}</p>", unsafe_allow_html=True)
            _, col_img, _ = st.columns([1, 4, 1]) 
            with col_img: 
                st.image(nombre, use_container_width=True)
            imagen_encontrada = True
            break
    if not imagen_encontrada:
        # Mensaje informativo elegante si aún no se han subido las imágenes exportadas del PPTX
        st.info(f"💡 Diapositiva: {posibles_nombres[0]} (Suba la imagen para visualizarla en este apartado)")

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
                csv_path = "Cadena de abastecimiento (1).xlsx - Cadena de abastecimiento.csv"
                try:
                    # Detección inteligente automática de separador (coma o punto y coma)
                    df_auth = pd.read_csv(csv_path, sep=None, engine='python')
                    df_auth.columns = df_auth.columns.str.strip()
                    
                    # Formateo y limpieza de números de identificación flotantes a enteros limpios
                    cedulas_validas = set()
                    if 'Identificacion' in df_auth.columns:
                        for x in df_auth['Identificacion'].dropna():
                            try:
                                f_val = float(x)
                                if f_val.is_integer():
                                    cedulas_validas.add(str(int(f_val)))
                                else:
                                    cedulas_validas.add(str(f_val))
                            except:
                                cedulas_validas.add(str(x).strip())
                    else:
                        st.error("No se encontró la columna 'Identificacion' en el archivo.")
                except Exception as e:
                    cedulas_validas = set()
                    st.error("Error al cargar la base de datos de autorización. Verifique el archivo CSV.")

                input_cedula = ced.strip()
                if input_cedula in cedulas_validas:
                    st.session_state['cedula'] = input_cedula
                    st.rerun()
                else: 
                    st.error("Número de cédula no autorizado o no registrado en el personal de Cadena de Abastecimiento.")
else:
    # Definición de opciones de menú exactamente idénticas en aspecto usando caracteres invisibles únicos
    opt_m1 = "Módulo 1: Equipo de Canastas Aptas"
    opt_e1 = "    📝 Evaluación"
    opt_c1 = "    🎓 Certificado"
    
    opt_m2 = "Módulo 2: Equipo de Canastas No Aptas"
    opt_e2 = "    📝 Evaluación\u200b"
    opt_c2 = "    🎓 Certificado\u2