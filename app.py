import streamlit as st
import os

# Configuración Base
st.set_page_config(page_title="Plataforma Kikes", page_icon="📦", layout="wide")

# Estilos de Identidad Visual (Verde Kikes)
st.markdown("""
    <style>
        .stApp { background-color: #f7fbf7; }
        .main-banner { background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%); padding: 30px; border-radius: 15px; color: white; text-align: center; margin-bottom: 25px; }
        .module-title { color: #008a3e; font-family: 'Arial Black'; border-bottom: 3px solid #008a3e; }
        .stButton>button { width: 100%; border-radius: 30px; background-color: #008a3e; color: white; font-weight: bold; }
        .info-box { background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #008a3e; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# Lógica de Acceso
if 'cedula' not in st.session_state: st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    logo_path = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)
    if logo_path:
        _, col_img, _ = st.columns([2.5, 1, 2.5])
        with col_img: st.image(logo_path, use_container_width=True)
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1></div>", unsafe_allow_html=True)
    _, col_form, _ = st.columns([1, 1.8, 1])
    with col_form:
        with st.form("login"):
            cedula = st.text_input("Número de Cédula del Empleado:")
            if st.form_submit_button("Ingresar al Sistema"):
                if cedula.isdigit() and len(cedula) >= 5:
                    st.session_state['cedula'] = cedula
                    st.rerun()
                else: st.error("Cédula no válida.")
else:
    # Menú Lateral
    modulo = st.sidebar.radio("🗺️ Mapa de Ruta Pro", [
        "Módulo 1: Equipo de Canastas Aptas", "📝 Evaluación Módulo 1",
        "Módulo 2: Equipo de Canastas No Aptas", "📝 Evaluación Módulo 2",
        "Módulo 3: Lavado y Desinfección", "📝 Evaluación Módulo 3"
    ])
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.rerun()

    # CONTENIDO MÓDULO 1 (Información idéntica al adjunto)
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 class='module-title'>📦 Módulo 1: Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        
        t1, t2, t3, t4, t5 = st.tabs(["🕒 Origen y Partes", "📏 Ficha Técnica", "🔄 Sistemas Ovoid", "🚛 Uso con Producto", "🚫 Almacenamiento y Usos"])

        with t1:
            st.subheader("Cronología de la Canasta Ovoid")
            st.write("2019: Diseño | 2020: Piloto | 2021: Primera Implementación (B/quilla) | 2023: Operación Total")
            st.markdown("---")
            st.subheader("9 Partes de la Canasta Ovoid")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("1. **Piso Tipo Bandeja:** Distribución de carga.\n2. **Hendiduras:** Agarre cómodo.\n3. **Resistencia:** Refuerzos estructurales.\n4. **Sistema Apilado/Anidado:** Diseño inteligente.\n5. **Identificador de Posición:** Ubicación correcta.")
            with c2:
                st.markdown("6. **Resistencia Estructura:** Protege el huevo.\n7. **Marcación Personalizada:** Identidad visual.\n8. **Manija Anidado:** Facilidad de transporte.\n9. **Identidad Visual:** Reconocimiento instantáneo.")

        with t2:
            st.subheader("Componentes y Dimensiones Exactas")
            col1, col2, col3, col4 = st.columns(4)
            with col1: st.metric("Canasta Kikes", "AFCA022"); st.caption("63 x 32 x 23 cm")
            with col2: st.metric("Estiba Ovoid", "AFES013"); st.caption("124 x 65 x 10.5 cm")
            with col3: st.metric("Gancho Metálico", "MDGA105"); st.caption("8 x 8.6 x 3 cm")
            with col4: st.metric("Separador Ovoid", "AFSE003"); st.caption("124 x 66 x 2 cm")

        with t3:
            st.subheader("Sistemas Canasta Ovoid")
            st.success("**Apilar (Con Producto):** Identificador de posición en **SENTIDO OPUESTO**.")
            st.info("**Anidar (Vacía):** Identificador de posición al **MISMO COSTADO**.")
            st.markdown("---")
            st.write("**Pasos para Apilar:** 1. Identifica sistema | 2. Visualiza identificador | 3. Ajusta en sentido opuesto.")

        with t4:
            st.subheader("Uso con Producto (Cedi, CE y Plantas)")
            st.warning("⚠️ **Carga Máxima:** 17.25 kg | **Cantidad Máxima:** 240 huevos (8 bandejas x 30 unds).")
            
            st.write("**Número de huevos por canasta:**")
            st.table({"Tipo de huevo": ["A-AA-B-M-L", "XL", "JUMBO"], "Suelto": [240, 180, 120], "Amarrado": [180, 120, "N/A"]})
            
            st.write("**Configuraciones de Entrega:**")
            st.markdown("- **Sencilla Nivel 6:** 24 canastas + 2 ganchos + 1 estiba.\n- **Remontada Nivel 9:** 36 canastas + 4 ganchos + 2 estibas + 1 separador.\n- **Remontada Nivel 11:** 44 canastas + 4 ganchos + 2 estibas + 1 separador.")
            
            st.write("**Cargue Autoventa:**")
            st.table({"Vehículo": ["Minitruck TM", "Dongfeng", "Motocarro Ayco/Vaisand"], "Cantidad": [75, 100, 48], "Apilado": ["3 niv x 25", "4 niv x 25", "4 niv x 12"]})

        with t5:
            st.subheader("Almacenamiento y Transporte (Vacío)")
            st.info("✅ **Anidar 16 niveles de canastas por estiba Ovoid.**")
            st.write("- **Estibas:** 11 niveles.\n- **Separadores:** 24 niveles.\n- **Ganchos:** 30 por paquete.")
            st.markdown("---")
            st.error("🚫 **Usos Indebidos:** NO usar como silla/escalera | NO exhibir otros productos | NO guardar basura | NO arrastrar con gancho.")

    # SISTEMA DE EVALUACIÓN Y CERTIFICADO
    elif "Evaluación" in modulo:
        st.markdown(f"<h2 class='module-title'>{modulo}</h2>", unsafe_allow_html=True)
        with st.form("quiz"):
            st.write("Aprobar con 80% para obtener certificado.")
            p1 = st.radio("¿Sentido del identificador al apilar con producto?", ["Mismo costado", "Sentido opuesto"])
            p2 = st.radio("¿Cuántos niveles de canastas vacías se anidan por estiba?", ["8", "16", "24"])
            p3 = st.radio("¿Peso máximo de una canasta con producto?", ["15 kg", "17.25 kg", "20 kg"])
            if st.form_submit_button("Evaluar"):
                score = 0
                if p1 == "Sentido opuesto": score += 34
                if p2 == "16": score += 33
                if p3 == "17.25 kg": score += 33
                if score >= 80:
                    st.success(f"¡APROBADO! {score}%"); st.balloons()
                    st.download_button("📜 Descargar Certificado", f"Certificado de Aprobación\nEmpleado: {st.session_state['cedula']}\nMódulo: {modulo}", f"Certificado_{st.session_state['cedula']}.txt")
                else: st.error(f"Puntaje: {score}%. Requieres 80%.")
    else:
        st.write("Módulo informativo.")