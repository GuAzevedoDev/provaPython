import pandas as pd
import plotly.express as px
import streamlit as st

ARQUIVO = "censo_1872.xlsx"
FONTE = "https://basedosdados.org/"


@st.cache_data
def carregar_dados():
    df = pd.read_excel(ARQUIVO, engine="openpyxl")
    return df.drop_duplicates()


def calcular_totais(df):
    return {
        "Homens livres": df["homens_livres"].sum(),
        "Homens escravizados": df["homens_escravizados"].sum(),
        "Mulheres livres": df["mulheres_livres"].sum(),
        "Mulheres escravizadas": df["mulheres_escravizadas"].sum(),
    }


def montar_tabela(totais):
    total_homens = totais["Homens livres"] + totais["Homens escravizados"]
    total_mulheres = totais["Mulheres livres"] + totais["Mulheres escravizadas"]
    linhas = []
    for grupo, total in totais.items():
        base = total_homens if grupo.startswith("Homens") else total_mulheres
        linhas.append(
            {
                "Grupo": grupo,
                "Total de pessoas": int(total),
                "Percentual (%)": round(total / base * 100, 2),
            }
        )
    return pd.DataFrame(linhas)


df = carregar_dados()
tabela = montar_tabela(calcular_totais(df))

st.title("Censo de 1872: população livre e escravizada")

visualizacao = st.sidebar.radio("Visualização", ["Tabela", "Gráficos"])

if visualizacao == "Tabela":
    st.header("Totais e percentuais por grupo")
    st.dataframe(tabela, width="stretch", hide_index=True)
    st.caption("O percentual de cada grupo é calculado dentro do próprio sexo.")
else:
    st.header("Percentual de livres e escravizados por sexo")
    homens = tabela[tabela["Grupo"].str.startswith("Homens")]
    mulheres = tabela[tabela["Grupo"].str.startswith("Mulheres")]
    st.plotly_chart(
        px.pie(homens, names="Grupo", values="Total de pessoas", title="Homens"),
        width="stretch",
    )
    st.plotly_chart(
        px.pie(mulheres, names="Grupo", values="Total de pessoas", title="Mulheres"),
        width="stretch",
    )

st.markdown(f"Fonte dos dados: [{FONTE}]({FONTE})")
