from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives

def enviar_email(assunto, corpo, destinatario):
    send_mail(
        assunto,
        corpo,
        settings.DEFAULT_FROM_EMAIL,
        [destinatario],
        fail_silently=True,
    )

def enviar_email_html(assunto, corpo, destinatario, html):
    subject = assunto
    from_email = settings.DEFAULT_FROM_EMAIL
    to = destinatario
    text_content = corpo
    html_content = html

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def enviar_email_com_anexo(assunto, corpo, destinatario, anexo):
    email = EmailMessage(
        assunto,
        corpo,
        settings.DEFAULT_FROM_EMAIL,
        [destinatario],
    )
    email.attach_file(anexo)
    email.send()
