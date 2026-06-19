# Let's check for any compilation errors in the full code structure.
full_code = '''import streamlit as st
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
                    df_auth = pd.read_csv(csv_path, sep=None, engine='python')
                    df_auth.columns = df_auth.columns.str.strip()
                    
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
    opt_m1 = "Módulo 1: Equipo de Canastas Aptas"
    opt_e1 = "    📝 Evaluación"
    opt_c1 = "    🎓 Certificado"
    
    opt_m2 = "Módulo 2: Equipo de Canastas No Aptas"
    opt_e2 = "    📝 Evaluación\u200b"
    opt_c2 = "    🎓 Certificado\u200b"
    
    opt_m3 = "Módulo 3: Lavado y Desinfección"
    opt_e3 = "    📝 Evaluación\u200b\u200b"
    opt_c3 = "    🎓 Certificado\u200b\u200b"

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

    if modulo == opt_m1:
        st.markdown("<h2 style='color: #008a3e;'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        tabs = st.tabs(["🕒 Cronología", "🔍 Partes", "📐 Dimensiones", "🔄 Sistemas", "🚫 Usos Indebidos", "🥚 Carga y Huevos", "🏗️ Estibado y Armado", "🏢 Almacenamiento"])

        with tabs[0]:
            st.subheader("Cronología de la Canasta Ovoid")
            col_izq, col_der = st.columns([2.2, 1])
            with col_izq:
                imagen_cronologia_cargada = False
                for nombre in ["Slide4.PNG", "Slide4.png", "cronologia.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; -webkit-transform: translateZ(0); transform: translateZ(0); border-radius: 8px;">', unsafe_allow_html=True)
                        imagen_cronologia_cargada = True
                        break
                if not imagen_cronologia_cargada:
                    st.info("💡 Diapositiva: Slide4.PNG")
            with col_der:
                if os.path.exists("Video.mp4"):
                    st.video("Video.mp4")
                else:
                    imagen_presentador_cargada = False
                    for nombre in ["Slide3.PNG", "Slide3.png", "introduccion_cronologia.png"]:
                        if os.path.exists(nombre):
                            img_base64 = get_base64_image(nombre)
                            st.markdown(f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; -webkit-transform: translateZ(0); transform: translateZ(0); border-radius: 8px;">', unsafe_allow_html=True)
                            imagen_presentador_cargada = True
                            break
                    if not imagen_presentador_cargada:
                        st.info("💡 Diapositiva: Slide3.PNG")

        with tabs[1]:
            st.subheader("Partes de la Canasta Ovoid")
            imagen_encontrada_p1 = False
            for nombre in ["Partes.png", "Slide5.PNG", "Slide5.png", "partes.png", "image_3a2949.jpg"]:
                if os.path.exists(nombre):
                    img_base64 = get_base64_image(nombre)
                    st.markdown(f'<div style="max-width: 750px; margin: 0 auto 20px auto;"><img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto; display: block; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px;"></div>', unsafe_allow_html=True)
                    imagen_encontrada_p1 = True
                    break
            if not imagen_encontrada_p1:
                st.info("💡 Diapositiva: Partes.png")
                
            if os.path.exists("Partes2.png"):
                img_base64_2 = get_base64_image("Partes2.png")
                st.markdown(f'<div style="max-width: 750px; margin: 20px auto 20px auto;"><img src="data:image/png;base64,{img_base64_2}" style="width: 100%; height: auto; display: block; image-rendering: -webkit-optimize-contrast; image-rendering: high-quality; border-radius: 8px;"></div>', unsafe_allow_html=True)
            else:
                st.info("💡 Diapositiva: Partes2.png")

        with tabs[2]:
            st.subheader("Ficha Técnica: Componentes y Dimensiones")
            col_comp, col_dim = st.columns(2)
            with col_comp:
                img_found = False
                for nombre in ["Canasta Kikes.png", "Slide6.PNG", "Slide6.png", "canasta_kikes_ficha.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        img_found = True
                        break
            with col_dim:
                img_found = False
                for nombre in ["Dimensiones Canasta Kikes.png", "Dimensiones Canasta.png", "Dimensiones Canasta Ovoid.png", "Slide11.PNG", "Slide11.png", "dimensiones_canasta.png"]:
                    if os.path.exists(nombre):
                        img_base64 = get_base64_image(nombre)
                        st.markdown(f'<div class="uniform-container"><img src="data:image/png;base64,{img_base64}" class="uniform-img"></div>', unsafe_allow_html=True)
                        img_found = True
                        break
            st.markdown("---")

        with tabs[3]:
            st.subheader("Sistemas de la Canasta Ovoid")
            img_found1 = False
            for nombre in ["Sistemas Canasta Ovoid.png", "Slide13.PNG", "Slide13.png", "sistemas_canasta.png"]:
                if os.path.exists(nombre):
                    img_base64 = get_base64_image(nombre)
                    st.markdown(f'<div class="uniform-container" style="height: 380px;"><img src="data:image/png;base64,{img_base64}" class="uniform-img" style="image-rendering: crisp-edges !important;"></div>', unsafe_allow_html=True)
                    img_found1 = True
                    break

        with tabs[4]:
            st.subheader("Usos Indebidos del Equipo")
            st_image_nitida_multiple(["Slide15.PNG", "Slide15.png", "usos_prohibidos.png"], "🚫 Prohibiciones: Cuidado Físico y Ergonomía del Activo")

        with tabs[5]:
            st.subheader("Carga Máxima, Tipos de Huevo y Capacidades")
            st_image_nitida_multiple(["Slide17.PNG", "Slide17.png", "carga_maxima_canasta.png"], "Límites de Peso Máximo Operativo (17.25 kg)")

        with tabs[6]:
            st.subheader("Procedimiento Correcto de Armado y Apilado")
            st_image_nitida_multiple(["Slide28.PNG", "Slide28.png", "apilado_pasos.png"], "Paso a Paso del Apilado de la Canasta Ovoid")

        with tabs[7]:
            st.subheader("Estándares de Almacenamiento y Retorno")
            st_image_nitida_multiple(["Slide36.PNG", "Slide36.png", "anidado_pasos.png"], "Paso a Paso del Anidado de Canastas Vacías")

    elif modulo == opt_e1:
        st.subheader("Evaluación de Conocimientos Técnicos - Módulo 1")
        with st.form("quiz_m1"):
            p1 = st.radio("¿Sentido del identificador al anidar canastas VACÍAS?", ["Costado opuesto", "Mismo costado"], key="m1_p1")
            submit_eval = st.form_submit_button("Finalizar Evaluación")
        if submit_eval:
            st.session_state['score_m1'] = 100
            st.session_state['aprobado_m1'] = True

    elif modulo == opt_c1:
        st.subheader("Certificado Oficial Módulo 1")
        if st.session_state['aprobado_m1']:
            logo_base64 = get_base64_image(logo_path) if logo_path else ""
            certificado_html = f"""
            <div style="border: 15px solid #008a3e; padding: 40px; text-align: center; background-color: white; border-style: double; margin: 20px 0;">
                <img src="data:image/png;base64,{logo_base64}" width="150">
            </div>
            """
            st.markdown(certificado_html, unsafe_allow_html=True)
            st.download_button(
                label="📥 Guardar Registro de Certificado (TXT)",
                data="""CERTIFICADO HUEVOS KIKES""",
                file_name="Certificado.txt",
                mime="text/plain",
                key="dl_m1"
            )

    elif modulo == opt_m2:
        st.markdown("<h2 style='color: #008a3e;'>📦 Módulo 2: Equipo de Canastas No Aptas</h2>", unsafe_allow_html=True)
        
    elif modulo == opt_e2:
        st.subheader("Evaluación de Conocimientos Técnicos - Módulo 2")

    elif modulo == opt_c2:
        st.subheader("Certificado Oficial Módulo 2")

    elif modulo == opt_m3:
        st.markdown("<h2 style='color: #008a3e;'>🧼 Módulo 3: Lavado y Desinfección</h2>", unsafe_allow_html=True)
        
    elif modulo == opt_e3:
        st.subheader("Evaluación de Conocimientos Técnicos - Módulo 3")

    elif modulo == opt_c3:
        st.subheader("Certificado Oficial Módulo 3")
'''

try:
    compile(full_code, "app.py", "exec")
    print("Code compiles cleanly with no syntax errors!")
except SyntaxError as e:
    print(f"Syntax Error found: {e}")