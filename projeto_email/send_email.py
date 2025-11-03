import smtplib
import email.message


# Função enviar email
def enviar_email():
    corpo_email = """
    <p>Fala, aí!</p>
    <p>Segue email automático do projeto de automação básico.</p>
    """

    # Criar mensagem com assunto, remetente, destinatário e senha
    msg = email.message.Message()
    msg['Subject'] = 'Assunto'
    msg['Form'] = 'magnolopes1212@gmail.com'
    msg['To'] = 'marcelofiquene@hotmail.com'
    password = 'ujwe httq dkby tgvy'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Crendenciais
    s.login(msg['Form'], password)
    s.sendmail(msg['Form'], msg['To'], msg.as_string().encode('utf-8'))


enviar_email()
print('Email enviado')
