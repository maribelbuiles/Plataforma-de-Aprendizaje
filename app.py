import streamlit as st
import os

# Configuración de página
st.set_page_config(page_title="Aprendizaje Kikes", page_icon="📦", layout="wide")

# Estilos Creativos
st.markdown("""
    <style>
        .stApp { background-color: #f0f7f0; }
        .main-banner { background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; }
        .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 20px; border-top: 5px solid #008a3e; }
        .stButton>button { border-radius: 50px; background-color: #008a3e; color: white; font-weight: bold; height: 3em; }
    </style>
""", unsafe_allow_html=True)

# Función para mostrar imágenes de forma segura
def mostrar_recurso(nombre_archivo, caption=""):
    if os.path.exists(nombre_archivo):
        st.image(nombre_archivo, caption=caption, use_container_width=True)
    else:
        st.info(f"🖼️ Aquí va el recurso: {nombre_archivo}")

# --- LOGIN ---
if 'cedula' not in st.session_state: st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    logo = "logo.png" if os.path.exists("logo.png") else "logo.png.png"
    if os.path.exists(logo):
        _, col_l, _ = st.columns([2.5, 1, 2.5])
        with col_l: st.image(logo, use_container_width=True)
    
    st.markdown("<div class='main-banner'><h1>Plataforma de Aprendizaje Kikes</h1></div>", unsafe_allow_html=True)
    
    _, col_f, _ = st.columns([1, 1.5, 1])
    with col_f:
        with st.form("login"):
            ced = st.text_input("Ingresa tu Cédula para comenzar:")
            if st.form_submit_button("Entrar a la Ruta de Aprendizaje"):
                if ced.isdigit() and len(ced) >= 5:
                    st.session_state['cedula'] = ced
                    st.rerun()
else:
    # --- INTERFAZ DE APRENDIZAJE ---
    st.sidebar.image("logo.png" if os.path.exists("logo.png") else "logo.png.png", width=100)
    modulo = st.sidebar.radio("📍 Tu Mapa de Ruta:", [
        "Módulo 1: Equipo de Canastas Aptas", "📝 Examen Módulo 1",
        "Módulo 2: Canastas No Aptas", "📝 Examen Módulo 2",
        "Módulo 3: Lavado y Desinfección", "📝 Examen Módulo 3"
    ])
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- CONTENIDO DINÁMICO MÓDULO 1 ---
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 style='color: #008a3e;'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["🕒 Historia y Cobertura", "📐 Partes y Medidas", "🔄 Sistemas de Uso", "🚛 Cargue y Autoventa"])
        
        with tab1:
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("<div class='card'><h3>Nuestra Cobertura</h3></div>", unsafe_allow_html=True)
                mostrar_recurso("mapa.png", "Mapa de Centros de Distribución")
            with col_b:
                st.markdown("<div class='card'><h3>Cronología Ovoid</h3></div>", unsafe_allow_html=True)
                mostrar_recurso("cronologia.png", "Evolución 2019 - 2023")

        with tab2:
            st.markdown("<div class='card'><h3>Conoce tu herramienta de trabajo</h3></div>", unsafe_allow_html=True)
            mostrar_recurso("partes.png", "Las 9 partes de la Canasta")
            mostrar_recurso("dimensiones.png", "Ficha técnica de componentes")

        with tab3:
            st.markdown("<div class='card'><h3>Sistemas de Apilado y Anidado</h3></div>", unsafe_allow_html=True)
            mostrar_recurso("sistemas.png")
            st.video("video_kikes.mp4") if os.path.exists("video_kikes.mp4") else st.warning("📹 Video: Dale sentido a la bandeja (Pendiente subir video_kikes.mp4)")
            
            st.markdown("<div class='card'><h3>¡Cuidado! Usos Indebidos</h3></div>", unsafe_allow_html=True)
            mostrar_recurso("usos.png")

        with tab4:
            st.markdown("<div class='card'><h3>Optimización de Transporte</h3></div>", unsafe_allow_html=True)
            mostrar_recurso("cargue.png")
            st.info("💡 Recuerda: El arrume vacío es de **16 niveles** sobre estiba Ovoid.")

    # --- EVALUACIÓN Y CERTIFICADO ---
    elif "Examen" in modulo:
        st.markdown(f"<h2 style='color: #008a3e;'>📝 {modulo}</h2>", unsafe_allow_html=True)
        with st.form("examen"):
            st.write("Demuestra lo aprendido para obtener tu certificado.")
            p1 = st.radio("¿Cuál es el arrume correcto de canastas vacías?", ["8 niveles", "16 niveles", "20 niveles"])
            p2 = st.radio("Al apilar CON producto, ¿cómo van los identificadores?", ["Mismo costado", "Costado opuesto"])
            
            if st.form_submit_button("Calificar Examen"):
                score = 0
                if p1 == "16 niveles": score += 50
                if p2 == "Costado opuesto": score += 50
                
                if score >= 80:
                    st.success(f"¡Excelente! Calificación: {score}%")
                    st.balloons()
                    # Generación de certificado simple
                    cert_text = f"CERTIFICADO DE APROBACIÓN\n\nEl empleado con cédula {st.session_state['cedula']}\nha aprobado satisfactoriamente el {modulo}.\n\n¡Felicidades!"
                    st.download_button("🎓 Descargar mi Certificado", cert_text, file_name=f"Certificado_{modulo}.txt")
                else:
                    st.error(f"Calificación: {score}%. Necesitas 80% para el certificado. ¡Repasa el módulo!")

    else:
        st.write("Información técnica en construcción...")