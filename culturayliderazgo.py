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
st.title("Evolución Empresarial en la Era de la IA")
st.Header("Tablero de Control: Cultura y Liderazgo Digital")

# Filtrar datos por capacidad
capacidades = df["Capacidad"].unique()

for capacidad in capacidades:
    # Sección de la capacidad
    st.header(f"Capacidad: {capacidad}")
    df_cap = df[df["Capacidad"] == capacidad]
    
    # Tabla con información de OKRs y KPIs
    st.subheader(f"Resumen de Metas para {capacidad}")
    st.table(df_cap[["Meta", "OKR", "KPI", "Valor Actual", "Meta Objetivo"]])
    
    # Gráficos por meta
    st.subheader(f"Gráficos por Meta - {capacidad}")
    for _, row in df_cap.iterrows():
        st.markdown(f"**Meta:** {row['Meta']}")
        st.markdown(f"- **OKR:** {row['OKR']}")
        st.markdown(f"- **KPI:** {row['KPI']}")
        
        # Crear gráfico para la meta
        fig, ax = plt.subplots()
        ax.bar(["Actual", "Meta"], [row["Valor Actual"], row["Meta Objetivo"]], color=["blue", "green"])
        ax.set_title(f"Progreso de la Meta: {row['Meta']}")
        ax.set_ylabel("Valores")
        st.pyplot(fig)

# Instrucciones finales
st.markdown("Este tablero permite visualizar el progreso de cada meta individualmente, junto con sus OKRs y KPIs.")
