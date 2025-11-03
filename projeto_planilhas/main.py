import pandas as pd
from openpyxl import Workbook
import os


# Verifica se o caminho existe
caminho = '/home/magno/Atas-2025/clientes.xlsx'

if os.path.exists(caminho):
    # Ler a planilha original
    df = pd.read_excel(caminho)
else:
    print('Arquivo não encontrado', caminho)

# Limpa espaços extras
df.columns = df.columns.str.strip()

# Filtrar clientes com saldo negativo
inadiplentes = df[df['Saldo'] < 0]


# Criar uma nova planilha com os inadiplentes
wb = Workbook()
ws = wb.active
ws.title = 'Inadiplentes'


# Adiconar cabeçalhos
ws.append(['Nome', 'Email', 'Saldo'])


# Adicionar dados
for _, row in inadiplentes.iterrows():
    ws.append([row['Nome'], row['Email'], row['Saldo']])


# Salvar o novo arquivo
wb.save('relatorio_inadiplentes.xlsx')

print("Relatório gerado com sucesso!")
