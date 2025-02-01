import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Carregar os dados
df = pd.read_csv("finances.csv")
df["Mês"] = df["Data"].apply(lambda x: "-".join(x.split("-")[:-1]))
df["Data"] = pd.to_datetime(df["Data"])
df["Data"] = df["Data"].apply(lambda x: x.date())
df = df[df["Categoria"] != "Receitas"]
df["Valor"] = df["Valor"].apply(lambda x: round(x, 2))

# Adicionar coluna oculta para contar o número de transações por categoria
df["Contagem"] = 1

# Agrupar os dados
df = df.groupby(["Data", "Mês", "Categoria"]).agg({"Valor": "sum", "Contagem": "sum"}).reset_index()

def filter_data(df, mes, selected_categories):
    df_filtered = df[df['Mês'] == mes]
    if selected_categories:
        df_filtered = df_filtered[df_filtered['Categoria'].isin(selected_categories)]
    return df_filtered

# Título do Dashboard
st.title("Dashboard de Finanças Pessoais")

# Filtros de data
st.sidebar.header("Filtros")

# Definir intervalo de data
mes = st.sidebar.selectbox("Mês", df["Mês"].unique())

# Filtro de categoria
categories = df["Categoria"].unique().tolist()
selected_categories = st.sidebar.multiselect("Filtrar por Categorias", categories, default=categories)

df_filtered = filter_data(df, mes, selected_categories)

# ====================
c1, c2 = st.columns([0.6, 0.4])

# Mostrar tabela de finanças filtradas
c1.dataframe(df_filtered)

# Gráfico de barras dos gastos por categoria
category_distribution = df_filtered.groupby("Categoria").agg({"Valor": "sum", "Contagem": "sum"}).reset_index()
fig_bar = px.bar(category_distribution, x='Categoria', y='Valor', 
                 title='Gastos por Categoria', text='Valor')
fig_bar.update_layout(xaxis_title='Categoria', yaxis_title='Valor')
c1.plotly_chart(fig_bar, use_container_width=True)

# Distribuição de Categorias
fig_pie = px.pie(category_distribution, values='Contagem', names='Categoria', 
                 title='Distribuição por Categoria', hole=0.3)
c2.plotly_chart(fig_pie, use_container_width=True)

# Gráfico de linha da evolução dos gastos ao longo do tempo
fig_line = px.line(df_filtered, x='Data', y='Valor', color='Categoria', 
                   title='Evolução dos Gastos ao Longo do Tempo')
fig_line.update_layout(xaxis_title='Data', yaxis_title='Valor')
st.plotly_chart(fig_line, use_container_width=True)

# Gráfico de barras da contagem de transações por categoria
fig_count = px.bar(category_distribution, x='Categoria', y='Contagem', 
                   title='Contagem de Transações por Categoria', text='Contagem')
fig_count.update_layout(xaxis_title='Categoria', yaxis_title='Contagem')
st.plotly_chart(fig_count, use_container_width=True)