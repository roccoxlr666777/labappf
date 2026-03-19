import streamlit as st
import streamlit.components.v1 as components

# Configuración de página
st.set_page_config(page_title="Gestor Jurídico Laboral", layout="wide")

# CSS Personalizado para el "Look & Feel" de documento y Tooltips
st.markdown("""
<style>
    /* Estilo del Papel */
    .paper {
        background-color: white;
        padding: 50px;
        color: black;
        font-family: 'Times New Roman', serif;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border: 1px solid #ddd;
        line-height: 1.6;
    }
    
    /* Tooltips con JS/CSS */
    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 2px dotted #2196F3;
        color: #0d47a1;
        cursor: help;
        font-weight: bold;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 250px;
        background-color: #333;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%; 
        left: 50%;
        margin-left: -125px;
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 0.8rem;
        font-family: sans-serif;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }

    /* Estilo de Impresión */
    @media print {
        .no-print { display: none !important; }
        .paper { box-shadow: none; border: none; padding: 0; }
    }
</style>
""", unsafe_allow_html=True)

# Lógica de Navegación
menu = st.sidebar.radio("Navegación", ["Redactor de Contrato", "Causales y Suspensión"])

if menu == "Redactor de Contrato":
    st.title("📄 Redactor de Contrato Individual de Trabajo")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("Datos del Contrato")
        with st.expander("Identificación de las Partes", expanded=True):
            patron = st.text_input("Nombre del Patrón/Empresa", "Empresa S.A. de C.V.")
            trabajador = st.text_input("Nombre del Trabajador", "Juan Pérez")
            nacionalidad = st.text_input("Nacionalidad/CURP", "Mexicana / XXXX000000")
        
        with st.expander("Condiciones de Trabajo"):
            puesto = st.text_input("Puesto o Funciones", "Analista de Datos")
            jornada = st.selectbox("Tipo de Jornada", ["Diurna (8h)", "Nocturna (7h)", "Mixta (7.5h)"])
            salario = st.number_input("Salario Mensual ($)", value=15000)
            lugar = st.text_input("Lugar de Trabajo", "Ciudad de México")

    with col2:
        st.subheader("Previsualización del Documento")
        
        # HTML del Contrato con Tooltips
        html_contrato = f"""
        <div class="paper" id="printableArea">
            <h2 style="text-align: center;">CONTRATO INDIVIDUAL DE TRABAJO</h2>
            <p>CONTRATO QUE CELEBRAN POR UNA PARTE EL 
                <span class="tooltip">PATRÓN<span class="tooltiptext">Persona física o moral que utiliza los servicios de uno o varios trabajadores (Art. 10 LFT).</span></span> 
                <b>{patron}</b> Y POR LA OTRA EL 
                <span class="tooltip">TRABAJADOR<span class="tooltiptext">Persona física que presta a otra un trabajo personal subordinado (Art. 8 LFT).</span></span> 
                <b>{trabajador}</b>, BAJO LAS SIGUIENTES CLÁUSULAS:</p>
            
            <p><b>PRIMERA. EL TRABAJO:</b> El trabajador se obliga a prestar su 
                <span class="tooltip">TRABAJO<span class="tooltiptext">Toda actividad humana, intelectual o material, independientemente del grado de preparación (Art. 8 LFT).</span></span> 
                consistente en: <i>{puesto}</i>.</p>
            
            <p><b>SEGUNDA. JORNADA:</b> Las partes acuerdan una jornada de tipo {jornada}.</p>
            
            <p><b>TERCERA. SALARIO:</b> El trabajador percibirá la cantidad de ${salario:,.2f} MXN mensuales.</p>
            
            <hr>
            <div style="background: #fff3e0; padding: 10px; border-left: 5px solid #ff9800;">
                <small>⚠️ <b>Cláusulas Irrenunciables (Se tendrán por no puestas):</b><br>
                - Renuncia a derechos adquiridos (aguinaldo, vacaciones).<br>
                - Salarios inferiores al mínimo.<br>
                - Jornadas inhumanas o mayores a las legales.</small>
            </div>
        </div>
        """
        st.markdown(html_contrato, unsafe_allow_html=True)
        
        # Botón de Impresión usando JS
        if st.button("🖨️ Imprimir Contrato"):
            components.html("""
                <script>
                    var printContents = window.parent.document.getElementById('printableArea').innerHTML;
                    var originalContents = window.parent.document.body.innerHTML;
                    window.parent.print();
                </script>
            """, height=0)

elif menu == "Causales y Suspensión":
    st.title("⚖️ Terminación y Suspensión de la Relación")
    
    # Imagen de fuente libre (Unsplash - Derecho/Legal)
    st.image("https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&q=80&w=1000", 
             caption="Marco Legal de la Relación Laboral")

    tab1, tab2, tab3 = st.tabs(["Rescisión y Despido", "Suspensión Colectiva", "Contingencias"])
    
    with tab1:
        st.subheader("Causales de Rescisión (Art. 47 y 51 LFT)")
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("**Sin responsabilidad para el patrón (Despido Justificado):**")
            st.write("- Engaño con certificados falsos.\n- Incurrir en faltas de probidad u honradez.\n- Violencia contra el patrón o compañeros.\n- Más de 3 faltas en 30 días sin permiso.")
        with col_b:
            st.warning("**Sin responsabilidad para el trabajador (Retiro/Renuncia Justificada):**")
            st.write("- Engaño del patrón sobre condiciones.\n- Falta de probidad del patrón.\n- Reducción del salario.\n- Existencia de peligro grave para la salud.")

    with tab2:
        st.subheader("Suspensión Colectiva y Recorte de Personal")
        st.write("""
        Cuando la empresa necesita reducir su plantilla o suspender actividades temporalmente:
        * **Fuerza mayor o caso fortuito:** No imputable al patrón.
        * **Incapacidad física o mental del patrón:** Que imposibilite el trabajo.
        * **Exceso de producción:** Requiere autorización de la Junta/Tribunal.
        """)
        
    with tab3:
        st.error("🚨 Contingencias Sanitarias")
        st.write("""
        Conforme a la reforma de la LFT (derivada de casos como el AH1N1 o COVID-19):
        1. Si la autoridad declara contingencia que implique suspensión, el patrón debe pagar una **indemnización de un día de salario mínimo general vigente por cada día que dure la suspensión**, sin exceder de un mes (Art. 429, IV).
        """)