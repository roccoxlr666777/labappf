import streamlit as st
import streamlit.components.v1 as components
from datetime import date

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Gestor Laboral Pro - México", layout="wide", initial_sidebar_state="expanded")

# --- ESTILOS CSS (Interfaz Limpia y Tooltips) ---
st.markdown("""
<style>
    .reportview-container { background: #f8f9fa; }
    .document-paper {
        background: white;
        padding: 60px;
        border: 1px solid #dcdcdc;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
        font-family: 'Times New Roman', serif;
        color: #1a1a1a;
        line-height: 1.6;
    }
    .clause-nula {
        text-decoration: line-through;
        color: #d9534f;
        background-color: #f9f2f4;
        padding: 2px 4px;
        border-radius: 4px;
        cursor: help;
    }
    .legal-tag {
        font-size: 0.8em;
        padding: 3px 8px;
        border-radius: 10px;
        font-weight: bold;
        margin-bottom: 10px;
        display: inline-block;
    }
    .suspension { background: #fff3cd; color: #856404; }
    .rescision { background: #f8d7da; color: #721c24; }
    .terminacion { background: #d4edda; color: #155724; }
</style>
""", unsafe_allow_html=True)

# --- PANEL LATERAL (CONTROLES) ---
with st.sidebar:
    st.title("🛠️ Panel de Control")
    st.info("Configura aquí los datos para generar el documento legal.")
    
    opcion_menu = st.radio("Ir a:", ["📝 Redactor de Contrato", "📚 Catálogo de Incidencias (LFT)"])
    
    st.divider()
    
    if opcion_menu == "📝 Redactor de Contrato":
        with st.expander("👤 Partes y Beneficiarios", expanded=True):
            patron = st.text_input("Nombre del Patrón/Empresa", "Despacho Jurídico S.C.")
            trabajador = st.text_input("Nombre del Trabajador", "Juan Pérez García")
            beneficiarios = st.text_area("Beneficiarios (Art. 25-X)", "María Pérez (Hija), 50%; Luis Pérez (Hijo), 50%.")
            
        with st.expander("⏰ Jornada y Lugar", expanded=True):
            tipo_contrato = st.selectbox("Duración", ["Tiempo Indeterminado", "Tiempo Determinado", "Obra Determinada"])
            horario_detallado = st.text_input("Horario exacto", "Lun-Vie 09:00 a 18:00 (1h comida)")
            lugar_labores = st.text_input("Lugar de Trabajo", "Av. Reforma 123, Puebla, Pue.")
            
        with st.expander("💰 Pago y Salario", expanded=True):
            salario_diario = st.number_input("Salario Diario ($)", value=600.0)
            fecha_pago = st.text_input("Periodicidad/Día de Pago", "Días 15 y 30 de cada mes")
            forma_pago = st.selectbox("Método", ["Transferencia", "Efectivo", "Cheque"])
            
        with st.expander("🚫 Simulador de Cláusulas Nulas"):
            nula_1 = st.checkbox("Renuncia a PTU/Aguinaldo")
            nula_2 = st.checkbox("Jornada de 12 horas s/extra")
            nula_3 = st.checkbox("Acepta descuentos por errores")

# --- ÁREA PRINCIPAL ---
if opcion_menu == "📝 Redactor de Contrato":
    st.header("Vista Previa del Contrato Laboral")
    
    # Construcción dinámica del contrato
    contrato_html = f"""
    <div class="document-paper" id="printable">
        <h2 style="text-align: center;">CONTRATO INDIVIDUAL DE TRABAJO</h2>
        <p>En la ciudad de Puebla, México, a fecha de {date.today()}, celebran el presente contrato por una parte <b>{patron}</b> (EL PATRÓN) y por la otra <b>{trabajador}</b> (EL TRABAJADOR).</p>
        
        <p><b>PRIMERA. DURACIÓN:</b> El contrato se celebra por <b>{tipo_contrato}</b>.</p>
        
        <p><b>SEGUNDA. SERVICIOS:</b> El trabajador desempeñará sus funciones en {lugar_labores}.</p>
        
        <p><b>TERCERA. JORNADA:</b> Se pacta una jornada de: <b>{horario_detallado}</b>.</p>
        
        <p><b>CUARTA. SALARIO:</b> El patrón pagará la cantidad de <b>${salario_diario:,.2f}</b> diarios, mediante {forma_pago} los días {fecha_pago}.</p>
        
        <p><b>QUINTA. BENEFICIARIOS:</b> Para efectos del Art. 25, fracción X de la LFT, el trabajador designa a: <br><i>{beneficiarios}</i>.</p>
    """
    
    if nula_1 or nula_2 or nula_3:
        contrato_html += "<p><b>SEXTA. DISPOSICIONES ADICIONALES (ANÁLISIS DE NULIDAD):</b><ul>"
        if nula_1: contrato_html += '<li class="clause-nula">El trabajador renuncia al pago de utilidades y aguinaldo del presente año.</li>'
        if nula_2: contrato_html += '<li class="clause-nula">Se pacta jornada extendida de 12 horas sin derecho a cobro de horas extraordinarias.</li>'
        if nula_3: contrato_html += '<li class="clause-nula">El trabajador autoriza descuentos directos por errores en la operación sin límite legal.</li>'
        contrato_html += "</ul><small><i>* Las cláusulas tachadas son nulas de pleno derecho (Art. 5 LFT).</i></small></p>"
    
    contrato_html += "</div>"
    
    st.markdown(contrato_html, unsafe_allow_html=True)
    
    if st.button("🖨️ Imprimir Documento"):
        components.html("<script>window.parent.print();</script>", height=0)

