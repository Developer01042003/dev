from django.core.mail import send_mail
import uuid



def send_forgot_password_email(email,token):
    subject = "RESET PASSWORD LINK"
    message = f'hii,click the link to reset your password'

