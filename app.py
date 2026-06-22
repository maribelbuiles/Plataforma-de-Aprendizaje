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

        /* 🎯 CSS PARA FORZAR NITIDEZ EXTREMA Y ALINEACIÓN DE IMÁGENES */
        img {
            image-rendering: -webkit-optimize-contrast !important;
            image-rendering: crisp-edges !important;
            image-rendering: -moz-crisp-edges !important;
            image-rendering: -o-crisp-edges !important;
            image-rendering: high-quality !important;
            -ms-interpolation-mode: nearest-neighbor !important;
            display: block !important;
            margin-left: auto !important;
            margin-right: auto !important;
            max-width: 100% !important;
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
            height: 250px;
            width: 100%;
            background-color: transparent;
            overflow: hidden;
            margin-bottom: 10px;
        }

        .uniform-img {
            max-height: 100% !important;
            max-width: 100% !important;
            object-fit: contain !important;
            image-rendering: -webkit-optimize-contrast !important;
            image-rendering: high-quality !important; 
            -webkit-transform: translateZ(0); 
            transform: translateZ(0);
            border-radius: 8px;
            margin: 0 auto !important;
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

# Función para renderizar diapositivas con alta nitidez, centradas y de tamaño mediano-pequeño unificado (450px)
def st_image_nitida_multiple(posibles_nombres, subtitulo_opcional=""):
    for nombre in posibles_nombres:
        if os.path.exists(nombre):
            if subtitulo_opcional:
                st.markdown(f"<p style='text-align: center; color: #1b5e20; font-weight: bold; font-size: 15px; margin-top: 10px;'>{subtitulo_opcional}</p>", unsafe_allow_html=True)
            try:
                img_base64 = get_base64_image(nombre)
                ext = nombre.split('.')[-1].lower()
                mime_type = "image/png" if ext == "png" else "image/jpeg"
                st.markdown(f"""
                    <div style="text-align: center; width: 100%; margin: 10px auto;">
                        <img src="data:{mime_type};base64,{img_base64}" style="max-width: 450px; width: 100%; height: auto; display: inline-block; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px;">
                    </div>
                """, unsafe_allow_html=True)
            except:
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
                        st.markdown(f"""
                            <div style="text-align: center;">
                                <img src="data:image/png;base64,{img_base64}" style="max-width: 450px; width: 100%; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px; display: inline-block;">
                            </div>
                        """, unsafe_allow_html=True)
                        break
            with col_der:
                if os.path.exists("Video.mp4"):
                    st.video("Video.mp4")
                else:
                    for nombre in ["Slide3.PNG", "Slide3.png", "introduccion_cronologia.png"]:
                        if os.path.exists(nombre):
                            img_base64 = get_base64_image(nombre)
                            st.markdown(f"""
                                <div style="text-align: center;">
                                    <img src="data:image/png;base64,{img_base64}" style="max-width: 450px; width: 100%; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px; display: inline-block;">
                                </div>
                            """, unsafe_allow_html=True)
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
            
            # --- 1. CANASTA KIKES Y 2. ESTIBA OVOID LADO A LADO ---
            col_canasta, col_estiba = st.columns(2)
            with col_canasta:
                st_image_nitida_multiple(["Canasta Kikes.png", "Canasta Kikes.jpg", "Slide6.PNG", "Slide6.png"])
            with col_estiba:
                st_image_nitida_multiple(["Estiba Ovoid.png", "Estiba Ovoid.jpg", "Slide7.PNG", "Slide7.png"])
            
            st.markdown("---")

            # --- 3. SEPARADOR Y 4. GANCHO METÁLICO LADO A LADO ---
            col_separador, col_gancho = st.columns(2)
            with col_separador:
                st_image_nitida_multiple(["Separador.png", "Separador Ovoid.png", "Slide9.PNG", "Slide9.png"])
            with col_gancho:
                st_image_nitida_multiple(["Gancho Metálico.png", "Slide8.PNG", "Slide8.png"])

        # Pestaña 4: Sistemas
        with tabs[3]:
            st.subheader("Sistemas de la Canasta Ovoid")
            for nombre in ["Sistemas Canasta Ovoid.png", "Slide13.PNG", "Slide13.png", "sistemas_canasta.png"]:
                if os.path.exists(nombre):
                    img_base64 = get_base64_image(nombre)
                    st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 15px;">
                            <img src="data:image/png;base64,{img_base64}" style="max-width: 60%; height: auto; image-rendering: -webkit-optimize-contrast; border-radius: 8px; display: inline-block;">
                        </div>
                    """, unsafe_allow_html=True)
                    break
            for nombre in ["Slide14.PNG", "Slide14.png", "identificador_posicion_guia.png"]:
                if os.path.exists(nombre):
                    img_base64 = get_base64_image(nombre)
                    st.markdown(f"""
                        <div style="text-align: center;">
                            <img src="data:image/png;base64,{img_base64}" style="max-width: 60%; height: auto; image-rendering: -webkit-optimize-contrast; border-radius: 8px; display: inline-block;">
                        </div>
                    """, unsafe_allow_html=True)
                    break

        # Pestaña 5: Usos Indebidos
        with tabs[4]:
            st.subheader("Usos Indebidos del Equipo")
            st_image_nitida_multiple(["Slide15.PNG", "Slide15.png", "usos_prohibidos.png"], "🚫 Prohibiciones: Cuidado Físico y Ergonomía del Activo")
            st_image_nitida_multiple(["Slide16.PNG", "Slide16.png", "uso_con_sin_producto.png"], "Guía de Uso del Equipo Ovoid Con y Sin Producto")

        # Pestaña 6: Carga y Huevos
        with tabs[5]:
            st.subheader("Carga Máxima, Tipos de Huevo y Capacidades")
            st_image_nitida_multiple(["Slide17.PNG", "Slide17.png", "carga_maxima_canasta.png"], "Límites de Peso Máximo Operativo (17.25 kg)")
            st_image_nitida_multiple(["Slide18.PNG", "Slide18.png", "cantidad_maxima_huevos.png"], "Cantidad Máxima por Canasta (240 Huevos)")
            st_image_nitida_multiple(["Slide19.PNG", "Slide19.png", "tabla_numeros_huevos.png"], "Tabla de Unidades por Canasta Según Tipo de Huevo")
            st_image_nitida_multiple(["Slide20.PNG", "Slide20.png", "estibas_niveles.png"], "Niveles de Remontado en Distribución")
            st_image_nitida_multiple(["Slide21.PNG", "Slide21.png", "cargue_autoventa.png"], "Configuración de Cargue para Autoventa")
            st_image_nitida_multiple(["Slide22.PNG", "Slide22.png", "cargue_plantas.png"], "Líneas de Production y Carga en Plantas")
            st_image_nitida_multiple(["Slide23.PNG", "Slide23.png", "numeros_huevos_planta.png"], "Consumo e Inventario de Huevos por Tipo")
            st_image_nitida_multiple(["Slide24.PNG", "Slide24.png", "armado_estibas_planta.png"], "Estándar de Armado de Estibas en Clasificadoras")
            st_image_nitida_multiple(["Slide25.PNG", "Slide25.png", "cargue_primera_milla.png"], "Parámetros de Carga en Vehículos de Primera Milla")
            st_image_nitida_multiple(["Slide26.PNG", "Slide26.png", "cargue_tractocamion.png"], "Capacidad Técnica de Carga en Tractocamiones")
            st_image_nitida_multiple(["Slide27.PNG", "Slide27.png", "uso_sin_producto_generalidades.png"], "Reglas Logísticas para Canastas Vacías")

        # Pestaña 7: Estibado y Armado
        with tabs[6]:
            st.subheader("Procedimiento Correcto de Armado y Apilado")
            st_image_nitida_multiple(["Slide28.PNG", "Slide28.png", "apilado_pasos.png"], "Paso a Paso del Apilado de la Canasta Ovoid")
            st_image_nitida_multiple(["Slide29.PNG", "Slide29.png", "cedi_ce_generalidades.png"], "Operación en CEDI y Centros de Entrega")
            st_image_nitida_multiple(["Slide30.PNG", "Slide30.png", "dale_sentido_bande_video1.png"], "Identificación y Orientación Correcta de la Bandeja")
            st_image_nitida_multiple(["Slide31.PNG", "Slide31.png", "tabla_unidades_cedi.png"], "Capacidades de Distribución en CEDI")
            st_image_nitida_multiple(["Slide32.PNG", "Slide32.png", "llegada_canastas_producto.png"], "Cómo Recibir y Registrar las Canastas con Producto")
            st_image_nitida_multiple(["Slide33.PNG", "Slide33.png", "formas_cargue_autoventa.png"], "Nuevas Formas y Patrones de Cargue de Autoventa")
            st_image_nitida_multiple(["Slide34.PNG", "Slide34.png", "dale_sentido_bande_video2.png"], "Aseguramiento de Canastas en Plantas")
            st_image_nitida_multiple(["Slide35.PNG", "Slide35.png", "tabla_unidades_plantas.png"], "Armado de Estibas y Carga de Primera Milla en Plantas")

        # Pestaña 8: Almacenamiento
        with tabs[7]:
            st.subheader("Estándares de Almacenamiento y Retorno")
            st_image_nitida_multiple(["Slide36.PNG", "Slide36.png", "anidado_pasos.png"], "Paso a Paso del Anidado de Canastas Vacías")
            st_image_nitida_multiple(