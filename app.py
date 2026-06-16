import streamlit as st

# ==================================================
# CONFIGURACIÓN
# ==================================================
st.set_page_config(
    page_title="Academia de Canastas",
    page_icon="🥚",
    layout="wide"
)

# ==================================================
# ESTILOS
# ==================================================
st.markdown("""
<style>

.main {
    background-color: #f8f9fa;
}

.titulo{
    text-align:center;
    color:#2E7D32;
    font-size:38px;
    font-weight:bold;
}

.subtitulo{
    color:#1B5E20;
    font-size:26px;
    font-weight:bold;
}

.tarjeta{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.15);
    margin-bottom:15px;
}

.evaluacion{
    background:#FFF3CD;
    padding:15px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# CABECERA
# ==================================================
st.markdown(
    '<p class="titulo">🥚 Plataforma de Formación Equipo de Canastas</p>',
    unsafe_allow_html=True
)

st.write("")

# ==================================================
# MENU
# ==================================================
modulo = st.sidebar.radio(
    "Seleccione un módulo",
    [
        "🏆 Equipo de Canastas Aptas",
        "⚠️ Equipo de Canastas No Aptas",
        "🧼 Lavado y Desinfección"
    ]
)

# ==================================================
# MODULO 1
# ==================================================
if modulo == "🏆 Equipo de Canastas Aptas":

    st.markdown(
        '<p class="subtitulo">Equipo de Canastas Aptas</p>',
        unsafe_allow_html=True
    )

    temas = [
        "Partes de la Canasta",
        "Partes del Separador",
        "Partes de la Estiba",
        "Partes del Gancho",
        "Apilado Correcto",
        "Anidado Correcto",
        "Capacidad por Tipo de Huevo",
        "Sentido de la Bandeja",
        "Armado de Estiba",
        "Almacenamiento",
        "Transporte"
    ]

    tema = st.selectbox("Seleccione un tema", temas)

    if tema == "Partes de la Canasta":
        st.info("""
        • Manijas

        • Hendiduras

        • Piso ventilado

        • Refuerzos estructurales

        • Sistema de anidado

        • Sistema de apilado

        • Identificador de posición
        """)

    elif tema == "Apilado Correcto":
        st.success("""
        Las pestañas superiores deben encajar en las cavidades de la siguiente canasta.

        El identificador debe quedar en el costado opuesto.
        """)

    elif tema == "Anidado Correcto":
        st.success("""
        Las columnas inferiores deben encajar en los rieles.

        El identificador debe quedar en el mismo costado.
        """)

    elif tema == "Capacidad por Tipo de Huevo":

        st.table({
            "Tipo Huevo":
                ["A-AA-B-M-L", "XL", "JUMBO"],
            "Cantidad":
                [240, 180, 120]
        })

    elif tema == "Armado de Estiba":
        st.write("""
        1. Colocar 4 canastas base.

        2. Instalar gancho inferior.

        3. Apilar niveles.

        4. Instalar gancho superior.

        5. Aplicar vinipel.
        """)

    st.markdown("---")

    st.markdown(
        '<div class="evaluacion"><b>Evaluación</b></div>',
        unsafe_allow_html=True
    )

    p1 = st.radio(
        "En el apilado el identificador debe quedar:",
        [
            "Mismo lado",
            "Lado opuesto"
        ]
    )

    if st.button("Calificar Módulo 1"):

        if p1 == "Lado opuesto":
            st.success("Aprobado")
        else:
            st.error("Respuesta incorrecta")

# ==================================================
# MODULO 2
# ==================================================
elif modulo == "⚠️ Equipo de Canastas No Aptas":

    st.markdown(
        '<p class="subtitulo">Equipo de Canastas No Aptas</p>',
        unsafe_allow_html=True
    )

    st.warning("""
    Una canasta NO apta presenta:

    • Manijas rotas

    • Piso fracturado

    • Hendiduras dañadas

    • Sistema de apilado roto

    • Sistema de anidado roto

    • Refuerzos fracturados

    • Identificador dañado
    """)

    st.markdown("### Proceso")

    st.write("""
    1. Identificar daño.

    2. Clasificar tipo de daño.

    3. Contabilizar unidades.

    4. Registrar formulario.

    5. Coordinar envío.

    6. Gestionar reparación.
    """)

    st.markdown("---")

    st.markdown(
        '<div class="evaluacion"><b>Evaluación</b></div>',
        unsafe_allow_html=True
    )

    p2 = st.radio(
        "¿Una canasta con manija rota es apta?",
        ["Sí", "No"]
    )

    if st.button("Calificar Módulo 2"):

        if p2 == "No":
            st.success("Aprobado")
        else:
            st.error("Respuesta incorrecta")

# ==================================================
# MODULO 3
# ==================================================
elif modulo == "🧼 Lavado y Desinfección":

    st.markdown(
        '<p class="subtitulo">Lavado y Desinfección</p>',
        unsafe_allow_html=True
    )

    tabs = st.tabs([
        "EPP",
        "Productos",
        "Proceso",
        "Secado",
        "Evaluación"
    ])

    with tabs[0]:

        st.write("""
        EPP Obligatorios:

        • Gorro

        • Monogafas

        • Guantes nitrilo

        • Delantal

        • Botas
        """)

    with tabs[1]:

        st.success("""
        DETERGENTE

        Biodex

        30 ml por cada 1000 ml de agua
        """)

        st.info("""
        DESINFECTANTE

        Biosanit

        5 ml por cada 1000 ml de agua
        """)

    with tabs[2]:

        st.write("""
        1. Clasificar canastas

        2. Humedecer

        3. Aplicar detergente

        4. Esperar 10 minutos

        5. Refregar

        6. Enjuagar

        7. Aplicar desinfectante

        8. No enjuagar
        """)

    with tabs[3]:

        st.warning("""
        Tiempo mínimo de secado:

        4 horas
        """)

    with tabs[4]:

        p3 = st.radio(
            "¿Cuántos ml de Biodex se agregan por 1000 ml de agua?",
            [
                "5 ml",
                "30 ml",
                "100 ml"
            ]
        )

        if st.button("Calificar Módulo 3"):

            if p3 == "30 ml":
                st.success("Aprobado")
            else:
                st.error("Respuesta incorrecta")

# ==================================================
# PIE
# ==================================================
st.markdown("---")
st.caption("Academia de Canastas - Gestión Logística")