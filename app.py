import streamlit as st

# ==================================================
# CONFIGURACIÓN GENERAL
# ==================================================
st.set_page_config(
    page_title="Plataforma de Cadena de Abastecimiento",
    page_icon="🚛",
    layout="wide"
)

# ==================================================
# ESTILOS
# ==================================================
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

.titulo{
    text-align:center;
    color:#1B5E20;
    font-size:40px;
    font-weight:bold;
}

.subtitulo{
    color:#2E7D32;
    font-size:28px;
    font-weight:bold;
}

.card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 6px rgba(0,0,0,0.15);
    margin-bottom:15px;
}

.resaltado{
    background:#E8F5E9;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #2E7D32;
}

.evaluacion{
    background:#FFF8E1;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #FFB300;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# ENCABEZADO
# ==================================================
st.markdown(
    '<p class="titulo">🚛 Plataforma de Cadena de Abastecimiento</p>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">
    Bienvenido a la plataforma de capacitación logística.
    Seleccione un módulo en el menú lateral para iniciar el proceso de formación.
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3082/3082037.png",
    width=120
)

st.sidebar.title("Módulos")

modulo = st.sidebar.radio(
    "Seleccione una opción",
    [
        "🏆 Equipo de Canastas Aptas",
        "⚠️ Equipo de Canastas No Aptas",
        "🧼 Lavado y Desinfección",
        "🎓 Evaluación Final"
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

    tema = st.selectbox(
        "Seleccione un tema",
        [
            "Partes de la Canasta",
            "Partes del Separador",
            "Partes de la Estiba",
            "Partes del Gancho",
            "Apilado Correcto",
            "Anidado Correcto",
            "Capacidad de Canastas",
            "Sentido de la Bandeja",
            "Armado de Estiba",
            "Almacenamiento",
            "Transporte"
        ]
    )

    if tema == "Partes de la Canasta":

        st.markdown("""
        <div class="resaltado">
        ✔ Manijas

        ✔ Hendiduras

        ✔ Piso ventilado

        ✔ Refuerzos estructurales

        ✔ Sistema de anidado

        ✔ Sistema de apilado

        ✔ Identificador de posición
        </div>
        """, unsafe_allow_html=True)

    elif tema == "Partes del Separador":

        st.info("""
        Medidas:

        • 124 cm x 66 cm

        • Espesor aproximado: 2 cm
        """)

    elif tema == "Partes de la Estiba":

        st.info("""
        Medidas:

        • Largo: 124 cm

        • Ancho: 66 cm

        • Altura: 10.5 cm
        """)

    elif tema == "Partes del Gancho":

        st.success("""
        Utilizado para asegurar la carga
        durante el estibado.
        """)

    elif tema == "Apilado Correcto":

        st.success("""
        ✔ Las pestañas deben encajar.

        ✔ El identificador debe quedar
        en el lado opuesto.
        """)

    elif tema == "Anidado Correcto":

        st.success("""
        ✔ Las columnas inferiores deben
        encajar en los rieles.

        ✔ El identificador debe quedar
        en el mismo costado.
        """)

    elif tema == "Capacidad de Canastas":

        st.table({
            "Tipo Huevo": ["A-AA-B-M-L", "XL", "JUMBO"],
            "Cantidad": [240, 180, 120]
        })

    elif tema == "Sentido de la Bandeja":

        st.warning("""
        El primer nivel debe alinearse
        correctamente con el piso
        de la canasta.
        """)

    elif tema == "Armado de Estiba":

        st.write("""
        1. Ubicar 4 canastas base.

        2. Instalar gancho inferior.

        3. Completar niveles.

        4. Instalar gancho superior.

        5. Aplicar vinipel.
        """)

    elif tema == "Almacenamiento":

        st.write("""
        • Pasillo de maniobra: 1.5 m

        • Pasillo de seguridad: 1.0 m

        • Distancia a pared: 0.60 m
        """)

    elif tema == "Transporte":

        st.write("""
        Verificar:

        ✔ Estado de canastas

        ✔ Estado de separadores

        ✔ Estado de estibas

        ✔ Estado de ganchos
        """)

# ==================================================
# MODULO 2
# ==================================================
elif modulo == "⚠️ Equipo de Canastas No Aptas":

    st.markdown(
        '<p class="subtitulo">Equipo de Canastas No Aptas</p>',
        unsafe_allow_html=True
    )

    st.error("""
    Una canasta NO apta presenta:

    • Manijas rotas

    • Piso fracturado

    • Hendiduras dañadas

    • Refuerzos fracturados

    • Sistema de anidado roto

    • Sistema de apilado roto

    • Identificador dañado
    """)

    st.markdown("### Procedimiento")

    st.write("""
    1. Identificar daño.

    2. Clasificar daño.

    3. Contabilizar unidades.

    4. Registrar formulario.

    5. Coordinar envío.

    6. Gestionar reparación.
    """)

    st.markdown("### Clasificación")

    daño = st.selectbox(
        "Seleccione el daño",
        [
            "Manija rota",
            "Piso fracturado",
            "Refuerzo roto",
            "Sistema de apilado roto",
            "Sistema de anidado roto"
        ]
    )

    st.warning(f"Canasta clasificada como NO APTA por: {daño}")

# ==================================================
# MODULO 3
# ==================================================
elif modulo == "🧼 Lavado y Desinfección":

    st.markdown(
        '<p class="subtitulo">Lavado y Desinfección de Canastas</p>',
        unsafe_allow_html=True
    )

    pestañas = st.tabs([
        "EPP",
        "Productos",
        "Proceso",
        "Secado",
        "Consideraciones"
    ])

    with pestañas[0]:

        st.markdown("""
        ### Elementos de Protección Personal

        ✔ Gorro

        ✔ Monogafas

        ✔ Guantes nitrilo

        ✔ Delantal plástico

        ✔ Botas
        """)

    with pestañas[1]:

        col1, col2 = st.columns(2)

        with col1:

            st.success("""
            DETERGENTE

            Biodex

            Dilución:

            30 ml por cada
            1000 ml de agua
            """)

        with col2:

            st.info("""
            DESINFECTANTE

            Biosanit

            Dilución:

            5 ml por cada
            1000 ml de agua
            """)

    with pestañas[2]:

        st.markdown("""
        ### Proceso de Lavado

        1. Clasificar canastas

        2. Humedecer

        3. Aplicar detergente

        4. Esperar 10 minutos

        5. Refregar

        6. Enjuagar

        7. Aplicar desinfectante

        8. No enjuagar
        """)

    with pestañas[3]:

        st.warning("""
        Tiempo mínimo de secado:

        4 horas
        """)

    with pestañas[4]:

        st.write("""
        ✔ Lavar diariamente las canastas no aptas.

        ✔ Mantener presión de 1700 PSI.

        ✔ Usar cepillo ultrasuave.

        ✔ Secar completamente antes del uso.

        ✔ Utilizar siempre Biodex y Biosanit.
        """)

# ==================================================
# EVALUACIÓN FINAL
# ==================================================
elif modulo == "🎓 Evaluación Final":

    st.markdown(
        '<p class="subtitulo">Evaluación Final</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="evaluacion">Responda las siguientes preguntas.</div>',
        unsafe_allow_html=True
    )

    p1 = st.radio(
        "1. En el apilado el identificador debe quedar:",
        [
            "Mismo lado",
            "Lado opuesto"
        ]
    )

    p2 = st.radio(
        "2. Una canasta con manija rota es:",
        [
            "Apta",
            "No apta"
        ]
    )

    p3 = st.radio(
        "3. Biodex se diluye:",
        [
            "5 ml por litro",
            "30 ml por litro",
            "100 ml por litro"
        ]
    )

    p4 = st.radio(
        "4. Tiempo mínimo de secado:",
        [
            "1 hora",
            "2 horas",
            "4 horas"
        ]
    )

    if st.button("Calificar Examen"):

        nota = 0

        if p1 == "Lado opuesto":
            nota += 25

        if p2 == "No apta":
            nota += 25

        if p3 == "30 ml por litro":
            nota += 25

        if p4 == "4 horas":
            nota += 25

        st.metric("Resultado", f"{nota}/100")

        if nota >= 80:
            st.success("APROBADO ✅")
            st.balloons()
        else:
            st.error("NO APROBADO ❌")

# ==================================================
# PIE DE PAGINA
# ==================================================
st.markdown("---")

st.caption(
    "Plataforma de Cadena de Abastecimiento | Gestión Logística | Incubadora Santander"
)