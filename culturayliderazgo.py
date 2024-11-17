import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos simulados organizados por capacidades
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

# Generar datos simulados de progreso mensual para cada meta
def generate_progress_data(actual, target, months=10):
    progress = np.linspace(actual, target, months)
    return progress

# Crear DataFrame
df = pd.DataFrame(data)

# Generar datos mensuales para cada meta
df["Progreso Mensual"] = df.apply(
    lambda row: generate_progress_data(row["Valor Actual"], row["Meta Objetivo"]), axis=1
)

# Título general
st.title("Tablero de Control: Cultura y Liderazgo Digital")

# Filtrar datos por capacidad
capacidades = df["Capacidad"].unique()

for capacidad in capacidades:
    # Sección de la capacidad
    st.header(f"Capacidad: {capacidad}")
    df_cap = df[df["Capacidad"] == capacidad]
    
    # Tabla con información de OKRs y KPIs
    st.subheader(f"Resumen de Metas para {capacidad}")
    st.table(df_cap[["Meta", "OKR", "KPI", "Valor Actual", "Meta Objetivo"]])
    
    # Gráficos por meta con datos temporales
    st.subheader(f"Gráficos por Meta - {capacidad}")
    for i, row in df_cap.iterrows():
        st.markdown(f"**Meta:** {row['Meta']}")
        st.markdown(f"- **OKR:** {row['OKR']}")
        st.markdown(f"- **KPI:** {row['KPI']}")
        
        # Selección de tipo de gráfico
        if i % 3 == 0:
            # Gráfico de líneas para progreso mensual
            fig, ax = plt.subplots()
            ax.plot(range(1, 11), row["Progreso Mensual"], marker='o', label="Progreso", color="blue")
            ax.axhline(row["Meta Objetivo"], color="green", linestyle="--", label="Meta Objetivo")
            ax.set_title(f"Evolución del Progreso: {row['Meta']}")
            ax.set_xlabel("Mes")
            ax.set_ylabel("Progreso")
            ax.legend()
            st.pyplot(fig)
        elif i % 3 == 1:
            # Gráfico de barras acumulativas
            fig, ax = plt.subplots()
            ax.bar(range(1, 11), row["Progreso Mensual"], color="orange", label="Progreso")
            ax.axhline(row["Meta Objetivo"], color="green", linestyle="--", label="Meta Objetivo")
            ax.set_title(f"Progreso Acumulativo: {row['Meta']}")
            ax.set_xlabel("Mes")
            ax.set_ylabel("Progreso")
            ax.legend()
            st.pyplot(fig)
        else:
            # Gráfico de áreas apiladas
            actual = row["Valor Actual"]
            remaining = row["Meta Objetivo"] - actual
            fig, ax = plt.subplots()
            ax.barh(["Progreso", "Faltante"], [actual, remaining], color=["blue", "red"])
            ax.set_title(f"Progreso y Faltante: {row['Meta']}")
            ax.set_xlabel("Valores")
            st.pyplot(fig)

# Instrucciones finales
st.markdown("Este tablero incluye gráficos con datos temporales que muestran la evolución del progreso para cada meta, usando líneas, barras acumulativas y áreas apiladas.")

