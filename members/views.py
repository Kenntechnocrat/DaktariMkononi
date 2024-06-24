from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import DoctorCreationForm
from .forms import RegisterUserForm
from .forms import RegisterDocForm
from django.core.mail import send_mail

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            ...
            messages.success(request, "Password or username InValid")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Sign Out Successful")
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, "Sign Up Completed!")
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form':form,
    })

#doctor

def login_doctor(request):
    if request.method == "POST":
        license_no = request.POST['license_no']
        password = request.POST['password']
        user = authenticate(request, license_no=license_no, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            ...
            messages.success(request, "Password or License no. invalid")
            return redirect('login_doctor')
    else:
        return render(request, 'authenticate/login_doctor.html', {})

def register_doctor(request):
    if request.method == "POST":
        form = RegisterDocForm(request.POST)
        if form.is_valid():
            form.save()
            license_no = form.cleaned_data['license_no']
            password = form.cleaned_data['password1']
            user = authenticate(license_no=license_no, password = password)
            login(request, user)
            messages.success(request, "Sign Up Completed!")
            return redirect('index')
    else:
        form = RegisterDocForm()
    return render(request, 'authenticate/register_doctor.html', {
        'form':form,
    })

def logout_doctor(request):
    logout(request)
    messages.success(request, "Sign Out Successful")
    return redirect('index')