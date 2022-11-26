from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User, auth
from estate.token import account_activation_token
from django.core.mail import EmailMessage
from tola.helpers import send_forget_password_mail
from ppty.models import Profile
import uuid


# Create your views here.

def activate(request, uidb64, token):
     return redirect('homepage')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "Protocol": 'https' if request.is_secure() else 'http'
    }
    )

    email = EmailMessage(mail_subject, to={to_email})
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to your email <b> {to_email}</b> inbox and click on \ received activation link to confirm and complete the registration. <b>Note:</> Check your spam folder.')

    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly')

def login(request):
    if request.method== 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = auth.authenticate(username=username,password=password)

         if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
         else:
             messages.info(request,'invalid credentials')
             return redirect('login')

    else:
        return render(request,'login-register.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1,)
                user.save();
                activateEmail(request, user, forms.cleaned_data.get('email'))
                print(request,'Your account has been created successfully!')
                return redirect('login')
                
                
        else:
            messages.info(request,'password doesn`t match')
            return redirect('register')
        return redirect("/")

    else:
        return render(request,'login-register.html')



    return render(request,'login-register.html')

def logout(request):
        auth.logout(request)
        return redirect('/')

def dashboard(request):
    total_users = User.objects.all().count()
    return render(request, 'dashboard.html', {'name':'dashboard', 'total_users' : total_users})

def profile(request):
    return render(request, 'profile.html', {'name':'profile'})

def buy_property(request):
    return render(request, 'Buy_property.html', {'name':'buy_property'})

    
def add_properties(request):
    return render(request, 'add-properties.html', {'name':'add_properties'})

def Mortgage_property(request):
    return render(request, 'Mortgage_property.html', {'name':'Mortgage_property'})

def Rent_property(request):
    return render(request, 'Rent_property.html', {'name':'Rent_property'})

def Sale_property(request):
    return render(request, 'Sale_property.html', {'name':'Sale_property'})

def setting(request):
    return render(request, 'setting.html', {'name':'setting'})

def change_password(request , token):
    context = {}
    try:
        profile_obj = Profile.objects.gets(forget_password_token = token)

        print(profile_obj)


    except Exception as e:
        print(e)
    return render(request , 'change_password.html')











    return render(request, 'change_password.html', {'name':'change_password'})


import uuid
def forget_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('forget_password')

            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('forget_password')




    except Exception as e:
        print(e)
    return render(request, 'forget_password.html', {'name':'forget_password'})