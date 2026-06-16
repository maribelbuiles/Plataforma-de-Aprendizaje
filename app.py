import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Plataforma de Aprendizaje - Gestión de Canastas", 
    page_icon="🎓", 
    layout="wide"
)

# --- SISTEMA DE INGRESO POR CÉDULA (SESSIÓN STATE) ---
if 'cedula' not in st.session_state:
    st.session_state['cedula'] = None

if st.session_state['cedula'] is None:
    # Pantalla de Login
    st.markdown("<h1 style='text-align: center;'>🎓 Plataforma de Aprendizaje</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>Incubadora Santander S.A.</h3>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("Ingreso al Sistema")
        with st.form("login_form"):
            cedula_input = st.text_input("Número de Cédula del Operario:", placeholder="Ej: 1098680700")
            boton_ingresar = st.form_submit_button("Ingresar a la Capacitación")
            
            if boton_ingresar:
                if cedula_input.strip().isdigit() and len(cedula_input.strip()) >= 6:
                    st.session_state['cedula'] = cedula_input.strip()
                    st.rerun()
                else:
                    st.error("Por favor, ingrese un número de cédula válido (solo números, mínimo 6 dígitos).")
else:
    # --- MENÚ LATERAL Y NAVEGACIÓN ---
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.sidebar.title(f"👤 Operario: {st.session_state['cedula']}")
    
    st.sidebar.write("---")
    st.sidebar.header("Módulos del Curso")
    modulo = st.sidebar.radio(
        "Seleccione el tema a estudiar:",
        [
            "Módulo 1: Equipo de Canastas Aptas",
            "Módulo 2: Equipo de Canastas No Aptas y Dañadas",
            "Módulo 3: Lavado y Desinfección de Canastas",
            "📝 Evaluación Final"
        ]
    )
    
    if st.sidebar.button("Cerrar Sesión ❌"):
        st.session_state['cedula'] = None
        st.rerun()

    # --- CONTENIDO DE LOS MÓDULOS ---
    
    # ==========================================
    # MÓDULO 1: EQUIPO DE CANASTAS APTAS
    # ==========================================
    if modulo == "Módulo 1: Equipo de Canastas Aptas":
        st.title("📦 Módulo 1: Control y Uso de Equipo de Canastas Aptas")
        st.write("Basado en la normativa vigente y el procedimiento **GL-P-02**.")
        st.write("---")
        
        st.header("1. Criterios de una Canasta Apta")
        st.write("Una canasta se considera **Apta** para la operación logística si cumple las siguientes condiciones:")
        st.info("🔹 **Polvo medio:** Material particulado que no está fijado a la superficie y es fácil de eliminar.\n\n🔹 **Lavadas:** Canastas limpias listas para el cargue seguro de bandejas.")
        
        st.header("2. Ficha Técnica y Usabilidad")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Especificaciones de la Canasta Kikes (AFCA022)")
            st.markdown("""
            * **Dimensiones:** $63 \\times 32 \\times 23$ cm.
            * **Peso vacío:** 1,75 Kg.
            * **Diseño:** Piso tipo bandeja para optimización de espacio y hendiduras de fácil manipulación.
            """)
        with col2:
            st.subheader("Capacidad de Huevos por Canasta (Tallas)")
            st.markdown("""
            * **Tallas A, AA, B, M, L:** 240 unidades sueltas o 180 amarradas.
            * **Talla XL:** 180 unidades sueltas o 120 amarradas.
            * **Talla JUMBO:** 120 unidades sueltas (No aplica amarrado).
            """)

        st.header("3. Procedimiento Correcto de Apilado y Anidado")
        st.markdown("""
        * **Apilado Adecuado (Con Producto):** Rectificar que las pestañas superiores de las esquinas encajen exactamente en las cavidades inferiores de la canasta siguiente. El identificador de posición debe ir al **costado opuesto**.
        * **Anidado Adecuado (Vacías):** Las columnas inferiores deben encajar en los rieles superiores de la canasta de abajo. El identificador de posición debe quedar al **mismo costado** para optimizar espacio (en arrumes de 6 o 16 niveles según transporte).
        """)
        
        st.header("4. Armado de Estiba y Uso de Vinipel")
        st.warning("⚠️ **Sentido de la bandeja:** En el primer nivel, se deben alinear los agujeros inferiores de la canasta con las pestañas de la bandeja de cartón para evitar roturas.")
        st.markdown("""
        1. Colocar una base de **4 canastas** en la estiba unidas en el medio con un gancho metálico (MDGA105).
        2. Asegurar el último nivel con un segundo gancho metálico.
        3. **Aplicación de Vinipel:** Dar **dos vueltas tensadas** desde el taco de la estiba. Posteriormente, aplicar de forma ascendente la tercera, cuarta y quinta vuelta en **forma de corbatín** para permitir la ventilación del producto.
        """)

    # ==========================================
    # MÓDULO 2: EQUIPO DE CANASTAS NO APTAS
    # ==========================================
    elif modulo == "Módulo 2: Equipo de Canastas No Aptas y Dañadas":
        st.title("⚠️ Módulo 2: Criterios de No Aptitud y Gestión de Equipos Dañados")
        st.write("Instrucciones críticas para evitar daños estructurales y contaminación microbiológica.")
        st.write("---")
        
        st.header("1. Clasificación del Estado No Apto")
        st.error("🚨 **Una canasta se cataloga como NO APTA de inmediato si presenta:**\n\n1. **Residuos de huevo:** Filtraciones o suciedad orgánica pegada.\n2. **Polvo crítico:** Suciedad incrustada que requiere de acción mecánica o química para desprenderse.\n3. **Gusanos o plagas:** Presencia de vectores biológicos.")
        
        st.header("2. Definición de Canastas Dañadas (AFCA022-DA)")
        st.write("Son aquellas que pierden su integridad física. Debes retirarlas de la operación si tienen partidas:")
        st.markdown("""
        * Las manijas o hendiduras de manipulación.
        * El piso de la canasta o los refuerzos de estructura.
        * La identificación visual o el sistema de apilado/anidado.
        """)
        
        st.header("3. ❌ Usos Indebidos Estrictamente Prohibidos")
        st.markdown("""
        * **NO** usar las canastas como silla o escalera de apoyo.
        * **NO** utilizarlas para almacenar papelería o documentación de oficina.
        * **NO** usarlas como depósitos de basura, residuos o chatarra.
        * **NO USAR EL GANCHO PARA ARRASTRAR EL ARRUME:** El uso de ganchos para jalar genera fracturas estructurales fatales en la zona de las manijas.
        """)

        st.header("4. Flujo de Disposición de Dañados")
        st.markdown("""
        1. El auxiliar de despachos identifica y clasifica las cantidades de equipos dañados.
        2. Se diligencia el formulario oficial de registro en Google de la compañía.
        3. Planeación coordina con el proveedor (**Mercico**) para enviar desde las Plantas el lote dañado para su respectiva reposición bajo Orden de Trabajo (OT).
        """)

    # ==========================================
    # MÓDULO 3: LAVADO Y DESINFECCIÓN
    # ==========================================
    elif modulo == "Módulo 3: Lavado y Desinfección de Canastas":
        st.title("🧼 Módulo 3: Procedimiento Operativo de Limpieza y Desinfección")
        st.write("Establecido bajo el código **GL-P-01** en concordancia con la Resolución 2674 de 2013 del Ministerio de Salud.")
        st.write("---")
        
        st.header("1. Elementos de Protección Personal (EPP) Obligatorios")
        st.write("Antes de iniciar las actividades en el lavadero, es obligatorio el uso de:")
        st.markdown("""
        * **Gorro:** Tela dacrón blanca.
        * **Monogafas:** Antiempañantes con banda elástica ajustable.
        * **Guantes:** De nitrilo de caña alta (Alphatec Solvex 18\").
        * **Delantal:** Plástico amarillo calibre 25.
        * **Botas:** Plásticas blancas caña alta con puntera de seguridad.
        """)
        
        st.header("2. Paso a Paso del Proceso L&D")
        
        st.subheader("Fase A: Preparación y Lavado Químico")
        st.markdown("""
        1. **Anidamiento:** Organizar las canastas no aptas en columnas anidadas de **8 unidades**.
        2. **Humedecimiento:** Mojar el arrume utilizando una hidrolavadora configurada estrictamente a **1700 PSI con chorro en abanico** (evita romper el plástico).
        3. **Dosificación del Detergente:** Diluir **30 ml de Biodex** (detergente neutro, biodegradable sin fragancia) por cada **1000 ml de agua**.
        4. **Aplicación:** Usar el espumador manual acoplado y **dejar actuar la espuma por un lapso de 10 minutos**.
        5. **Acción Mecánica:** Restregar enérgicamente cada canasta con el **cepillo ultrasuave**, enfatizando en los bordes y en la base inferior.
        6. **Enjuague:** Retirar por completo el jabón con la hidrolavadora a 1700 PSI en abanico sin dejar residuos.
        """)
        
        st.subheader("Fase B: Desinfección y Secado")
        st.markdown("""
        7. **Dosificación del Desinfectante:** Diluir **5 ml de Biosanit** (bactericida, virucida y fungicida de amplio espectro) por cada **1000 ml de agua** dentro del fumigador atomizador.
        8. **Aplicación:** Atomizar de forma individual cada canasta. ⚠️ **¡NO SE DEBE ENJUAGAR EL DESINFECTANTE!**
        9. **Secado Óptimo:** Volver a anidar las canastas en columnas de 8 unidades y dejarlas secar sobre una superficie limpia durante **4 horas** como mínimo antes de usarlas de nuevo.
        """)

    # ==========================================
    # EVALUACIÓN DE CONOCIMIENTOS
    # ==========================================
    elif modulo == "📝 Evaluación Final":
        st.title("📝 Evaluación de Validación de Conocimientos")
        st.write("Responde las siguientes preguntas para completar tu registro de capacitación.")
        st.write("---")
        
        q1 = st.radio(
            "1. ¿Cuál es la dosificación correcta para la solución de lavado con detergente Biodex?",
            ["5 ml por cada 1000 ml de agua", "30 ml por cada 1000 ml de agua", "50 ml por cada 500 ml de agua"]
        )
        
        q2 = st.radio(
            "2. ¿Cuál es la presión correcta y tipo de chorro que debe configurarse en la hidrolavadora para no dañar las canastas?",
            ["1200 PSI con chorro directo", "2500 PSI con chorro de aguja", "1700 PSI con chorro en abanico"]
        )
        
        q3 = st.radio(
            "3. ¿Cuál de las siguientes acciones representa un USO INDEBIDO prohibido por el procedimiento GL-P-02?",
            ["Almacenar bandejas alineadas según la pestaña", "Usar el gancho metálico para arrastrar o halar los arrumes", "Anidar las canastas limpias en columnas de 8 unidades"]
        )
        
        q4 = st.radio(
            "4. Una vez aplicado el desinfectante Biosanit en la canasta, ¿qué acción sigue?",
            ["Enjuagar de inmediato con agua limpia", "Restregar con el cepillo ultrasuave", "No enjuagar y dejar secar en arrumes de 8 por 4 horas"]
        )
        
        if st.button("Enviar Respuestas ✔️"):
            aciertos = 0
            if q1 == "30 ml por cada 1000 ml de agua": aciertos += 1
            if q2 == "1700 PSI con chorro en abanico": aciertos += 1
            if q3 == "Usar el gancho metálico para arrastrar o halar los arrumes": aciertos += 1
            if q4 == "No enjuagar y dejar secar en arrumes de 8 por 4 horas": aciertos += 1
            
            if aciertos == 4:
                st.success(f"🎉 ¡Excelente! Operario con Cédula {st.session_state['cedula']} ha aprobado la capacitación con 4/4 aciertos.")
                st.balloons()
            else:
                st.error(f"Has obtenido {aciertos} de 4 aciertos. Te recomendamos repasar los módulos y volver a intentarlo.")