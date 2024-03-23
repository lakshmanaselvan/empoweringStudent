from django.shortcuts import get_object_or_404, render, redirect
from .models import Registration
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
import random
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .forms import StaffRegistrationForm
from .models import StaffRegistration
from .forms import studentLoginForm
from .forms import staffLoginForm
# Create your views here.


def staffRegistration(request):
    form = StaffRegistrationForm
    if request.method == 'POST':
        email = request.POST.get('email')

        if not email.endswith('@tec-edu.in'):
            msg = "Invalid email format. Please use an email ending with @tec-edu.in"
            return render(request, "staffRegistration.html", {'msg': msg, 'form':form})
        
        if StaffRegistration.objects.filter(email = email).exists():
            msg = "Email already exists"
            return render(request, "staffRegistration.html", {'msg':msg})
        else:
            username = request.POST.get('name')
            password = request.POST.get('password')
            domain_name = get_current_site(request).domain
            token = str(random.random()).split('.')[1]
            user = StaffRegistration(name = username, email = email,password = password, token = token )
            user.save()
            link = f'http://{domain_name}/account/verify/{token}'
            send_mail(
                'Email Verification',
                f'Please click {link} to verify your mail',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            msg = "The mail has been sent!"
            return render(request, 'success.html', {'msg':msg})
    return render(request, 'staffRegistration.html', {'form':form})

def registration(request):
    form = RegistrationForm
    if request.method == 'POST':
        email = request.POST.get('email')
        if Registration.objects.filter(email= email).exists():
            msg = "Email already exists"
            return render(request, "registration.html", {'msg':msg, 'form':form})
        else:
            username = request.POST.get('name')
            password = request.POST.get('password')
            # http://my-domain.com/verification-token
            domain_name = get_current_site(request).domain
            token = str(random.random()).split('.')[1]
            user = Registration(name = username, email = email, password = password, token = token)
            user.save()
            link = f'http://{domain_name}/account/verify/{token}'
            send_mail(
                'Email Verification',
                f'Please click {link} to verify your mail',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
                )
            msg = "The mail has been sent!"
            return render(request, 'success.html', {'msg':msg})
    return render(request, "registration.html", {'form':form})

def verify(request, token):
    try:
        user = get_object_or_404(Registration, token=token)
        if not user.is_verified:
            user.is_verified = True
            user.save()
            msg = 'Your email has been verified successfully.'
            return render(request, 'success.html', {'msg':msg})
        else:
            msg = 'Your email is already verified.'
            return render(request, 'success.html', {'msg':msg})
    except Exception as e:
        msg = str(e)
    return render(request, 'registration.html', {'msg': msg})

def login(request):
    form = studentLoginForm
    if request.method == "POST":
        email = request.POST['email']
        if not email.endswith('@gmail.com'):
            msg = "Invalid email format. Please use an email ending with @gmail.com"
            return render(request, "staffLogin.html", {'msg': msg, 'form':form})
        password = request.POST['password']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_verified:
                auth_login(request, user)
                current_domain = get_current_site(request).domain
                redirect_url = f"http://{current_domain}/events/"
                return redirect(redirect_url)
        else:
            msg = 'Email & password are invalid or email not verified successful'
            return render(request, 'login.html', {'msg':msg, 'form':form})
    return render(request, 'login.html', {'form':form})

def staffLogin(request):
    form = staffLoginForm
    if request.method == "POST":
        email = request.POST['email']
        if not email.endswith('@tec-edu.in'):
            msg = "Invalid email format. Please use an email ending with @tec-edu.in"
            return render(request, "staffLogin.html", {'msg': msg, 'form':form})
        password = request.POST['password']
        user = authenticate(request, email=email, password = password)
        if user is not None:
            if user.is_verified:
                auth_login(request, user)
                current_domain = get_current_site(request).domain
                redirect_url = f"http://{current_domain}/events/"
                return redirect(redirect_url)
        else:
            msg = 'Email & password are invalid or email not verified successful'
            return render(request, 'staffLogin.html', {'msg':msg, 'form':form})
    return render(request, 'staffLogin.html', {'form':form})