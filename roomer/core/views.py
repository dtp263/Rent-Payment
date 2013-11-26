from django.shortcuts import render, redirect
from forms import *

from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from django.contrib.auth.forms import AuthenticationForm
import os


def logoutView(request):
    logout(request)
    return render_to_response('registration/logged_out.html')

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account')
                else:
                    return redirect('index')
        else:
            return render(request, "registration/login.html", {'form':form})
    else:
        LoginForm = AuthenticationForm()
        return render(request, "registration/login.html", {'form':LoginForm})

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
#     return True
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
    user = request.user
    userProfile = user.get_profile()
    if userProfile.islandlord == True:
        return render(request, "landlord/landlord_profile.html", {'user':user, 'profile':userProfile})
    elif userProfile.islandlord == False:
        return render(request, "tenant/tenant_profile.html", {'user':user, 'profile':userProfile})

@login_required
def uploadPropertyPic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

@login_required
def newProperty(request):
    if request.method == 'POST':
        form = PropertyProfileForm(data=request.POST)

        if form.is_valid():
            form.save()
            propertyProfile = create_propertyProfile(form.cleaned_data['title'])
            return propertyProfilePage(request, title=title)
        else:
            return render(request, "core/error.html", {'form':form})
    else:
        profileForm = PropertyProfileForm()
        addressForm = addressTypeForm()
        return render(request, "landlord/add_property.html", {'profileForm':profileForm, 'addressForm':addressForm})


def propertyProfilePage(request, owner=None, title=None):
    if not title == None:
        propertyProfile = propertyProfile.objects.filter(title=title)
        return render(request, "property/property_page.html", {'propertyProfile':propertyProfile})
    else:
        return render(request, "core/error.html")


def registerLandlord(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                )
            #Save user and authenticate
            user.save()
            #Save profile data
            profile = user.get_profile()
            profile.zipcode = form.cleaned_data['zip']
            profile.islandlord = True
            profile.save()
            #Log the user in
            login(request, user)
            return redirect('account')
    else:
        form = UserProfileCreationForm()
    return render(request, "registration/register.html", {'form': form})

def registerTenant(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            #Save user and authenticate
            form.save()

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            #Save profile data
            profile = user.get_profile()
            profile.zipcode = form.cleaned_data['zip']
            profile.ip_address = request.META['REMOTE_ADDR']
            profile.save()
            #Log the user in
            login(request, user)
            return redirect('account')
    else:
        form = UserProfileCreationForm()

    return render(request, "registration/register.html", {'form': form},)