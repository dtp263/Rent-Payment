from django.shortcuts import render, redirect, render_to_response
from forms import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf
from django.db.models import *
from core.models import *
from django.http import HttpResponseRedirect
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

def property_profile(request, property_id):
    propertyProf = get_object_or_404(propertyProfile, id=property_id)
    return render(request, 'property/property_page.html', {'propertyProfile':propertyProf})


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
        properties = propertyProfile.objects.filter(owner=user)
        return render(request, "landlord/landlord_profile.html", {'user':user, 'profile':userProfile, 'properties':properties})
    elif userProfile.islandlord == False:
        return render(request, "tenant/tenant_profile.html", {'user':user, 'profile':userProfile})
    else:
        return render(request, "core/error.html", {'form':propertyForm})




@login_required
def upload_property_pic(request, property_id):
    if request.method == 'POST':
        form = PropertyImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            propertyProf = get_object_or_404(propertyProfile, id=property_id)
            propertyProf.property_image = request.FILES['image']
            propertyProf.save()
            return render_to_response('property/property_page.html', {'propertyProfile':propertyProf})
    else:
        form = PropertyImageUploadForm()
    return render(request, 'landlord/add_property_photo.html', {'form':form})

@login_required
def newProperty(request):
    if request.method == 'POST':
        propertyForm = PropertyProfileForm(data=request.POST)
        if propertyForm.is_valid():
            # propertyProfileObject = propertyProfile.objects.create_propertyProfile(request.user)
            propertyProfileObject = propertyProfile(owner=request.user)
            propertyProfileObject.totalcost = propertyForm.cleaned_data['totalcost']
            propertyProfileObject.title = propertyForm.cleaned_data['title']
            propertyProfileObject.description = propertyForm.cleaned_data['description']
            propertyProfileObject.numberOfbedrooms = propertyForm.cleaned_data['numberOfbedrooms']
            propertyProfileObject.state = propertyForm.cleaned_data['state']
            propertyProfileObject.zipcode = propertyForm.cleaned_data['zipcode']
            propertyProfileObject.city = propertyForm.cleaned_data['city']
            propertyProfileObject.save()
            return account(request)
        else:
            return render(request, "core/error.html", {'form':propertyForm})
    else:
        propertyForm = PropertyProfileForm()
        return render(request, "landlord/add_property.html", {'propertyForm':propertyForm})


# def property_profilePage(request, propertyProfile_id):
#     propertyProfile = propertyProfile.objects.filter(id=propertyProfile_id)
#     # return render_to_response(request, "core/error.html", {'form':propertyForm})
#     return render_to_response(request, "property/property_page.html", {'propertyProfile':propertyProfile})

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