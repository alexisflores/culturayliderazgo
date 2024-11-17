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
st.markdown(
    """
    <style>
    .title-container {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def generate_progress_data(actual, target, months=10):
    progress = np.linspace(actual, target, months)
    return progress
# Crear DataFrame
df = pd.DataFrame(data)
df["Progreso Mensual"] = df.apply(
    lambda row: generate_progress_data(row["Valor Actual"], row["Meta Objetivo"]), axis=1
)

# Título general
#st.title("Evolución Empresarial en la Era de la IA")
st.markdown('<div class="title-container"><h1>Evolución Empresarial en la Era de la IA</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="title-container"><h2>Tablero de Control: Cultura y Liderazgo Digital</h1></div>', unsafe_allow_html=True)
# st.header("Tablero de Control: Cultura y Liderazgo Digital")

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
    for i, row in df_cap.iterrows():
        st.markdown(f"**Meta:** {row['Meta']}")
        st.markdown(f"- **OKR:** {row['OKR']}")
        st.markdown(f"- **KPI:** {row['KPI']}")

        # Alternar tipos de gráficos
        if i % 3 == 0:
            # Gráfico de barras
            fig, ax = plt.subplots()
            ax.bar(["Actual", "Meta"], [row["Valor Actual"], row["Meta Objetivo"]], color=["blue", "green"])
            ax.set_title(f"Progreso de la Meta: {row['Meta']}")
            ax.set_ylabel("Valores")
            st.pyplot(fig)
        elif i % 3 == 1:
            # Gráfico de líneas
            fig, ax = plt.subplots()
            ax.plot(["Actual", "Meta"], [row["Valor Actual"], row["Meta Objetivo"]], marker='o', color="orange")
            ax.set_title(f"Progreso de la Meta: {row['Meta']}")
            ax.set_ylabel("Valores")
            st.pyplot(fig)
        else:
            # Gráfico circular
               # Gráfico de áreas apiladas
            final_value = row["Progreso Mensual"][-1]
            remaining_value = row["Meta Objetivo"] - final_value
            fig, ax = plt.subplots()
            ax.fill_between(
                ["Progreso", "Faltante"],
                [final_value, 0],
                [final_value, remaining_value],
                color=["blue", "red"],
                alpha=0.5,
                label=["Progreso", "Faltante"]
            )
            ax.set_title(f"Progreso y Faltante: {row['Meta']}")
            ax.set_ylabel("Valores")
            ax.legend(["Progreso", "Faltante"])
            st.pyplot(fig)
        # Crear gráfico para la meta
       # Crear gráfico para la meta
        # fig, ax = plt.subplots()
        #ax.bar(["Actual", "Meta"], [row["Valor Actual"], row["Meta Objetivo"]], color=["blue", "green"])
        #ax.set_title(f"Progreso de la Meta: {row['Meta']}")
        #ax.set_ylabel("Valores")
        #st.pyplot(fig)

# Instrucciones finales
st.markdown("Este tablero permite visualizar el progreso de cada meta individualmente, junto con sus OKRs y KPIs.")
