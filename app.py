import streamlit as st
import os

# Configuración de la interfaz de la página
st.set_page_config(
    page_title="Plataforma de Cadena de Abastecimiento", 
    page_icon="📦", 
    layout="wide"
)

# --- ESTILOS CSS DINÁMICOS Y CREATIVOS (IDENTIDAD KIKES) ---
st.markdown("""
    <style>
        /* Fondo general de la aplicación */
        .stApp { background-color: #f7fbf7; }
        
        /* Banner superior de la plataforma con degradado verde */
        .main-banner {
            background: linear-gradient(135deg, #008a3e 0%, #2bb673 100%);
            padding: 35px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        /* Cajas de títulos en módulos */
        .module-title {
            color: #008a3e;
            font-family: 'Arial Black', sans-serif;
            border-bottom: 3px solid #008a3e;
            padding-bottom: 5px;
        }
        
        /* Botones personalizados con verde Kikes */
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
    # --- PANTALLA DE INGRESO CREATIVA Y DINÁMICA ---
    
    # Busca de forma automática cualquiera de los dos nombres del archivo detectados
    logo_path = None
    if os.path.exists("logo.png"):
        logo_path = "logo.png"
    elif os.path.exists("logo.png.png"):
        logo_path = "logo.png.png"

    # --- LOGO CON NITIDEZ FORZADA ---
    if logo_path:
        # Columna central estrecha para controlar el tamaño sin perder resolución
        _, col_img2, _ = st.columns([2.5, 1, 2.5])
        with col_img2:
            st.image(logo_path, use_container_width=True)
            
    # Banner principal
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1></div>", unsafe_allow_html=True)
    
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
    
    # =========================================================
    # MÓDULO 1: EQUIPO DE CANASTAS APTAS (GL-P-02)
    # =========================================================
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 class='module-title'>📦 Módulo 1: Control y Uso de Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        st.write("Normativas y estándares obligatorios para el manejo adecuado de activos fijos de carga.")
        
        tab1, tab2, tab3 = st.tabs(["📋 Ficha Técnica", "🔄 Apilado y Anidado", "🚛 Armado de Estibas"])
        
        with tab1:
            st.subheader("Especificaciones de los Elementos (Código AFCA022)")
            st.write("El equipo logístico cuenta con pesos específicos que se deben considerar en el cálculo de carga del vehículo:")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.info("""
                * **Canasta Ovoid:** 1.75 kg.
                * **Separador Ovoid:** 8 kg.
                """)
            with col_b:
                st.info("""
                * **Estiba Ovoid:** 11 kg.
                * **Gancho Metálico:** 0.1 kg.
                """)
                
            st.subheader("Capacidad de Carga por Tipo de Huevo")
            st.write("La capacidad volumétrica de unidades por canasta cambia de acuerdo con la clasificación:")
            st.markdown("""
            * **Tallas A, AA, B, M, L:** 240 unidades sueltas o 180 unidades amarradas.
            * **Talla XL:** 180 unidades sueltas o 120 unidades amarradas.
            * **Talla JUMBO:** 120 unidades sueltas (no cuenta con opción de amarrado).
            """)
            st.write("Dimensiones de referencia para la manipulación: Canasta Kikes (63x32x23 cm), Separadores Ovoid (124 cm x 66 cm) y Estibas Ovoid (124 cm x 66 cm).")
            
        with tab2:
            st.subheader("Criterios de Posicionamiento Correcto")
            st.markdown("""
            * **Apilado de Canastas (Con Producto):** Se debe rectificar minuciosamente que las pestañas de las esquinas superiores de la canasta encajen de forma exacta en las cavidades de la parte inferior de la columna de la canasta siguiente. El identificador de posición debe estar dispuesto siempre en el **costado opuesto** al de la canasta inferior.
            * **Anidado de Canastas (Vacías):** Las columnas de la base inferior deben deslizarse y encajar por completo en los rieles de la parte superior de la canasta continua. Para la optimización de espacio, el identificador de posición de todo el arrume debe encontrarse hacia el **mismo costado**.
            * **Configuración Técnica:** Arrume de 16 niveles por estiba Ovoid.
            """)
            
        with tab3:
            st.subheader("Estiba Sencilla y Remontada")
            st.warning("⚠️ **Sentido Obligatorio de la Bandeja:** En el primer nivel del armado, se tienen que alinear los agujeros inferiores de la canasta con las pestañas laterales de la bandeja de huevo de cartón para evitar incrementos de altura y roturas de producto.")
            st.markdown("""
            1. **Sujeción en Base:** Ubicar un bloque de 4 canastas en el primer nivel de la estiba y asegurarlas en el centro exacto utilizando el **gancho metálico (MDGA105)**.
            2. **Sujeción Superior:** Asegurar firmemente las 4 canastas del último nivel con un segundo gancho metálico idéntico.
            3. **Aplicación de Vinipel:** Instalar el vinipel desde el taco base de la estiba aplicando **dos vueltas completamente tensadas**. Las vueltas consecutivas (3ª, 4ª y 5ª) se deben aplicar de forma ascendente en **forma de corbatín** para asegurar la ventilación del huevo.
            """)

    # =========================================================
    # MÓDULO 2: EQUIPO DE CANASTAS NO APTAS (GL-P-02 / GL-P-01)
    # =========================================================
    elif modulo == "Módulo 2: Equipo de Canastas No Aptas":
        st.markdown("<h2 class='module-title'>⚠️ Módulo 2: Identificación de No Aptitud y Gestión de Dañados</h2>", unsafe_allow_html=True)
        st.write("Criterios críticos de clasificación biológica, física y procesos de disposición de activos defectuosos.")
        
        col_c, col_d = st.columns(2)
        
        with col_c:
            st.error("### 🚨 Criterios de No Aptitud (Retiro del Flujo)")
            st.write("Una canasta debe segregarse del inventario operativo inmediatamente si presenta uno de estos estados:")
            st.markdown("""
            * **Residuos de Huevo:** Filtración orgánica de producto pegada o descompuesta en la estructura.
            * **Polvo Crítico:** Suciedad sólida incrustada que requiere de acción mecánica y química forzosa para desprenderse.
            * **Presencia de Vectores (Gusanos):** Presencia de contaminación biológica activa en cualquier área de la superficie.
            """)
            
        with col_d:
            st.warning("### 🔧 Definición de Canasta Dañada (AFCA022-DA)")
            st.write("Se consideran definitivamente inutilizables y candidatas a mantenimiento con proveedor externo si tienen rupturas en:")
            st.markdown("""
            * Las manijas de sujeción lateral o las hendiduras de manipulación.
            * El piso estructural tipo bandeja o los refuerzos de resistencia de la base.
            * La marcación de identificación visual, o el sistema de acople para apilado y anidado.
            """)
            
        st.markdown("---")
        st.subheader("🚫 Prohibiciones Críticas en el Uso de Activos")
        st.write("Para resguardar el ciclo de vida útil del material, queda estrictamente prohibido:")
        st.markdown("""
        * **NO** utilizar el equipo de canastas como sillas provisionales o escaleras de apoyo dentro de los centros de operación.
        * **NO** destinar las canastas para almacenamiento de chatarra, residuos corporativos, basuras o documentación de oficina.
        * **NO UTILIZAR EL GANCHO PARA ARRASTRAR ARRUMES:** Halar las pilas de canastas con herramientas rígidas afecta la estabilidad de la estructura y causa fracturas directas en el área de la manija.
        """)

    # =========================================================
    # MÓDULO 3: LAVADO Y DESINFECCIÓN (GL-P-01)
    # =========================================================
    elif modulo == "Módulo 3: Lavado y Desinfección de Canastas":
        st.markdown("<h2 class='module-title'>🧼 Módulo 3: Procedimiento de Higienización Estándar</h2>", unsafe_allow_html=True)
        st.write("Protocolo operativo obligatorio regido bajo la Resolución 2674 de 2013 del Ministerio de Salud.")
        
        st.subheader("1. Dotación de EPP Obligatoria para Lavaderos")
        st.write("Previo a la manipulación de soluciones químicas, el personal asignado debe portar:")
        st.markdown("""
        * **Protección de cabeza:** Gorro higiénico en tela dacrón de color blanco.
        * **Protección visual:** Monogafas antiempañantes con banda elástica de sujeción ajustable.
        * **Protección dérmica:** Guantes de nitrilo de resistencia química extendida (Referencia Alphatec Solvex 18\").
        * **Protección corporal:** Delantal plástico impermeable de color amarillo, calibre 25.
        * **Protección de extremidades:** Bota plástica blanca de caña alta equipada con puntera de seguridad.
        """)
        
        st.subheader("2. Proceso Secuencial de Limpieza y Desinfección (L&D)")
        
        col_e, col_f = st.columns(2)
        with col_e:
            st.success("#### 🔹 Fase A: Remoción Mecánica y Lavado")
            st.markdown("""
            1. **Disposición:** Anidar el lote de canastas no aptas conformando columnas estables en bloques de **8 unidades**.
            2. **Preenjuague:** Humedecer los arrumes completos usando hidrolavadora regulada estrictamente a **1700 PSI con boquilla en abanico**.
            3. **Dosificación Química:** Preparar la solución agregando **30 ml de detergente neutro Biodex** por cada 1000 ml de agua limpia.
            4. **Aplicación:** Esparcir la mezcla homogénea con el espumador mecánico y **permitir un tiempo de acción de 10 minutos**.
            5. **Fricción:** Restregar firmemente la superficie con el **cepillo ultrasuave**, concentrando la fuerza en los bordes internos y la base.
            6. **Aclarado:** Enjuagar de forma individual cada canasta con hidrolavadora a 1700 PSI para remover trazas químicas.
            """)
            
        with col_f:
            st.success("#### 🔹 Fase B: Aplicación de Sanitizante y Secado")
            st.markdown("""
            7. **Dosificación del Desinfectante:** Diluir exactamente **5 ml de bactericida Biosanit** por cada 1000 ml de agua en el fumigador atomizador.
            8. **Aplicación Dirigida:** Atomizar el desinfectante de amplio espectro de manera individualizada cubriendo toda la canasta.
            9. **Restricción Operativa:** ⚠️ **¡PROHIBIDO ENJUAGAR!** El producto Biosanit debe permanecer impregnado sobre la superficie plástica para asegurar el efecto residual protector.
            10. **Ciclo de Secado:** Volver a anidar las unidades limpias en columnas de 8 piezas y situarlas sobre un área limpia durante un tiempo mínimo de **4 horas** antes de su retorno al proceso de cargue.
            """)