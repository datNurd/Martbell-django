from django.shortcuts import render
from .forms import MerchantProfileForm, MerchantForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        merchant_form = MerchantForm(data=request.POST)
        merchant_profile_form = MerchantProfileForm(data=request.POST)

        if merchant_form.is_valid() and merchant_profile_form.is_valid():
            user = merchant_form.save()
            user.set_password(user.password)
            user.save()
            profile = merchant_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print merchant_form.errors, merchant_profile_form.errors
    else:
        merchant_form = MerchantForm()
        merchant_profile_form = MerchantProfileForm()
    return render(request,'merchant/register.html',{'merchant_form':merchant_form,'merchant_profile_form':merchant_profile_form,'registered':registered})

def login_merchant(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/merchant/pannel/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid login details. Please relogin")

    else:
        return render(request,'merchant/login.html',{})

@login_required
def logout_merchant(request):
    logout(request)
    return HttpResponseRedirect('/merchant/login/')

@login_required
def pannel(request):
    return HttpResponse("<h1>You are viewing this because you are logged in.</h1><br/><a href='/merchant/logout/'>Logout</a>")
