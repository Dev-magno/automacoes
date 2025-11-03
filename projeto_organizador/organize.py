import os
import shutil
from datetime import datetime


# Pasta com os arquivos a organizar
origem = '/home/magno/Downloads'
destino = 'organizados'


# Extensões por tipo
tipos = {
    'pdf': ['.pdf'],
    'excel': ['.xls', '.xlsx'],
    'imagens': ['.jpg', '.jpeg', '.png']
}


# Função para organizar
def organizar_arquivos():
    for arquivo in os.listdir(origem):
        caminho_arquivo = os.path.join(origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            ext = os.path.splitext(arquivo)[1].lower()
            tipo = None

            # Identifica o tipo
            for chave, extensoes in tipos.items():
                if ext in extensoes:
                    tipo = chave
                    break

            if tipo:
                # Data da criação
                timestamp = os.path.getatime(caminho_arquivo)
                data = datetime.fromtimestamp(timestamp)
                pasta_mes = data.strftime('%Y-%M')

                # Cria pasta destino
                destino_final = os.path.join(destino, tipo, pasta_mes)
                os.makedirs(destino_final, exist_ok=True)

                # Mover arquivo
                shutil.move(caminho_arquivo, os.path.join(
                    destino_final, arquivo))
                print(f'Movido: {arquivo} -> {destino_final}')


organizar_arquivos()
