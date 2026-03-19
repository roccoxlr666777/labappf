import streamlit as st
import streamlit.components.v1 as components
from datetime import date

st.set_page_config(page_title="Consultor LFT Pro", layout="wide", initial_sidebar_state="expanded")

# --- ESTILOS DE DESPACHO ---
st.markdown("""
<style>
    .lft-article {
        background-color: #f4f4f2;
        padding: 20px;
        border-left: 5px solid #1a3a5a;
        font-family: 'Courier New', Courier, monospace;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .example-box {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 5px;
        border: 1px dashed #2980b9;
        margin-top: 10px;
    }
    .reinicio-alerta {
        color: #d35400;
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.9em;
    }
    .document-body {
        background-color: white;
        padding: 45px;
        border: 1px solid #000;
        font-family: 'Times New Roman', Times, serif;
        text-align: justify;
    }
</style>
""", unsafe_allow_html=True)

# --- PANEL LATERAL: CONTRATO FORMAL (ART. 25) ---
with st.sidebar:
    st.title("📂 Gestión de Expediente")
    modo = st.radio("Acción:", ["Redactar Contrato Art. 25", "Catálogo Art. 42, 47, 51, 53"])
    
    if modo == "Redactar Contrato Art. 25":
        st.subheader("Datos del Proemio")
        p_nom = st.text_input("Patrón / Empresa")
        p_rfc = st.text_input("RFC Patrón")
        p_dom = st.text_input("Domicilio Fiscal")
        
        st.divider()
        t_nom = st.text_input("Trabajador")
        t_curp = st.text_input("CURP")
        t_rfc = st.text_input("RFC Trabajador")
        t_nac = st.text_input("Nacionalidad", "Mexicana")
        t_edad = st.number_input("Edad", 18, 99, 30)
        t_sexo = st.selectbox("Sexo", ["Masculino", "Femenino"])
        t_dom = st.text_input("Domicilio Particular")
        
        st.divider()
        st.subheader("Condiciones Art. 25")
        c_tipo = st.selectbox("Tipo (Art. 35)", ["Tiempo Indeterminado", "Tiempo Determinado", "Obra Determinada"])
        c_serv = st.text_area("Servicios (Fracc. III - Precisión)")
        c_lugar = st.text_input("Lugar de prestación (Fracc. IV)")
        c_jornada = st.text_input("Jornada (Fracc. V - Horario y duración)")
        c_salario = st.text_input("Salario (Monto y forma de pago)")
        c_pago_dia = st.text_input("Día de Pago")
        c_pago_lug = st.text_input("Lugar de Pago (Art. 108)")
        c_ben = st.text_area("Beneficiarios (Fracc. X)")

# --- ÁREA PRINCIPAL ---
if modo == "Redactar Contrato Art. 25":
    st.header("Generador de Contrato Individual de Trabajo")
    
    html_contrato = f"""
    <div class="document-body" id="print_area">
        <h3 style="text-align:center">CONTRATO INDIVIDUAL DE TRABAJO</h3>
        <p>CONTRATO QUE CELEBRAN POR UNA PARTE EL PATRÓN <b>{p_nom}</b>, CON RFC <b>{p_rfc}</b> Y DOMICILIO EN <b>{p_dom}</b>, Y POR LA OTRA EL TRABAJADOR <b>{t_nom}</b>, DE NACIONALIDAD <b>{t_nac}</b>, DE <b>{t_edad}</b> AÑOS, SEXO <b>{t_sexo}</b>, CON CURP <b>{t_curp}</b>, RFC <b>{t_rfc}</b> Y DOMICILIO EN <b>{t_dom}</b>, AL TENOR DE LAS SIGUIENTES:</p>
        
        <h4 style="text-align:center">CLÁUSULAS</h4>
        <p><b>PRIMERA. DURACIÓN.</b> El presente contrato se celebra por <b>{c_tipo}</b> de acuerdo al Art. 35 de la LFT.</p>
        <p><b>SEGUNDA. SERVICIOS.</b> El trabajador se obliga a prestar sus servicios consistentes en: {c_serv}.</p>
        <p><b>TERCERA. LUGAR.</b> El servicio se prestará en: {c_lugar}.</p>
        <p><b>CUARTA. JORNADA.</b> La duración de la jornada será: {c_jornada}.</p>
        <p><b>QUINTA. SALARIO.</b> El salario será de {c_salario}, pagaderos el día {c_pago_dia} en {c_pago_lug}.</p>
        <p><b>SEXTA. BENEFICIARIOS.</b> Se designan como beneficiarios conforme al Art. 25 fracc. X a: {c_ben}.</p>
    </div>
    """
    st.markdown(html_contrato, unsafe_allow_html=True)
    if st.button("🖨️ Imprimir"):
        components.html("<script>window.parent.print();</script>", height=0)

