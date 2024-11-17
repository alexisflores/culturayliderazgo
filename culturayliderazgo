import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos organizados por capacidades
data = {
    "Capacidad": ["Sensing", "Sensing", "Seizing", "Seizing", "Configuring", "Configuring"],
    "Meta": [
        "Monitoreo continuo de tendencias",
        "Ideación colaborativa interna",
        "Capacitación avanzada en IA",
        "Equipos multifuncionales en IA",
        "Rediseñar procesos con IA",
        "Implementar incentivos vinculados"
    ],
    "OKR": [
        "Identificar 10 tendencias/anual",
        "Incrementar ideas generadas 40%",
        "Capacitar al 80% líderes/anual",
        "Crear 5 equipos multifuncionales/6 meses",
        "Automatizar 3 procesos clave/2 años",
        "Aumentar productividad en 15%/áreas digitalizadas"
    ],
    "KPI": [
        "Tendencias identificadas",
        "Total de ideas generadas",
        "Líderes capacitados (%)",
        "Equipos creados",
        "Procesos automatizados (%)",
        "Empleados incentivados (%)"
    ],
    "Valor Actual": [8, 120, 75, 4, 50, 10],
    "Meta Objetivo": [10, 150, 80, 5, 100, 15]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Título general
st.title("Tablero de Control: Cultura y Liderazgo Digital")

# Filtrar datos por capacidad
capacidades = df["Capacidad"].unique()

for capacidad in capacidades:
    # Sección de la capacidad
    st.header(f"Capacidad: {capacidad}")
    df_cap = df[df["Capacidad"] == capacidad]
    
    # Mostrar tabla con información de OKRs y KPIs
    st.subheader(f"Resumen de Metas y Progresos para {capacidad}")
    st.table(df_cap[["Meta", "OKR", "KPI", "Valor Actual", "Meta Objetivo"]])
    
    # Gráfico de barras: OKR
    st.subheader(f"Progreso de OKRs - {capacidad}")
    fig_okr, ax_okr = plt.subplots()
    ax_okr.bar(df_cap["Meta"], df_cap["Valor Actual"], label="Actual", color="blue")
    ax_okr.bar(df_cap["Meta"], df_cap["Meta Objetivo"], label="Meta", alpha=0.5, color="green")
    ax_okr.set_title(f"OKR Actual vs Meta Objetivo para {capacidad}")
    ax_okr.set_ylabel("Valores")
    ax_okr.tick_params(axis="x", rotation=45)
    ax_okr.legend()
    st.pyplot(fig_okr)
    
    # Gráficos individuales por KPI
    st.subheader(f"Progreso de KPIs - {capacidad}")
    for _, row in df_cap.iterrows():
        fig_kpi, ax_kpi = plt.subplots()
        ax_kpi.bar(["Actual", "Meta"], [row["Valor Actual"], row["Meta Objetivo"]], color=["blue", "green"])
        ax_kpi.set_title(f"KPI: {row['KPI']}")
        ax_kpi.set_ylabel("Valores")
        st.pyplot(fig_kpi)

# Instrucciones finales
st.markdown("Este tablero permite monitorear el progreso de los OKRs y KPIs por capacidad, ayudando a evaluar el avance hacia los objetivos de transformación digital.")
