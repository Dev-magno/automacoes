import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Carregar os dados
df = pd.read_csv('faturamento.csv')

# Título
st.title('Dashboard de Faturamento Mensal')

# Filtro de Meses
meses = st.multiselect('Selecione os meses para visualizar:',
                       df['Mês'].tolist(), default=df['Mês'].tolist())

# Filtrar os dados
df_filtado = df[df['Mês'].isin(meses)]

# Mostrar tabela
st.subheader('Tabela de Faturamento')
st.dataframe(df_filtado)

# Gráfico de linha
st.subheader('Gráfico de Faturamento')
fig, ax = plt.subplots()
ax.plot(df_filtado['Mês'], df_filtado['Faturamento'], marker='o', color='blue')
ax.set_xlabel('Mês')
ax.set_ylabel('Faturamento (R$)')
ax.set_title('Evolução do Faturamento')
plt.xticks(rotation=45)
st.pyplot(fig)
