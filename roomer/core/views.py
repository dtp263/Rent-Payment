from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from forms import *

from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def logoutView(request):
    logout(request)
    return 


def loginView(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_and_login(request, onsuccess='/', onfail='/login/'):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)  

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']): 
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
        return auth_and_login(request)
    else:
        return redirect("/login/")

@login_required(login_url='/login/')
def secured(request):
    return render_to_response("secure.html")


@login_required
def account(request):
    return render(request, 'core/profile.html')

def registerLandlord(request):
    if request.method == 'POST':
        form = LandlordCreationForm(request.POST)
        if form.is_valid():
            #Save user and authenticate
            form.save()

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],

            )
            #Save profile data
            profile = user.get_profile()
            profile.zip = form.cleaned_data['zip']
            profile.save()
            #Log the user in
            login(request, user)
            return redirect('register_done')
    else:
        form = LandlordCreationForm()
    return render(request, "registration/register.html", {'form': form})

def registerTenant(request):
    if request.method == 'POST':
        form = TenantCreationForm(request.POST)
        if form.is_valid():
            #Save user and authenticate
            form.save()

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],

            )
            #Save profile data
            profile = user.get_profile()
            profile.zip = form.cleaned_data['zip']
            profile.save()
            #Log the user in
            login(request, user)
            return redirect('register_done')
    else:
        form = TenantCreationForm()

    return render(request, "registration/register.html", {'form': form},)


def register_done(request):
    return render(request, "registration/register_done.html")