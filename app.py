import streamlit as st
import os
import base64

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

        /* 🎯 CSS PARA FORZAR NITIDEZ EXTREMA DE IMÁGENES DE DIAPOSITIVAS */
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
        
        /* Contenedor elegante de advertencias logísticas */
        .info-card-kikes {
            background-color: #e8f5e9;
            border-left: 6px solid #008a3e;
            padding: 15px;
            border-radius: 4px;
            margin-top: 10px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Función para convertir imagen local a Base64 (necesario para el certificado HTML)
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- CONTROL DEL ESTADO DE SESIÓN ---
if 'cedula' not in st.session_state: 
    st.session_state['cedula'] = None

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
                if ced.isdigit() and len(ced) >= 5:
                    st.session_state['cedula'] = ced
                    st.rerun()
                else: 
                    st.error("Cédula no válida.")
else:
    # --- NAVEGACIÓN LATERAL ---
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

    # --- CONTENIDO MÓDULO 1 (REDISEÑADO CON LAS DIAPOSITIVAS DE LA PPT CORPORATIVA) ---
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 style='color: #008a3e;'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        
        # Pestañas basadas al 100% en el orden e información de "Equipo Canastas Aptas.pptx"
        tabs = st.tabs([
            "📋 Portada", 
            "🕒 Cronología", 
            "🔍 Partes", 
            "📐 Dimensiones", 
            "🔄 Sistemas", 
            "🚫 Usos Indebidos", 
            "📦 Uso Con Producto", 
            "🏗️ Apilado", 
            "🏢 Cedi & CE", 
            "🏭 Plantas"
        ])

        # Función robusta con fallback para renderizar imágenes de la presentación
        def st_image_nitida_multiple(posibles_nombres, subtitulo_opcional=""):
            imagen_encontrada = False
            for nombre in posibles_nombres:
                if os.path.exists(nombre):
                    if subtitulo_opcional:
                        st.markdown(f"<p style='text-align: center; color: #475569; font-weight: bold;'>{subtitulo_opcional}</p>", unsafe_allow_html=True)
                    _, col_img, _ = st.columns([1, 4, 1]) 
                    with col_img: 
                        st.image(nombre, use_container_width=True)
                    imagen_encontrada = True
                    break
            if not imagen_encontrada:
                # Indicador elegante en caso de que falte cargar la diapositiva específica en Streamlit
                st.info(f"Diapositiva disponible: {posibles_nombres[0]} (Suba la imagen para visualizarla en este apartado)")

        # Pestaña 1: Portada
        with tabs[0]:
            st.subheader("Equipo de Canastas Aptas - Ruta de Abastecimiento Nacional")
            st_image_nitida_multiple(
                ["portada.png", "portada.jpg", "Slide1.png", "Slide1.PNG"], 
                "Esquema e Identidad Corporativa de Canastas Aptas"
            )
            st_image_nitida_multiple(
                ["mapa.png", "mapa.jpg", "Slide2.png", "Slide2.PNG"], 
                "Mapa General de Distribución Nacional (Caloto, Bucaramanga, Bogotá D.C., Barranquilla, Cali, etc.)"
            )

        # Pestaña 2: Cronología
        with tabs[1]:
            st.subheader("Cronología de la Canasta Ovoid")
            st_image_nitida_multiple(
                ["cronologia.png", "cronologia.jpg", "Slide3.png", "Slide4.png", "Slide4.PNG"],
                "Línea de Tiempo del Proyecto: Desde el Diseño Conceptual (2019) hasta la Operación Nacional Total (2023)"
            )

        # Pestaña 3: Partes
        with tabs[2]:
            st.subheader("Partes de la Canasta Ovoid")
            st_image_nitida_multiple(
                ["partes.png", "partes.jpg", "image_3a2949.jpg", "Slide5.png", "Slide5.PNG"],
                "Los 9 Componentes del Molde y sus Funciones de Distribución de Carga"
            )

        # Pestaña 4: Dimensiones
        with tabs[3]:
            st.subheader("Ficha Técnica: Dimensiones del Equipo")
            st.write("Medidas del sistema para la prevención de riesgos y un estibado balanceado:")
            st_image_nitida_multiple(
                ["dimensiones.png", "dimensiones.jpg", "Slide6.png", "Slide7.png", "Slide8.png", "Slide9.png", "Slide10.png", "Slide11.png", "Slide12.png"],
                "Dimensiones Oficiales: Canastas Kikes (AFCA022), Estiba (AFES013), Gancho (MDGA105) y Separadores (AFSE003)"
            )

        # Pestaña 5: Sistemas
        with tabs[4]:
            st.subheader("Sistemas de Apilado y Anidado")
            st_image_nitida_multiple(
                ["sistemas.png", "sistemas.jpg", "Slide13.png", "Slide14.png", "Slide14.PNG"],
                "Orientación Técnica de los Identificadores de Color en Costados"
            )

        # Pestaña 6: Usos Indebidos
        with tabs[5]:
            st.subheader("Usos Indebidos de los Activos de Kikes")
            st_image_nitida_multiple(
                ["usos_prohibidos.png", "usos_prohibidos.jpg", "usos_indebidos.png", "usos_indebidos.jpg", "Slide15.png", "Slide16.png", "Slide16.PNG"],
                "🚫 Protocolo de Protección del Activo: Prohibido arrastrar, usar como silla, escalón o guardar basuras"
            )

        # Pestaña 7: Uso Con Producto
        with tabs[6]:
            st.subheader("Uso de Canasta Ovoid con Producto")
            st_image_nitida_multiple(
                ["uso_con_producto.png", "uso_con_producto.jpg", "Slide17.png", "Slide18.png", "Slide19.png", "Slide20.png", "Slide21.png", "Slide22.png", "Slide23.png", "Slide24.png", "Slide25.png", "Slide26.png", "Slide27.png"],
                "Carga Máxima Operativa Autorizada: 17.25 kg y Cantidad Límite de 240 huevos por canasta"
            )

        # Pestaña 8: Apilado
        with tabs[7]:
            st.subheader("Paso a Paso de Apilado de Canasta Ovoid")
            st_image_nitida_multiple(
                ["apilado.png", "apilado.jpg", "apilado_canasta.png", "Slide28.png", "Slide28.PNG"],
                "Procedimiento Correcto para Garantizar la Estabilidad Vertical de las Columnas"
            )

        # Pestaña 9: Cedi & CE
        with tabs[8]:
            st.subheader("Parámetros y Capacidad de Vehículos Autoventa")
            st_image_nitida_multiple(
                ["cedi_ce.png", "cedi_ce.jpg", "cargue_vehiculos.png", "cargue_vehiculos.jpg", "Slide29.png", "Slide30.png", "Slide31.png", "Slide32.png", "Slide33.png", "Slide34.png", "Slide35.png"],
                "Distribución de Vehículos: Límites Técnicos para Dongfeng, Minitruck y Motocarros"
            )

        # Pestaña 10: Plantas
        with tabs[9]:
            st.subheader("Flujos Técnicos y Remontado en Plantas")
            st_image_nitida_multiple(
                ["plantas.png", "plantas.jpg", "Slide36.png", "Slide37.png", "Slide38.png"],
                "Aseguramiento con Ganchos de Estibas Remontadas y Uso del Separador Ovoid"
            )

    # --- EVALUACIÓN Y CERTIFICADO CREATIVO ---
    elif "Evaluación" in modulo:
        st.markdown(f"<h2 style='color: #008a3e;'>{modulo}</h2>", unsafe_allow_html=True)
        
        with st.form("quiz"):
            p1 = st.radio("¿Sentido del identificador al anidar canastas VACÍAS?", ["Costado opuesto", "Mismo costado"])
            p2 = st.radio("¿Peso máximo permitido por canasta cargada?", ["15.5 kg", "17.25 kg", "20 kg"])
            p3 = st.radio("¿Cuántas canastas carga un Minitruck TM?", ["75", "100", "48"])
            p4 = st.radio("¿Se permite usar la canasta como escalera?", ["Sí", "No"])
            p5 = st.radio("¿Cuántas canastas vacías se anidan en un arrume por estiba Ovoid?", ["11", "16", "24"])
            submit_eval = st.form_submit_button("Finalizar Evaluación")

        if submit_eval:
            score = 0
            if p1 == "Mismo costado": score += 20
            if p2 == "17.25 kg": score += 20
            if p3 == "75": score += 20
            if p4 == "No": score += 20
            if p5 == "16": score += 20
            
            if score >= 80:
                st.success(f"¡APROBADO CON {score}%!")
                st.balloons()
                
                # --- CERTIFICADO VISUAL (HTML DINÁMICO) ---
                logo_base64 = get_base64_image(logo_path) if logo_path else ""
                
                certificado_html = f"""
                <div style="border: 15px solid #008a3e; padding: 40px; text-align: center; background-color: white; border-style: double; margin: 20px 0;">
                    <img src="data:image/png;base64,{logo_base64}" width="150" style="margin-bottom: 20px;">
                    <h1 style="color: #008a3e; font-family: 'Georgia', serif; font-size: 45px; margin: 10px 0;">Certificado de Aprobación</h1>
                    <p style="font-size: 20px; color: #333;">La Plataforma de Cadena de Abastecimiento otorga este reconocimiento a:</p>
                    <h2 style="font-size: 35px; color: #000; text-decoration: underline; margin: 20px 0;">ID DE EMPLEADO: {st.session_state['cedula']}</h2>
                    <p style="font-size: 20px; color: #333;">Por completar con éxito y demostrar conocimientos técnicos en:</p>
                    <h3 style="font-size: 28px; color: #2bb673; margin: 15px 0;">{modulo}</h3>
                    <div style="margin-top: 30px; padding: 15px; background-color: #f0f7f0; display: inline-block; border-radius: 10px;">
                        <span style="font-size: 22px; font-weight: bold; color: #008a3e;">Calificación Final: {score}%</span>
                    </div>
                    <p style="margin-top: 40px; font-style: italic; color: #777;">Emitido por el Sistema de Capacitación Técnica de Huevos Kikes</p>
                </div>
                """
                st.markdown(certificado_html, unsafe_allow_html=True)
                
                st.download_button(
                    label="📥 Guardar Registro de Certificado (TXT)",
                    data=f"CERTIFICADO HUEVOS KIKES\nID: {st.session_state['cedula']}\nCurso: {modulo}\nPuntaje: {score}%",
                    file_name=f"Certificado_Kikes_{st.session_state['cedula']}.txt",
                    mime="text/plain"
                )
            else:
                st.error(f"Puntaje insuficiente: {score}%. Necesitas 80% para aprobar. Repasa el material.")
    else:
