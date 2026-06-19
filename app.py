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
    # --- NAVEGACIÓN ---
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

    # --- CONTENIDO MÓDULO 1 (SIGUE FIELMENTE EL ORDEN DE TU PPTX CORPORATIVO) ---
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
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

        # Pestaña 1: Cronología (Lado a lado: Infografía a la izquierda, Presentador/Video a la derecha)
        with tabs[0]:
            st.subheader("Cronología de la Canasta Ovoid")
            
            # Diagramación side-by-side con columnas de Streamlit
            col_izq, col_der = st.columns([2.2, 1])
            
            with col_izq:
                # Infografía del timeline (Lado izquierdo)
                imagen_cronologia_cargada = False
                for nombre in ["Slide4.PNG", "Slide4.png", "cronologia.png"]:
                    if os.path.exists(nombre):
                        st.image(nombre, use_container_width=True)
                        imagen_cronologia_cargada = True
                        break
                if not imagen_cronologia_cargada:
                    st.info("💡 Diapositiva: Slide4.PNG (Línea de tiempo de la Cronología)")
                    
            with col_der:
                # Presentador (Video interactivo si existe, o imagen estática en su defecto)
                if os.path.exists("Video.mp4"):
                    st.video("Video.mp4")
                else:
                    imagen_presentador_cargada = False
                    for nombre in ["Slide3.PNG", "Slide3.png", "introduccion_cronologia.png"]:
                        if os.path.exists(nombre):
                            st.image(nombre, use_container_width=True)
                            imagen_presentador_cargada = True
                            break
                    if not imagen_presentador_cargada:
                        st.info("💡 Diapositiva: Slide3.PNG (Presentador de la Cronología)")

        # Pestaña 2: Partes (Slide 5)
        with tabs[1]:
            st.subheader("Partes de la Canasta Ovoid")
            st_image_nitida_multiple(
                ["Partes.png", "Slide5.PNG", "Slide5.png", "partes.png", "image_3a2949.jpg"], 
                "Los 9 Componentes Estructurales de la Canasta"
            )

        # Pestaña 3: Ficha Técnica (Slide 6 a 12)
        with tabs[2]:
            st.subheader("Ficha Técnica: Componentes y Dimensiones")
            st_image_nitida_multiple(
                ["Canasta Kikes.png", "Slide6.PNG", "Slide6.png", "canasta_kikes_ficha.png"], 
                "Canastas Kikes AFCA022"
            )
            st_image_nitida_multiple(
                ["Estiba Ovoid.png", "Slide7.PNG", "Slide7.png", "estiba_ovoid_ficha.png"], 
                "Estiba Ovoid AFES013"
            )
            st_image_nitida_multiple(
                ["Gancho Metálico.png", "Slide8.PNG", "Slide8.png", "gancho_metalico_ficha.png"], 
                "Gancho Metálico MDGA105"
            )
            st_image_nitida_multiple(
                ["Separador Ovoid.png", "Slide9.PNG", "Slide9.png", "separador_ovoid_ficha.png"], 
                "Separador Ovoid AFSE003"
            )
            st_image_nitida_multiple(
                ["Dimensiones Estiba Ovoid.png", "Slide10.PNG", "Slide10.png", "dimensiones_estiba.png"], 
                "Dimensiones Estiba ($124\\text{ cm} \\times 65\\text{ cm} \\times 10.5\\text{ cm}$)"
            )
            st_image_nitida_multiple(
                ["Slide11.PNG", "Slide11.png", "dimensiones_canasta.png"], 
                "Dimensiones Canasta ($63\\text{ cm} \\times 32\\text{ cm} \\times 23\\text{ cm}$)"
            )
            st_image_nitida_multiple(
                ["Dimensiones Separador Ovoid.png", "Slide12.PNG", "Slide12.png", "dimensiones_separador.png"], 
                "Dimensiones Separador ($124\\text{ cm} \\times 66\\text{ cm} \\times 2\\text{ cm}$)"
            )
            st_image_nitida_multiple(
                ["Dimensiones Gancho Metálico.png"], 
                "Dimensiones Gancho Metálico ($8\\text{ cm} \\times 8.6\\text{ cm} \\times 3\\text{ cm}$)"
            )

        # Pestaña 4: Sistemas (Slide 13 y 14)
        with tabs[3]:
            st.subheader("Sistemas de la Canasta Ovoid")
            st_image_nitida_multiple(
                ["Slide13.PNG", "Slide13.png", "sistemas_canasta.png"], 
                "Alineación y Posicionamiento de Identificadores de Color"
            )
            st_image_nitida_multiple(
                ["Slide14.PNG", "Slide14.png", "identificador_posicion_guia.png"], 
                "Uso de Identificador de Posición (Apilar vs Anidar)"
            )

        # Pestaña 5: Usos Indebidos (Slide 15 y 16)
        with tabs[4]:
            st.subheader("Usos Indebidos del Equipo")
            st_image_nitida_multiple(
                ["Slide15.PNG", "Slide15.png", "usos_prohibidos.png"], 
                "🚫 Prohibiciones: Cuidado Físico y Ergonomía del Activo"
            )
            st_image_nitida_multiple(
                ["Slide16.PNG", "Slide16.png", "uso_con_sin_producto.png"], 
                "Guía de Uso del Equipo Ovoid Con y Sin Producto"
            )

        # Pestaña 6: Carga y Huevos (Slide 17 a 27)
        with tabs[5]:
            st.subheader("Carga Máxima, Tipos de Huevo y Capacidades")
            st_image_nitida_multiple(
                ["Slide17.PNG", "Slide17.png", "carga_maxima_canasta.png"], 
                "Límites de Peso Máximo Operativo (17.25 kg)"
            )
            st_image_nitida_multiple(
                ["Slide18.PNG", "Slide18.png", "cantidad_maxima_huevos.png"], 
                "Cantidad Máxima por Canasta (240 Huevos)"
            )
            st_image_nitida_multiple(
                ["Slide19.PNG", "Slide19.png", "tabla_numeros_huevos.png"], 
                "Tabla de Unidades por Canasta Según Tipo de Huevo"
            )
            st_image_nitida_multiple(
                ["Slide20.PNG", "Slide20.png", "estibas_niveles.png"], 
                "Niveles de Remontado en Distribución"
            )
            st_image_nitida_multiple(
                ["Slide21.PNG", "Slide21.png", "cargue_autoventa.png"], 
                "Configuración de Cargue para Autoventa"
            )
            st_image_nitida_multiple(
                ["Slide22.PNG", "Slide22.png", "cargue_plantas.png"], 
                "Líneas de Producción y Carga en Plantas"
            )
            st_image_nitida_multiple(
                ["Slide23.PNG", "Slide23.png", "numeros_huevos_planta.png"], 
                "Consumo e Inventario de Huevos por Tipo"
            )
            st_image_nitida_multiple(
                ["Slide24.PNG", "Slide24.png", "armado_estibas_planta.png"], 
                "Estándar de Armado de Estibas en Clasificadoras"
            )
            st_image_nitida_multiple(
                ["Slide25.PNG", "Slide25.png", "cargue_primera_milla.png"], 
                "Parámetros de Carga en Vehículos de Primera Milla"
            )
            st_image_nitida_multiple(
                ["Slide26.PNG", "Slide26.png", "cargue_tractocamion.png"], 
                "Capacidad Técnica de Carga en Tractocamiones"
            )
            st_image_nitida_multiple(
                ["Slide27.PNG", "Slide27.png", "uso_sin_producto_generalidades.png"], 
                "Reglas Logísticas para Canastas Vacías"
            )

        # Pestaña 7: Estibado y Armado (Slide 28 a 35)
        with tabs[6]:
            st.subheader("Procedimiento Correcto de Armado y Apilado")
            st_image_nitida_multiple(
                ["Slide28.PNG", "Slide28.png", "apilado_pasos.png"], 
                "Paso a Paso del Apilado de la Canasta Ovoid"
            )
            st_image_nitida_multiple(
                ["Slide29.PNG", "Slide29.png", "cedi_ce_generalidades.png"], 
                "Operación en CEDI y Centros de Entrega"
            )
            st_image_nitida_multiple(
                ["Slide30.PNG", "Slide30.png", "dale_sentido_bandeja_video1.png"], 
                "Identificación y Orientación Correcta de la Bandeja"
            )
            st_image_nitida_multiple(
                ["Slide31.PNG", "Slide31.png", "tabla_unidades_cedi.png"], 
                "Capacidades de Distribución en CEDI"
            )
            st_image_nitida_multiple(
                ["Slide32.PNG", "Slide32.png", "llegada_canastas_producto.png"], 
                "Cómo Recibir y Registrar las Canastas con Producto"
            )
            st_image_nitida_multiple(
                ["Slide33.PNG", "Slide33.png", "formas_cargue_autoventa.png"], 
                "Nuevas Formas y Patrones de Cargue de Autoventa"
            )
            st_image_nitida_multiple(
                ["Slide34.PNG", "Slide34.png", "dale_sentido_bandeja_video2.png"], 
                "Aseguramiento de Canastas en Plantas"
            )
            st_image_nitida_multiple(
                ["Slide35.PNG", "Slide35.png", "tabla_unidades_plantas.png"], 
                "Armado de Estibas y Carga de Primera Milla en Plantas"
            )

        # Pestaña 8: Almacenamiento (Slide 36 a 38)
        with tabs[7]:
            st.subheader("Estándares de Almacenamiento y Retorno")
            st_image_nitida_multiple(
                ["Slide36.PNG", "Slide36.png", "anidado_pasos.png"], 
                "Paso a Paso del Anidado de Canastas Vacías"
            )
            st_image_nitida_multiple(
                ["Slide37.PNG", "Slide37.png", "cedi_generalidades_vacias.png"], 
                "Normas de Retorno y Consolidación de Vacíos"
            )
            st_image_nitida_multiple(
                ["Slide38.PNG", "Slide38.png", "almacenamiento_transporte_ficha.png"], 
                "Límites: Niveles de Canastas, Estibas, Separadores y Ganchos"
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
        st.write("Módulo informativo.")