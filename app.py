import streamlit as st
import os

# Configuración de la interfaz de la página
st.set_page_config(
    page_title="Plataforma de Cadena de Abastecimiento", 
    page_icon="📦", 
    layout="wide"
)

# --- ESTILOS CSS DINÁMICOS Y CREATIVOS CON IDENTIDAD KIKES ---
st.markdown("""
    <style>
        .stApp { background-color: #f7fbf7; }
        .main-banner {
            background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%);
            padding: 35px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .module-title {
            color: #008a3e;
            font-family: 'Arial Black', sans-serif;
            border-bottom: 3px solid #008a3e;
            padding-bottom: 5px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 30px;
            height: 3.2em;
            background-color: #008a3e;
            color: white;
            font-weight: bold;
            font-size: 16px;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-color: #006a2e;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTROL DEL ESTADO DE SESIÓN (INGRESO POR CÉDULA) ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    # --- PANTALLA DE INGRESO ---
    col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
    with col_img2:
        # DETECTOR AUTOMÁTICO DE LOGO
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        else:
            st.error("⚠️ No se encuentra el archivo 'logo.png' en la raíz de GitHub.")
            st.markdown("**Archivos detectados actualmente en tu repositorio:**")
            # Esto te listará los archivos reales para ver si se subió mal el nombre
            for archivo in os.listdir("."):
                if not archivo.startswith("."):
                    st.code(archivo)
            
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1><p>Módulos de Capacitación Técnica Operativa</p></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<h3 style='text-align: center; color: #333;'>Acceso al Personal</h3>", unsafe_allow_html=True)
        with st.form("login_form"):
            cedula_input = st.text_input("Número de Cédula del Empleado:")
            submit = st.form_submit_button("Ingresar al Sistema")
            
            if submit:
                if cedula_input.strip().isdigit() and len(cedula_input.strip()) >= 5:
                    st.session_state['cedula'] = cedula_input.strip()
                    st.rerun()
                else:
                    st.error("Por favor, ingrese un número de cédula válido (solo dígitos numéricos).")
else:
    # --- INTERFAZ INTERNA (MENÚ LATERAL) ---
    st.sidebar.markdown(f"### 👤 Empleado: `{st.session_state['cedula']}`")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🗺️ Mapa de Ruta Pro")
    
    modulo = st.sidebar.radio(
        "Seleccione el Módulo de Aprendizaje:",
        [
            "Módulo 1: Equipo de Canastas Aptas", 
            "Módulo 2: Equipo de Canastas No Aptas", 
            "Módulo 3: Lavado y Desinfección de Canastas"
        ]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- DESARROLLO DE CONTENIDO TÉCNICO ---
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 class='module-title'>📦 Módulo 1: Control y Uso de Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        st.write("Normativas y estándares obligatorios para el manejo adecuado de activos fijos de carga[cite: 2].")
        
        tab1, tab2, tab3 = st.tabs(["📋 Ficha Técnica", "🔄 Apilado y Anidado", "🚛 Armado de Estibas"])
        with tab1:
            st.subheader("Especificaciones de los Elements (Código AFCA022)")
            st.write("El equipo logístico cuenta con pesos específicos que se deben considerar en el cálculo de carga del vehículo[cite: 2]:")
            st.info("""
            * **Canasta Ovoid:** 1,75 Kg[cite: 2].
            * **Separador Ovoid:** 8,00 Kg[cite: 2].
            * **Estiba Ovoid:** 11,00 Kg[cite: 2].
            * **Gancho Metálico:** 0,10 Kg[cite: 2].
            """)
        with tab2:
            st.subheader("Criterios de Posicionamiento Correcto")
            st.markdown("""
            * **Apilado de Canastas (Con Producto):** Se debe rectificar minuciosamente que las pestañas de las esquinas superiores de la canasta encajen de forma exacta en las cavidades de la parte inferior de la columna de la canasta siguiente[cite: 2]. El identificador de posición debe estar dispuesto siempre en el **costado opuesto** al de la canasta inferior[cite: 2].
            * **Anidado de Canastas (Vacías):** Las columnas de la base inferior deben deslizarse y encajar por completo en los rieles de la parte superior de la canasta continua[cite: 2]. Para la optimización de espacio, el identificador de posición de todo el arrume debe encontrarse hacia el **mismo costado**[cite: 2].
            """)
        with tab3:
            st.subheader("Estiba Sencilla y Remontada")
            st.warning("⚠️ **Sentido Obligatorio de la Bandeja:** En el primer nivel del armado, se tienen que alinear los agujeros inferiores de la canasta con las pestañas laterales de la bandeja de huevo de cartón para evitar incrementos de altura y roturas de producto[cite: 2].")

    elif modulo == "Módulo 2: Equipo de Canastas No Aptas":
        st.markdown("<h2 class='module-title'>⚠️ Módulo 2: Identificación de No Aptitud y Gestión de Dañados</h2>", unsafe_allow_html=True)
        st.write("Criterios críticos de clasificación biológica, física y procesos de disposición de activos defectuosos[cite: 1, 2].")
        st.error("### 🚨 Criterios de No Aptitud (Retiro del Flujo)")
        st.markdown("""
        * **Residuos de Huevo:** Filtración orgánica de producto pegada o descompuesta en la estructura[cite: 1, 2].
        * **Polvo Crítico:** Suciedad sólida incrustada que requiere de acción mecánica y química forzosa para desprenderse[cite: 1, 2].
        * **Presencia de Vectores (Gusanos):** Presencia de contaminación biológica activa en cualquier área de la superficie[cite: 1, 2].
        """)

    elif modulo == "Módulo 3: Lavado y Desinfección de Canastas":
        st.markdown("<h2 class='module-title'>🧼 Módulo 3: Procedimiento de Higienización Estándar</h2>", unsafe_allow_html=True)
        st.write("Protocolo operativo obligatorio regido bajo la Resolución 2674 de 2013 del Ministerio de Salud[cite: 1].")
        st.subheader("Proceso Secuencial de Limpieza y Desinfección (L&D)")
        st.success("""
        1. **Disposición:** Anidar las canastas no aptas en bloques de **8 unidades**[cite: 1].
        2. **Preenjuague:** Hidrolavadora regulada a **1700 PSI con boquilla en abanico**[cite: 1].
        3. **Detergente:** **30 ml de detergente neutro Biodex** por cada 1000 ml de agua[cite: 1]. Dejar actuar por 10 minutos[cite: 1].
        4. **Desinfectante:** **5 ml de bactericida Biosanit** por cada 1000 ml de agua[cite: 1]. ¡PROHIBIDO ENJUAGAR EL BIOSANIT![cite: 1]
        5. **Secado:** Dejar secar en arrumes de 8 unidades por un tiempo mínimo de **4 horas**[cite: 1].
        """)