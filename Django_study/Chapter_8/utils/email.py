from django.core.mail import send_mail


def send_email(subject, message, from_email, to_email):
    to_email = to_email if isinstance(to_email, list) else [to_email,]
    send_mail(subject, message, from_email, to_email)