else:
    # --- CATÁLOGO DE INCIDENCIAS MEJORADO ---
    st.header("📚 Catálogo Legal: Suspensión, Rescisión y Terminación")
    
    cat = st.selectbox("Seleccione el supuesto jurídico:", 
                       ["Suspensión Temporal", "Rescisión (Despido Justificado)", "Rescisión (Retiro Justificado)", "Terminación y Casos Especiales"])
    
    if cat == "Suspensión Temporal":
        incidencias = {
            "Enfermedad Contagiosa (Art. 42-I)": {
                "ejemplo": "Trabajador con diagnóstico médico de enfermedad infectocontagiosa.",
                "inicio": "Desde la fecha del diagnóstico médico.",
                "reinicio": "Al día siguiente de que cese la causa (Alta médica).",
                "requisito": "Certificado de incapacidad del IMSS."
            },
            "Arresto del Trabajador (Art. 42-III)": {
                "ejemplo": "Detención por faltas administrativas o delitos no relacionados con el trabajo.",
                "inicio": "Desde el momento de la detención.",
                "reinicio": "A los 15 días siguientes de la fecha en que el trabajador sea puesto en libertad.",
                "requisito": "Copia de la boleta de libertad."
            },
            "Contingencia Sanitaria (Art. 42 Bis)": {
                "ejemplo": "Declaratoria oficial de la autoridad (ej. Pandemia).",
                "inicio": "En la fecha de publicación del decreto.",
                "reinicio": "Inmediatamente después de que termine la vigencia del decreto.",
                "pago": "1 día de salario mínimo por cada día de suspensión (máximo 30 días)."
            }
        }
        
        sel = st.selectbox("Especifique la causal:", list(incidencias.keys()))
        data = incidencias[sel]
        
        st.warning(f"### {sel}")
        st.write(f"**Ejemplo práctico:** {data['ejemplo']}")
        st.markdown(f"""
        - **🕒 Inicia:** {data['inicio']}
        - **🔄 Reinicio de labores:** {data['reinicio']}
        - **📄 Documento clave:** {data.get('requisito', 'Aviso oficial')}
        """)

    elif cat == "Rescisión (Despido Justificado)":
        st.error("### Causales de Rescisión (Art. 47 LFT)")
        st.markdown("""
        * **Faltas de probidad:** Actos de violencia contra el patrón o clientes.
        * **Daños materiales:** Causar daños a herramientas o equipo de forma intencional.
        * **Engaño:** Presentar certificados de estudio o habilidades falsas.
        * **Inasistencias:** Más de 3 faltas en 30 días sin permiso ni causa justificada.
        
        **Aviso de Rescisión:** El patrón debe entregar aviso escrito al trabajador o al Tribunal dentro de los 5 días hábiles siguientes.
        """)
        
    elif cat == "Terminación y Casos Especiales":
        col1, col2 = st.columns(2)
        with col1:
            st.success("#### Terminación Colectiva (Art. 434)")
            st.write("- Cierre de empresa por incosteabilidad.\n- Agotamiento de la materia de una industria extractiva.\n- Concurso mercantil.")
        with col2:
            st.info("#### Recorte de Personal")
            st.write("Si se reduce el personal, se debe respetar el escalafón: primero salen los de menor antigüedad.")
