from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'Portfolio send -> '+message_name,  # subject
            message,  # message
            settings.EMAIL_HOST_USER,  # form email
            [message_email, 'example2@gmail.com'],  # To Email
            fail_silently=False)

        return render(request, 'home.html')
    else:
        return render(request, 'home.html', context={})
