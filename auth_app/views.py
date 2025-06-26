from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def signup_view(request):
    template_name = 'auth_app/signup.html'
    form =UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    
    context={'form':form}
    return render(request,template_name,context)

def login_view(request):
    template_name = 'auth_app/login.html'
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_url')
    context={}
    return render(request,template_name,context)

def logout_view(request):
    logout(request)
    return redirect('login_url')