else:
    # --- CATÁLOGO LITERAL ---
    st.header("📖 Diccionario Literal de la Ley Federal del Trabajo")
    
    sel_art = st.selectbox("Seleccione el Artículo a consultar:", 
                          ["Artículo 42 (Suspensión)", "Artículo 47 (Rescisión Patrón)", "Artículo 51 (Rescisión Trabajador)", "Artículo 53 (Terminación)"])

    if sel_art == "Artículo 42 (Suspensión)":
        st.markdown("#### **Artículo 42.** Son causas de suspensión temporal de las obligaciones de prestar el servicio y pagar el salario, sin responsabilidad para el trabajador y el patrón:")
        
        causales_42 = {
            "I. La enfermedad contagiosa del trabajador.": {
                "ejemplo": "Trabajador con diagnóstico de Varicela o COVID-19.",
                "reinicio": "Art. 45-I: Al día siguiente de la fecha en que cese la causa."
            },
            "III. El arresto del trabajador.": {
                "ejemplo": "Detención por una falta administrativa (ej. alcoholímetro) de 36 horas.",
                "reinicio": "Art. 45-II: Dentro de los 15 días siguientes a la fecha en que el trabajador recupere su libertad."
            },
            "VII. La falta de los documentos que exijan las Leyes, necesarios para la prestación del servicio.": {
                "ejemplo": "Vencimiento de la licencia de conducir federal para un chofer.",
                "reinicio": "Art. 45-I: Al día siguiente en que se obtengan los documentos."
            }
        }
        
        for titulo, datos in causales_42.items():
            with st.container():
                st.markdown(f"<div class='lft-article'>{titulo}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='example-box'><b>Caso práctico:</b> {datos['ejemplo']}<br><span class='reinicio-alerta'>REINICIO: {datos['reinicio']}</span></div>", unsafe_allow_html=True)

    elif sel_art == "Artículo 47 (Rescisión Patrón)":
        st.markdown("#### **Artículo 47.** Son causas de rescisión de la relación de trabajo, sin responsabilidad para el patrón:")
        
        causales_47 = [
            "I. Engañarlo el trabajador con certificados falsos o referencias en los que se atribuyan capacidades que carezca.",
            "II. Incurrir el trabajador en faltas de probidad u honradez, en actos de violencia contra el patrón, sus familiares o personal directivo.",
            "VIII. Cometer el trabajador actos inmorales o de hostigamiento y/o acoso sexual contra cualquier persona en el establecimiento.",
            "X. Tener el trabajador más de tres faltas de asistencia en un período de treinta días, sin permiso del patrón o sin causa justificada.",
            "XIII. La sentencia ejecutoriada que imponga al trabajador una pena de prisión, que le impida el cumplimiento de la relación de trabajo."
        ]
        
        for c in causales_47:
            st.markdown(f"<div class='lft-article'>{c}</div>", unsafe_allow_html=True)
            if "faltas" in c:
                st.info("💡 **Ejemplo:** El trabajador falta los días 1, 5, 10 y 15 del mes. Al cuarto día de inasistencia en ese rango de 30 días, se configura la causal.")

    elif sel_art == "Artículo 53 (Terminación)":
        st.markdown("#### **Artículo 53.** Son causas de terminación de las relaciones de trabajo:")
        terminaciones = [
            "I. El mutuo consentimiento de las partes;",
            "II. La muerte del trabajador;",
            "III. La terminación de la obra o vencimiento del término o inversión del capital (Art. 36, 37 y 38);",
            "IV. La incapacidad física o mental o inhabilidad manifiesta del trabajador, que haga imposible la prestación del trabajo."
        ]
        for t in terminaciones:
            st.markdown(f"<div class='lft-article'>{t}</div>", unsafe_allow_html=True)
