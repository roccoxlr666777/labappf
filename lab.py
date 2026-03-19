import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Herramienta LFT", layout="wide")

st.markdown("""
<style>
    .documento {
        background-color: white;
        padding: 50px;
        color: black;
        font-family: 'Times New Roman', serif;
        line-height: 1.6;
        text-align: justify;
        border: 1px solid #ccc;
    }
    .tooltip-legal {
        position: relative;
        display: inline-block;
        color: #000;
        border-bottom: 1px dotted #000;
        cursor: help;
        font-weight: bold;
    }
    .tooltip-legal .tooltiptext {
        visibility: hidden;
        width: 300px;
        background-color: #333;
        color: #fff;
        text-align: left;
        border-radius: 4px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -150px;
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 0.85rem;
        font-family: 'Arial', sans-serif;
        font-weight: normal;
    }
    .tooltip-legal:hover .tooltiptext { visibility: visible; opacity: 1; }
    .clausula-nula {
        text-decoration: line-through;
        color: #c00;
        background-color: #fdd;
        padding: 2px;
    }
    .fraccion {
        background-color: #f9f9f9;
        padding: 15px;
        border-left: 4px solid #333;
        margin-bottom: 10px;
        font-family: 'Arial', sans-serif;
        color: #000;
    }
    .ejemplo {
        background-color: #eee;
        padding: 10px;
        margin-bottom: 15px;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Módulos")
    modulo = st.radio("Seleccione:", ["Contrato Individual (Art. 25)", "Catálogo LFT Íntegro"])
    
    if modulo == "Contrato Individual (Art. 25)":
        st.subheader("Datos del Patrón")
        p_nombre = st.text_input("Nombre o Razón Social", "Empresa S.A. de C.V.")
        p_rfc = st.text_input("RFC del Patrón")
        p_dom = st.text_input("Domicilio del Patrón")
        
        st.subheader("Datos del Trabajador")
        t_nombre = st.text_input("Nombre del Trabajador", "Nombre Completo")
        t_nac = st.text_input("Nacionalidad", "Mexicana")
        t_edad = st.number_input("Edad", min_value=15, value=25)
        t_sexo = st.selectbox("Sexo", ["Masculino", "Femenino", "Otro"])
        t_curp = st.text_input("CURP")
        t_rfc = st.text_input("RFC del Trabajador")
        t_dom = st.text_input("Domicilio del Trabajador")
        
        st.subheader("Condiciones Laborales")
        tipo_rel = st.selectbox("Naturaleza de la relación", ["Tiempo Indeterminado", "Tiempo Determinado", "Obra Determinada", "Temporada"])
        servicios = st.text_area("Servicios a prestar (Detallados)")
        lugar_serv = st.text_input("Lugar de prestación del servicio")
        jornada = st.text_input("Duración y horario de la jornada")
        salario = st.text_input("Monto del Salario")
        forma_pago = st.text_input("Día y lugar de pago")
        beneficiarios = st.text_area("Beneficiarios (Art. 25 Fracc. X)")
        
        st.subheader("Ejemplificar Cláusulas Nulas (Art. 5)")
        nula_1 = st.checkbox("Renuncia a indemnización")
        nula_2 = st.checkbox("Salario inferior al mínimo")

if modulo == "Contrato Individual (Art. 25)":
    st.title("Redacción del Contrato")
    
    html_contrato = f"""
    <div class="documento" id="area-impresion">
        <h2 style="text-align: center;">CONTRATO INDIVIDUAL DE TRABAJO</h2>
        
        <p>CONTRATO INDIVIDUAL DE TRABAJO QUE CELEBRAN POR UNA PARTE <b>{p_nombre}</b>, CON RFC <b>{p_rfc}</b> Y DOMICILIO EN <b>{p_dom}</b>, A QUIEN EN LO SUCESIVO SE LE DENOMINARÁ EL <span class="tooltip-legal">PATRÓN<span class="tooltiptext">Art. 10 LFT: La persona física o moral que utiliza los servicios de uno o varios trabajadores.</span></span>; Y POR LA OTRA PARTE <b>{t_nombre}</b>, DE NACIONALIDAD <b>{t_nac}</b>, DE <b>{t_edad}</b> AÑOS, SEXO <b>{t_sexo}</b>, CON CURP <b>{t_curp}</b>, RFC <b>{t_rfc}</b> Y DOMICILIO EN <b>{t_dom}</b>, A QUIEN EN LO SUCESIVO SE LE DENOMINARÁ EL <span class="tooltip-legal">TRABAJADOR<span class="tooltiptext">Art. 8 LFT: La persona física que presta a otra, física o moral, un trabajo personal subordinado.</span></span>; AL TENOR DE LAS SIGUIENTES:</p>
        
        <h3 style="text-align: center;">CLÁUSULAS</h3>
        
        <p><b>PRIMERA.</b> Las partes reconocen que el presente contrato se celebra por <b>{tipo_rel}</b>.</p>
        <p><b>SEGUNDA.</b> El trabajador se obliga a prestar su <span class="tooltip-legal">TRABAJO<span class="tooltiptext">Art. 8 LFT: Toda actividad humana, intelectual o material, independientemente del grado de preparación técnica.</span></span> personal subordinado, el cual consistirá expresamente en: <i>{servicios}</i>.</p>
        <p><b>TERCERA.</b> Los servicios se prestarán en: <b>{lugar_serv}</b>.</p>
        <p><b>CUARTA.</b> La duración de la jornada será de: <b>{jornada}</b>.</p>
        <p><b>QUINTA.</b> El trabajador percibirá la cantidad de <b>{salario}</b>, que le será cubierta el <b>{forma_pago}</b>.</p>
        <p><b>SEXTA.</b> Conforme a la Fracción X del Artículo 25 de la LFT, el trabajador designa como beneficiarios para el pago de salarios y prestaciones devengadas a: <b>{beneficiarios}</b>.</p>
    """
    
    if nula_1 or nula_2:
        html_contrato += "<p><b>SÉPTIMA. (CLÁUSULAS NULAS - ART. 5 LFT).</b></p><ul>"
        if nula_1: html_contrato += '<li class="clausula-nula">El trabajador renuncia anticipadamente al pago de cualquier indemnización en caso de rescisión.</li>'
        if nula_2: html_contrato += '<li class="clausula-nula">El trabajador acepta un salario inferior al mínimo general vigente.</li>'
        html_contrato += "</ul>"
        
    html_contrato += "</div>"
    
    st.markdown(html_contrato, unsafe_allow_html=True)
    if st.button("🖨️ Imprimir"):
        components.html("<script>window.parent.print();</script>", height=0)

elif modulo == "Catálogo LFT Íntegro":
    st.title("Artículos LFT (Texto Íntegro)")
    
    art = st.selectbox("Seleccione el Artículo:", [
        "Artículo 42 y 42 Bis (Suspensión)", 
        "Artículo 47 (Rescisión sin responsabilidad para el Patrón)", 
        "Artículo 51 (Rescisión sin responsabilidad para el Trabajador)", 
        "Artículo 53 (Terminación)"
    ])

    if art == "Artículo 42 y 42 Bis (Suspensión)":
        st.markdown("### Artículo 42. Son causas de suspensión temporal de las obligaciones de prestar el servicio y pagar el salario, sin responsabilidad para el trabajador y el patrón:")
        fracciones_42 = [
            ("I. La enfermedad contagiosa del trabajador;", "Ejemplo: Diagnóstico de COVID-19. Reinicio (Art. 45-I): Al día siguiente de que cese la causa."),
            ("II. La incapacidad temporal ocasionada por un accidente o enfermedad que no constituya un riesgo de trabajo;", "Ejemplo: Fractura fuera del horario laboral. Reinicio (Art. 45-I): Al día siguiente de que cese la causa."),
            ("III. El arresto del trabajador;", "Ejemplo: Detención administrativa. Reinicio (Art. 45-II): Dentro de los 15 días siguientes a que recupere su libertad."),
            ("IV. El cumplimiento de los servicios y el desempeño de los cargos mencionados en el artículo 5o de la Constitución, y el de las obligaciones consignadas en el artículo 31, fracción III de la misma Constitución;", "Ejemplo: Servicio militar. Reinicio (Art. 45-III): Dentro de los 15 días siguientes a la terminación."),
            ("V. La designación de los trabajadores como representantes ante los organismos estatales, Comisión Nacional de los Salarios Mínimos, Comisión Nacional para la Participación de los Trabajadores en las Utilidades de las Empresas y otros semejantes;", "Ejemplo: Nombramiento en CONASAMI. Reinicio (Art. 45-III): Dentro de los 15 días siguientes a la terminación."),
            ("VI. La falta de los documentos que exijan las Leyes y reglamentos, necesarios para la prestación del servicio, cuando sea imputable al trabajador;", "Ejemplo: Licencia de manejo vencida. Reinicio (Art. 45-I): Al día siguiente de subsanar el requisito."),
            ("VII. La conclusión de la temporada en el caso de los trabajadores contratados bajo esta modalidad; y", "Ejemplo: Fin de la cosecha. Reinicio: Al iniciar la siguiente temporada."),
            ("VIII. La licencia a que se refiere el artículo 140 Bis de la Ley del Seguro Social.", "Ejemplo: Licencia para cuidados médicos de hijos con cáncer. Reinicio (Art. 45-I): Al día siguiente de concluida la licencia.")
        ]
        for f, e in fracciones_42:
            st.markdown(f"<div class='fraccion'>{f}</div><div class='ejemplo'>{e}</div>", unsafe_allow_html=True)
            
        st.markdown("### Artículo 42 Bis.")
        st.markdown("<div class='fraccion'>En los casos en que las autoridades competentes emitan una declaratoria de contingencia sanitaria, conforme a las disposiciones aplicables, que implique la suspensión de las labores, se estará a lo dispuesto por el artículo 429, fracción IV de esta Ley.</div>", unsafe_allow_html=True)

    elif art == "Artículo 47 (Rescisión sin responsabilidad para el Patrón)":
        st.markdown("### Artículo 47. Son causas de rescisión de la relación de trabajo, sin responsabilidad para el patrón:")
        fracciones_47 = [
            ("I. Engañarlo el trabajador o en su caso, el sindicato que lo hubiese propuesto o recomendado con certificados falsos o referencias en los que se atribuyan al trabajador capacidad, aptitudes o facultades de que carezca. Esta causa de rescisión dejará de tener efecto después de treinta días de prestar sus servicios el trabajador;", "Ejemplo: Presentar cédula profesional falsa."),
            ("II. Incurrir el trabajador, durante sus labores, en faltas de probidad u honradez, en actos de violencia, amagos, injurias o malos tratamientos en contra del patrón, sus familiares o del personal directivo o administrativo de la empresa o establecimiento, o en contra de clientes y proveedores del patrón, salvo que medie provocación o que obre en defensa propia;", "Ejemplo: Robo de mercancía o agresión física al supervisor."),
            ("III. Incurrir el trabajador, durante sus labores, en faltas de probidad u honradez, en actos de violencia, amagos, injurias o malos tratamientos en contra de sus compañeros, si como consecuencia de ellos se altera la disciplina del lugar en que se desempeñe el trabajo;", "Ejemplo: Iniciar una pelea a golpes con otro trabajador en piso de ventas."),
            ("IV. Incurrir el trabajador, fuera del servicio, en contra del patrón, sus familiares o personal directivo administrativo, en alguno de los actos a que se refiere la fracción II, si son de tal manera graves que hagan imposible el cumplimiento de la relación de trabajo;", "Ejemplo: Agredir al patrón en la vía pública en un día de descanso."),
            ("V. Ocasionar el trabajador, intencionalmente, perjuicios materiales durante el desempeño de las labores o con motivo de ellas, en los edificios, obras, maquinaria, instrumentos, materias primas y demás objetos relacionados con el trabajo;", "Ejemplo: Destruir intencionalmente el servidor de la empresa."),
            ("VI. Ocasionar el trabajador los perjuicios de que habla la fracción anterior siempre que sean graves, sin dolo, pero con negligencia tal, que ella sea la causa única del perjuicio;", "Ejemplo: Olvidar cerrar las válvulas por descuido, inundando la fábrica."),
            ("VII. Comprometer el trabajador, por su imprudencia o descuido inexcusable, la seguridad del establecimiento o de las personas que se encuentren en él;", "Ejemplo: Fumar en una zona de manejo de explosivos o combustibles."),
            ("VIII. Cometer el trabajador actos inmorales o de hostigamiento y/o acoso sexual contra cualquier persona en el establecimiento o lugar de trabajo;", "Ejemplo: Realizar tocamientos no consensuados a compañeros de trabajo."),
            ("IX. Revelar el trabajador los secretos de fabricación o dar a conocer asuntos de carácter reservado, con perjuicio de la empresa;", "Ejemplo: Vender la base de datos de clientes a la competencia."),
            ("X. Tener el trabajador más de tres faltas de asistencia en un período de treinta días, sin permiso del patrón o sin causa justificada;", "Ejemplo: Faltar 4 veces de forma injustificada en un lapso de 30 días naturales."),
            ("XI. Desobedecer el trabajador al patrón o a sus representantes, sin causa justificada, siempre que se trate del trabajo contratado;", "Ejemplo: Negarse sistemáticamente a realizar las funciones descritas en su contrato."),
            ("XII. Negarse el trabajador a adoptar las medidas preventivas o a seguir los procedimientos indicados para evitar accidentes o enfermedades;", "Ejemplo: Negarse a utilizar casco y arnés en una obra de construcción."),
            ("XIII. Concurrir el trabajador a sus labores en estado de embriaguez o bajo la influencia de algún narcótico o droga enervante, salvo que, en este último caso, exista prescripción médica. Antes de iniciar su servicio, el trabajador deberá poner el hecho en conocimiento del patrón y presentar la prescripción suscrita por el médico;", "Ejemplo: Llegar al turno bajo los efectos del alcohol."),
            ("XIV. La sentencia ejecutoriada que imponga al trabajador una pena de prisión, que le impida el cumplimiento de la relación de trabajo;", "Ejemplo: Condena penal de 2 años con privación de libertad."),
            ("XIV Bis. La falta de documentos que exijan las leyes y reglamentos, necesarios para la prestación del servicio cuando sea imputable al trabajador y que exceda del periodo a que se refiere la fracción IV del artículo 43; y", "Ejemplo: Pérdida definitiva del permiso de portación de armas para un guardia de seguridad."),
            ("XV. Las análogas a las establecidas en las fracciones anteriores, de igual manera graves y de consecuencias semejantes en lo que al trabajo se refiere.", "Ejemplo: Conductas graves no tipificadas arriba pero que rompen la relación laboral.")
        ]
        for f, e in fracciones_47:
            st.markdown(f"<div class='fraccion'>{f}</div><div class='ejemplo'>{e}</div>", unsafe_allow_html=True)

    elif art == "Artículo 51 (Rescisión sin responsabilidad para el Trabajador)":
        st.markdown("### Artículo 51. Son causas de rescisión de la relación de trabajo, sin responsabilidad para el trabajador:")
        fracciones_51 = [
            ("I. Engañarlo el patrón, o en su caso, el sindicato al proponerle el trabajo, respecto de las condiciones del mismo. Esta causa de rescisión dejará de tener efecto después de treinta días de prestar sus servicios el trabajador;", "Ejemplo: Prometer un sueldo base que luego no se cumple en el primer pago."),
            ("II. Incurrir el patrón, sus familiares o cualquiera de sus representantes, dentro del servicio, en faltas de probidad u honradez, actos de violencia, amenazas, injurias, hostigamiento y/o acoso sexual, malos tratamientos u otros análogos, en contra del trabajador, cónyuge, padres, hijos o hermanos;", "Ejemplo: Insultos y gritos constantes por parte del director general."),
            ("III. Incurrir el patrón, sus familiares o trabajadores, fuera del servicio, en los actos a que se refiere la fracción anterior, si son de tal manera graves que hagan imposible el cumplimiento de la relación de trabajo;", "Ejemplo: Amenazas de muerte emitidas por el patrón fuera de la oficina."),
            ("IV. Reducir el patrón el salario del trabajador;", "Ejemplo: Reducción unilateral del salario diario pactado."),
            ("V. No recibir el salario correspondiente en la fecha o lugar convenidos o acostumbrados;", "Ejemplo: Falta de pago de nómina en los días establecidos."),
            ("VI. Sufrir perjuicios causados maliciosamente por el patrón, en sus herramientas o útiles de trabajo;", "Ejemplo: Destrucción por parte del patrón de equipo propiedad del trabajador."),
            ("VII. La existencia de un peligro grave para la seguridad o salud del trabajador o de su familia, ya sea por carecer de condiciones higiénicas el establecimiento o porque no se cumplan las medidas preventivas y de seguridad que las leyes establezcan;", "Ejemplo: Obligar a laborar en un edificio con daño estructural inminente."),
            ("VIII. Comprometer el patrón, por su imprudencia o descuido inexcusable, la seguridad del establecimiento o de las personas que se encuentren en él;", "Ejemplo: Manejo negligente de maquinaria pesada por parte del patrón poniendo en riesgo al personal."),
            ("IX. Exigir la realización de actos, conductas o comportamientos que menoscaben o atenten contra la dignidad del trabajador; y", "Ejemplo: Obligar al personal a soportar castigos humillantes."),
            ("X. Las análogas a las establecidas en las fracciones anteriores, de igual manera graves y de consecuencias semejantes, en lo que al trabajo se refiere.", "Ejemplo: Conductas análogas imputables al patrón.")
        ]
        for f, e in fracciones_51:
            st.markdown(f"<div class='fraccion'>{f}</div><div class='ejemplo'>{e}</div>", unsafe_allow_html=True)

    elif art == "Artículo 53 (Terminación)":
        st.markdown("### Artículo 53. Son causas de terminación de las relaciones de trabajo:")
        fracciones_53 = [
            ("I. El mutuo consentimiento de las partes;", "Ejemplo: Convenio de terminación ante la autoridad laboral."),
            ("II. La muerte del trabajador;", "Ejemplo: Fallecimiento natural que activa el pago a los beneficiarios del Art. 25-X."),
            ("III. La terminación de la obra o vencimiento del término o inversión del capital, de conformidad con los artículos 36, 37 y 38;", "Ejemplo: Conclusión del edificio para el que fue contratado el personal de obra."),
            ("IV. La incapacidad física o mental o inhabilidad manifiesta del trabajador, que haga imposible la prestación del trabajo; y", "Ejemplo: Invalidez dictaminada por el IMSS que impide ejercer su profesión."),
            ("V. Los casos a que se refiere el artículo 434.", "Ejemplo: Cierre de la empresa por incosteabilidad económica declarada.")
        ]
        for f, e in fracciones_53:
            st.markdown(f"<div class='fraccion'>{f}</div><div class='ejemplo'>{e}</div>", unsafe_allow_html=True)
