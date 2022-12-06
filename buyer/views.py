from http.client import HTTPResponse
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from mysite import settings
from .models import Buyer

# Create your views here.


def login(request):
    return render(request, 'login.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration_form.html')
    else:
        if request.POST['password'] == request.POST['cpassword']:
            password = request.POST['password']
            global user_data
            user_data = {
                'first_name': request.POST['firstname'],
                'last_name': request.POST['lastname'],
                'email': request.POST['email'],
                'password': request.POST['password'],
                're_password': request.POST['cpassword'],
            }
            if len(password) >= 8:
                special_char = False
                numbers = False
                upper_case = False
                lower_case = False
                for i in password:
                    if i in '!@#$%^&*':
                        special_char = True
                    if i in '0123456789':
                        numbers = True
                    if 97 <= ord(i) <= 122:
                        lower_case = True
                    if 65 <= ord(i) <= 90:
                        upper_case = True
                if lower_case and upper_case and special_char and numbers:
                    global c_otp
                    c_otp = random.randint(1000, 9999)
                    subject = "Registration At Blogspot"
                    message = f"Your OTP is {c_otp}."
                    from_email = settings.EMAIL_HOST_USER
                    send_mail(subject, message, from_email,
                              [request.POST['email']])
                    return render(request, 'otp.html', {'msg': 'Check Your Inbox!!'})
                else:
                    return render(request, 'registration_form.html', {'msg': 'akjsdklasjd'})
        else:
            return render(request, 'registration_form.html', {'msg': 'Both passwords are not same!!'})


def otp(request):
    if request.method == 'POST':
        if c_otp == int(request.POST['uotp']):
            Buyer.objects.create(
                firstname=user_data['first_name'],
                lastname=user_data['last_name'],
                email=user_data['email'],
                password=user_data['password'],
                cpassword=user_data['re_password'])
            return render(request, 'registration_form.html', {'msg': 'Account Successfully created!!'})
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def faqs(request):
    return render(request, 'faqs.html')


def checkout(request):
    return render(request, 'checkout.html')


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


def home(request):
    return HttpResponse('this is HOME page')
