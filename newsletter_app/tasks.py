from Newsletters.celery import app
from django.core.mail import send_mail

@app.task(name='send autor email')
def send_email_suscriptor(email):
        send_mail(
                    'Correo de suscripción',
                    'Este es el contenido que hay por tu suscripción',
                    'djangoTes@gmail.com',
                    [email],
                    fail_silently=False,
                )