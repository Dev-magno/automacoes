# 📧 Envio de E-mail Automático com Python (Gmail)

Este script Python permite enviar e-mails automaticamente usando a biblioteca `smtplib` e o servidor SMTP do Gmail. Ele é útil para automações simples como notificações, relatórios ou mensagens programadas.

## 🧪 Pré-requisitos

- Conta Gmail válida
- Python 3 instalado
- Acesso à internet
- Verificação em duas etapas ativada na conta Gmail
- Senha de app gerada para autenticação

## 📜 Como funciona

O script cria uma mensagem HTML e a envia para o destinatário usando o servidor SMTP do Gmail (`smtp.gmail.com`) na porta 587 com TLS.

### 📌 Estrutura do código

- Define o corpo do e-mail em HTML
- Cria a mensagem com remetente, destinatário e assunto
- Usa `smtplib` para autenticar e enviar o e-mail

---

## 🔐 Como ativar a verificação em duas etapas e gerar senha de app

### 1. Ativar verificação em duas etapas

1. Acesse [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Na seção **“Como você faz login no Google”**, clique em **Verificação em duas etapas**
3. Siga as instruções para ativar (você precisará de um celular para receber o código)

### 2. Gerar senha de app

> ⚠️ Essa opção só aparece após ativar a verificação em duas etapas

1. Acesse [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Faça login, se necessário
3. Em **Selecionar app**, escolha **Outro (personalizado)** e digite um nome (ex: `script-email`)
4. Clique em **Gerar**
5. Copie a senha gerada (16 caracteres) e use no lugar da sua senha normal no script

---

## 🧪 Exemplo de uso

```python
msg['Form'] = 'seuemail@gmail.com'
msg['To'] = 'destinatario@gmail.com'
password = 'sua_senha_de_app_gerada'