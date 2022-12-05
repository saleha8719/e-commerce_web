from http.client import HTTPResponse
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from mysite import settings

# Create your views here.


def login(request):
    return render(request, 'login.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration_form.html')
    else:
        global user_data
        user_data = {
            'first_name': request.POST['firstName'],
            'last_name': request.POST['lastName'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            're_password': request.POST['cpassword'],
        }
        if user_data['password'] == user_data['re_password']:
            global c_otp
            c_otp = random.randint(1000, 9999)
            message = f'Hi, your OTP is {c_otp}'
            subject = 'Carpolling Registration,'
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, [user_data['email']])
            return render(request, 'otp.html', {'msg': 'Check Your MailBox'})
        else:
            return render(request, 'registration_form.html', {'msg': 'Passwords Does Not Match'})


def otp(request):
    return render(request, 'otp.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def faqs(request):
    return render(request, 'faqs.html')


def checkout(request):
    return render(request, 'checkout.html')


def help(request):
    return render(request, 'help.html')


def icons(request):
    return render(request, 'icons.html')


def index(request):
    return render(request, 'index.html')


def payment(request):
    return render(request, 'payment.html')


def privacy(request):
    return render(request, 'privacy.html')


def product(request):
    return render(request, 'product.html')


def product2(request):
    return render(request, 'product2.html')


def single(request):
    return render(request, 'single.html')


def single2(request):
    return render(request, 'single2.html')


def terms(request):
    return render(request, 'terms.html')


def typography(request):
    return render(request, 'typography.html')


def home(request):
    return HttpResponse('this is HOME page')
