# 🖱️ Automação de Preenchimento de Formulário com PyAutoGUI

Este script automatiza o processo de abrir um navegador, acessar o site [Desec Security](https://desecsecurity.com/), navegar até a seção "Fale Conosco" e preencher um formulário de contato com informações pré-definidas usando a biblioteca `pyautogui`.

## 📋 Funcionalidades

- Abre o navegador clicando em uma posição específica da tela.
- Digita a URL do site e acessa a página.
- Navega até o menu "Fale Conosco".
- Rola a página para visualizar o formulário.
- Seleciona o assunto "Treinamento".
- Preenche os campos do formulário com:
  - Nome
  - E-mail
  - Telefone
  - Cargo
  - Mensagem personalizada
- Envia o formulário automaticamente.

## 🛠️ Requisitos

- Python 3.x
- Biblioteca [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

### Instalação

```bash
pip install pyautogui
```

## ⚠️ Observações

- As coordenadas de tela (x, y) são específicas para a resolução e layout do sistema onde o script foi desenvolvido. Elas podem precisar ser ajustadas para funcionar corretamente em outros dispositivos.

- O script não verifica se os elementos estão visíveis ou carregados, portanto é sensível ao tempo de carregamento da página.

- Certifique-se de que o navegador esteja na posição esperada e que nenhuma janela esteja obstruindo os elementos clicáveis.

## 📌 Uso

O uso será de acordo com seu sistema operacional. Python3 é usado no Ubuntu

```
python3 nome_do_arquivo.py
```
📎 Para adaptar o script a diferentes resoluções ou sites, você pode usar a função pyautogui.position() para capturar coordenadas manualmente.