import streamlit as st

# Configuración de la interfaz de la página
st.set_page_config(
    page_title="Plataforma de Cadena de Abastecimiento", 
    page_icon="📦", 
    layout="wide"
)

# --- ESTILOS CSS DINÁMICOS Y CREATIVOS CON IDENTIDAD KIKES ---
st.markdown("""
    <style>
        /* Fondo general suave de la aplicación */
        .stApp { background-color: #f7fbf7; }
        
        /* Banner superior de la plataforma */
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
    
    # Intento de cargar el logo en la parte superior central
    col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
    with col_img2:
        try:
            st.image("logo.png", use_container_width=True)
        except Exception:
            st.write(" ")  # Espacio en blanco si el archivo aún no se sube a GitHub
            
    st.markdown("<div class='main-banner'><h1>Plataforma de Cadena de Abastecimiento</h1><p>Módulos de Capacitación Técnica Operativa</p></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<h3 style='text-align: center; color: #333;'>Acceso al Personal</h3>", unsafe_allow_html=True)
        with st.form("login_form"):
            # Etiqueta exacta solicitada
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
    # MÓDULO 1: EQUIPO DE CANASTAS APTAS (Basado en GL-P-02)
    # =========================================================
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.markdown("<h2 class='module-title'>📦 Módulo 1: Control y Uso de Equipo de Canastas Aptas</h2>", unsafe_allow_html=True)
        st.write("Normativas y estándares obligatorios para el manejo adecuado de activos fijos de carga[cite: 2].")
        
        tab1, tab2, tab3 = st.tabs(["📋 Ficha Técnica", "🔄 Apilado y Anidado", "🚛 Armado de Estibas"])
        
        with tab1:
            st.subheader("Especificaciones de los Elementos (Código AFCA022)")
            st.write("El equipo logístico cuenta con pesos específicos que se deben considerar en el cálculo de carga del vehículo[cite: 2]:")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.info("""
                * **Canasta Ovoid:** 1,75 Kg[cite: 2].
                * **Separador Ovoid:** 8,00 Kg[cite: 2].
                """)
            with col_b:
                st.info("""
                * **Estiba Ovoid:** 11,00 Kg[cite: 2].
                * **Gancho Metálico:** 0,10 Kg[cite: 2].
                """)
                
            st.subheader("Capacidad de Carga por Tipo de Huevo")
            st.write("La capacidad volumétrica de unidades por canasta cambia de acuerdo con la clasificación[cite: 2]:")
            st.markdown("""
            * **Tallas A, AA, B, M, L:** 240 unidades sueltas o 180 unidades amarradas[cite: 2].
            * **Talla XL:** 180 unidades sueltas o 120 unidades amarradas[cite: 2].
            * **Talla JUMBO:** 120 unidades sueltas (no cuenta con opción de amarrado)[cite: 2].
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
            st.markdown("""
            1. **Sujeción en Base:** Ubicar un bloque de 4 canastas en el primer nivel de la estiba y asegurarlas en el centro exacto utilizando el **gancho metálico (MDGA105)**[cite: 2].
            2. **Sujeción Superior:** Asegurar firmemente las 4 canastas del último nivel con un segundo gancho metálico idéntico[cite: 2].
            3. **Aplicación de Vinipel:** Instalar el vinipel desde el taco base de la estiba aplicando **dos vueltas completamente tensadas**[cite: 2]. Las vueltas consecutivas (3ª, 4ª y 5ª) se deben aplicar de forma ascendente en **forma de corbatín** para asegurar ventilación al huevo[cite: 2].
            """)

    # =========================================================
    # MÓDULO 2: EQUIPO DE CANASTAS NO APTAS (Basado en GL-P-02 / GL-P-01)
    # =========================================================
    elif modulo == "Módulo 2: Equipo de Canastas No Aptas":
        st.markdown("<h2 class='module-title'>⚠️ Módulo 2: Identificación de No Aptitud y Gestión de Dañados</h2>", unsafe_allow_html=True)
        st.write("Criterios críticos de clasificación biológica, física y procesos de disposición de activos defectuosos[cite: 1, 2].")
        
        col_c, col_d = st.columns(2)
        
        with col_c:
            st.error("### 🚨 Criterios de No Aptitud (Retiro del Flujo)")
            st.write("Una canasta debe segregarse del inventario operativo inmediatamente si presenta uno de estos estados[cite: 1, 2]:")
            st.markdown("""
            * **Residuos de Huevo:** Filtración orgánica de producto pegada o descompuesta en la estructura[cite: 1, 2].
            * **Polvo Crítico:** Suciedad sólida incrustada que requiere de acción mecánica y química forzosa para desprenderse[cite: 1, 2]. *(El polvo medio se considera apto si se retira con facilidad)*[cite: 1, 2].
            * **Presencia de Vectores (Gusanos):** Presencia de contaminación biológica activa en cualquier área de la superficie[cite: 1, 2].
            """)
            
        with col_d:
            st.warning("### 🔧 Definición de Canasta Dañada (AFCA022-DA)")
            st.write("Se consideran definitivamente inutilizables y candidatas a mantenimiento con proveedor externo si tienen rupturas en[cite: 2]:")
            st.markdown("""
            * Las manijas de sujeción lateral o las hendiduras de manipulación[cite: 2].
            * El piso estructural tipo bandeja o los refuerzos de resistencia de la base[cite: 2].
            * La marcación de identificación visual, o el sistema de acople para apilado y anidado[cite: 2].
            """)
            
        st.markdown("---")
        st.subheader("🚫 Prohibiciones Críticas en el Uso de Activos")
        st.write("Para resguardar el ciclo de vida útil del material, queda estrictamente prohibido[cite: 2]:")
        st.markdown("""
        * **NO** utilizar el equipo de canastas como sillas provisionales o escaleras de apoyo dentro de los centros de operación[cite: 2].
        * **NO** destinar las canastas para almacenamiento de chatarra, residuos corporativos, basuras o documentación de oficina[cite: 2].
        * **NO UTILIZAR EL GANCHO PARA ARRASTRAR ARRUMES:** Halar las pilas de canastas con herramientas rígidas afecta la estabilidad de la estructura y causa fracturas directas en el área de la manija[cite: 2].
        """)

    # =========================================================
    # MÓDULO 3: LAVADO Y DESINFECCIÓN (Basado en GL-P-01)
    # =========================================================
    elif modulo == "Módulo 3: Lavado y Desinfección de Canastas":
        st.markdown("<h2 class='module-title'>🧼 Módulo 3: Procedimiento de Higienización Estándar</h2>", unsafe_allow_html=True)
        st.write("Protocolo operativo obligatorio regido bajo la Resolución 2674 de 2013 del Ministerio de Salud[cite: 1].")
        
        st.subheader("1. Dotación de EPP Obligatoria para Lavaderos")
        st.write("Previo a la manipulación de soluciones químicas, el personal asignado debe portar[cite: 1]:")
        st.markdown("""
        * **Protección de cabeza:** Gorro higiénico en tela dacrón de color blanco[cite: 1].
        * **Protección visual:** Monogafas antiempañantes con banda elástica de sujeción ajustable[cite: 1].
        * **Protección dérmica:** Guantes de nitrilo de resistencia química extendida (Referencia Alphatec Solvex 18\")[cite: 1].
        * **Protección corporal:** Delantal plástico impermeable de color amarillo, calibre 25[cite: 1].
        * **Protección de extremidades:** Bota plástica blanca de caña alta equipada con puntera de seguridad[cite: 1].
        """)
        
        st.subheader("2. Proceso Secuencial de Limpieza y Desinfección (L&D)")
        
        col_e, col_f = st.columns(2)
        with col_e:
            st.success("#### 🔹 Fase A: Remoción Mecánica y Lavado")
            st.markdown("""
            1. **Disposición:** Anidar el lote de canastas no aptas conformando columnas estables en bloques de **8 unidades**[cite: 1].
            2. **Preenjuague:** Humedecer los arrumes completos usando hidrolavadora regulada estrictamente a **1700 PSI con boquilla en abanico**[cite: 1]. *(Mantener esta presión evita daños físicos al plástico)*[cite: 1].
            3. **Dosificación Química:** Preparar la solución agregando **30 ml de detergente neutro Biodex** por cada 1000 ml de agua limpia[cite: 1].
            4. **Aplicación:** Esparcir la mezcla homogénea con el espumador mecánico y **permitir un tiempo de acción biológica de 10 minutos**[cite: 1].
            5. **Fricción:** Restregar firmemente la superficie con el **cepillo ultrasuave**, concentrando la fuerza en los bordes internos y la base[cite: 1].
            6. **Aclarado:** Enjuagar de forma individual cada canasta con hidrolavadora a 1700 PSI para remover trazas químicas[cite: 1].
            """)
            
        with col_f:
            st.success("#### 🔹 Fase B: Aplicación de Sanitizante y Secado")
            st.markdown("""
            7. **Dosificación del Desinfectante:** Diluir exactamente **5 ml de bactericida Biosanit** por cada 1000 ml de agua en el fumigador atomizador[cite: 1].
            8. **Aplicación Dirigida:** Atomizar el desinfectante de amplio espectro de manera individualizada cubriendo toda la canasta[cite: 1].
            9. **Restricción Operativa:** ⚠️ **¡PROHIBIDO ENJUAGAR!** El producto Biosanit debe permanecer impregnado sobre la superficie plástica para asegurar el efecto residual protector[cite: 1].
            10. **Ciclo de Secado:** Volver a anidar las unidades limpias en columnas de 8 piezas y situarlas sobre un área limpia durante un tiempo mínimo de **4 horas** antes de su retorno al proceso de cargue[cite: 1].
            """)