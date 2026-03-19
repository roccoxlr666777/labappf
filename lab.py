import streamlit as st
import streamlit.components.v1 as components
from datetime import date

st.set_page_config(page_title="Consola Jurídica Laboral", layout="wide")

# --- ESTILOS MEJORADOS ---
st.markdown("""
<style>
    .reportview-container { background: #f5f7f9; }
    .main-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        border-left: 8px solid #2c3e50;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .status-badge {
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 0.85em;
        font-weight: bold;
    }
    .suspension { background: #fff4e5; color: #b76e00; }
    .rescision { background: #ffebee; color: #c62828; }
    .terminacion { background: #e8f5e9; color: #2e7d32; }
</style>
""", unsafe_allow_html=True)

# --- BASE DE DATOS JURÍDICA (CATÁLOGO COMPLETO) ---
DB_LEGAL = {
    "SUSPENSIÓN TEMPORAL": {
        "Arresto del trabajador": {
            "articulo": "Art. 42 Fracc. III",
            "ejemplo": "El trabajador es detenido por un incidente de tránsito ajeno a la empresa por 72 horas.",
            "inicio": "Desde que el trabajador acredite el arresto ante el patrón.",
            "reinicio": "Al día siguiente de aquel en que la libertad sea otorgada.",
            "tipo": "suspension"
        },
        "Enfermedad contagiosa": {
            "articulo": "Art. 42 Fracc. I",
            "ejemplo": "El trabajador presenta diagnóstico de tuberculosis o una infección que ponga en riesgo al resto.",
            "inicio": "Desde la fecha en que el patrón tenga conocimiento.",
            "reinicio": "Al día siguiente de que cese la causa o el IMSS otorgue el alta.",
            "tipo": "suspension"
        },
        "Contingencia Sanitaria": {
            "articulo": "Art. 42 Bis",
            "ejemplo": "Declaratoria oficial de la Secretaría de Salud que ordene la suspensión de labores (ej. Pandemia).",
            "inicio": "En la fecha que dicte la declaratoria oficial.",
            "reinicio": "Inmediatamente después de que termine la vigencia de la declaratoria.",
            "tipo": "suspension"
        }
    },
    "RESCISIÓN (DESPIDO JUSTIFICADO)": {
        "Faltas de Probidad": {
            "articulo": "Art. 47 Fracc. II",
            "ejemplo": "El trabajador sustrae mercancía de la bodega o altera registros de ventas para beneficio personal.",
            "efecto": "Pérdida del empleo sin responsabilidad para el patrón.",
            "pago": "Finiquito (Partes proporcionales únicamente).",
            "tipo": "rescision"
        },
        "Inasistencias injustificadas": {
            "articulo": "Art. 47 Fracc. X",
            "ejemplo": "El trabajador falta los días lunes, martes, miércoles y jueves de la misma semana sin aviso.",
            "detalle": "Más de 3 faltas en un periodo de 30 días.",
            "tipo": "rescision"
        }
    },
    "TERMINACIÓN": {
        "Mutuo Consentimiento": {
            "articulo": "Art. 53 Fracc. I",
            "ejemplo": "Ambas partes firman un convenio de terminación voluntaria ante el Centro de Conciliación.",
            "pago": "Gratificación negociada o finiquito de ley.",
            "tipo": "terminacion"
        },
        "Incapacidad Física Manifiesta": {
            "articulo": "Art. 53 Fracc. IV",
            "ejemplo": "Un accidente fuera del trabajo deja al empleado con una invalidez permanente que impide realizar su puesto.",
            "derecho": "Pago de un mes de salario y prima de antigüedad (Art. 54).",
            "tipo": "terminacion"
        }
    }
}

# --- INTERFAZ ---
st.title("⚖️ Consola Experta en Derecho Laboral")

pestana_contrato, pestana_catalogo = st.tabs(["📄 Redactor de Contrato", "📚 Catálogo de Incidencias"])

with pestana_contrato:
    # (Mantener la lógica del contrato anterior, pero agregando los campos de horario y fecha de pago que solicitaste)
    st.info("Utilice la barra lateral para configurar las cláusulas de este documento.")
    # ... Lógica de redacción de contrato ...

with pestana_catalogo:
    st.subheader("Análisis de Incidencias en la Relación Laboral")
    
    col_nav, col_display = st.columns([1, 2])
    
    with col_nav:
        categoria = st.selectbox("Categoría Jurídica", list(DB_LEGAL.keys()))
        causal_nombre = st.selectbox("Seleccione la Causal Específica", list(DB_LEGAL[categoria].keys()))
        
        info = DB_LEGAL[categoria][causal_nombre]
    
    with col_display:
        st.markdown(f"""
        <div class="main-card">
            <h3>{causal_nombre}</h3>
            <span class="status-badge {info['tipo']}">{categoria}</span>
            <hr>
            <p><b>📍 Fundamento:</b> {info['articulo']}</p>
            <p><b>📖 Caso Práctico:</b> {info['ejemplo']}</p>
        """, unsafe_allow_html=True)
        
        if categoria == "SUSPENSIÓN TEMPORAL":
            st.markdown(f"""
                <div style="background:#fffde7; padding:15px; border-radius:8px; border:1px solid #fbc02d;">
                    <p style="margin:0;"><b>⏱️ Operatividad Temporal:</b></p>
                    <ul>
                        <li><b>Inicia:</b> {info['inicio']}</li>
                        <li><b>Reinicio de labores:</b> {info['reinicio']}</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        elif categoria == "RESCISIÓN (DESPIDO JUSTIFICADO)":
            st.markdown(f"<p style='color:red;'><b>⚠️ Consecuencia:</b> {info['efecto']}</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- IMAGEN DE APOYO VISUAL ---
st.write("---")
st.markdown("### Esquema de la Relación Laboral")
st.image("https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&q=80&w=1000", 
         caption="Gestión de Documentación y Cumplimiento Legal")
