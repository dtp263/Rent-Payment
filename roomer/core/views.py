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
    userProf = request.user.get_profile()
    owner = get_object_or_404(UserProfile, user=propertyProf.owner)
    tenants = UserProfile.objects.all().filter(living_in=propertyProf)
    return render(request, 'property/property_page.html', {'target_property':propertyProf, 'userProf':userProf, 'owner':owner, 'tenants':tenants})


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
    if userProfile.is_landlord == True:
        properties = propertyProfile.objects.filter(owner=user)
        return render(request, "landlord/landlord_profile.html", {'user':user, 'profile':userProfile, 'properties':properties})
    elif userProfile.is_landlord == False:
        home = userProfile.living_in
        return render(request, "tenant/tenant_profile.html", {'user':user, 'profile':userProfile, 'home':home})
    else:
        return render(request, "core/error.html")

def user_profile(request, user_id):
    user = request.user
    target_user = get_object_or_404(UserProfile, id=user_id)
    if target_user.is_landlord:
        properties = propertyProfile.objects.filter(owner=target_user.user)
        return render(request, "landlord/landlord_profile.html", {'user':user, 'profile':target_user, 'properties':properties})
    else:
        home = target_user.living_in
        return render(request, "tenant/tenant_profile.html", {'user':user, 'profile':target_user, 'home':home})


@login_required
def editAccountSettings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, instance=request.user.get_profile())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/')
    else:
        form = AccountSettingsForm(instance=request.user.get_profile())
    return render(request, "user/edit_user_settings.html", {'form':form})

@login_required
def upload_property_pic(request, property_id):
    if request.method == 'POST':
        form = PropertyImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            propertyProf = get_object_or_404(propertyProfile, id=property_id)
            propertyProf.property_image = request.FILES['image']
            propertyProf.save()
            return HttpResponseRedirect('/propertyProfile/%i/' % propertyProf.id)
    else:
        form = PropertyImageUploadForm()
    return render(request, 'property/add_property_photo.html', {'form':form})

@login_required
def upload_profile_pic(request, profile_id):
    if request.method == 'POST':
        form = ProfilePhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            userProf = get_object_or_404(UserProfile, id=profile_id)
            userProf.profile_image = request.FILES['image']
            userProf.save()
            return HttpResponseRedirect('/account/')
    else:
        form = ProfilePhotoUploadForm()
    return render(request, 'user/add_profile_photo.html', {'form':form})

@login_required
def newProperty(request):
    if request.method == 'POST':
        propertyForm = PropertyProfileForm(data=request.POST)
        if propertyForm.is_valid():
            propertyProfileObject = propertyProfile(owner=request.user)
            propertyProfileObject.totalcost = propertyForm.cleaned_data['totalcost']
            propertyProfileObject.title = propertyForm.cleaned_data['title']
            propertyProfileObject.description = propertyForm.cleaned_data['description']
            propertyProfileObject.numberOfbedrooms = propertyForm.cleaned_data['numberOfbedrooms']
            propertyProfileObject.state = propertyForm.cleaned_data['state']
            propertyProfileObject.zipcode = propertyForm.cleaned_data['zipcode']
            propertyProfileObject.city = propertyForm.cleaned_data['city']
            propertyProfileObject.save()
            properties = propertyProfile.objects.filter(owner=request.user)
            return HttpResponseRedirect('/propertyProfile/%i/' % propertyProfileObject.id)
        else:
            return render(request, "core/error.html", {'form':propertyForm})
    else:
        propertyForm = PropertyProfileForm()
        return render(request, "landlord/add_property.html", {'propertyForm':propertyForm})

@login_required
def edit_property_info(request, property_id):
    target_property = get_object_or_404(propertyProfile, id=property_id)
    if request.method == 'POST':
        property_info_form = PropertySettingsForm(data=request.POST, instance=target_property)
        if property_info_form.is_valid():
            property_info_form.save()
            return HttpResponseRedirect('/propertyProfile/%i/' % target_property.id)
        else:
            return render(request, "core/error.html", {'form':propertyForm, 'target_property':target_property})
    else:
        property_info_form = PropertySettingsForm(instance=target_property)
        return render(request, "property/property_settings.html", {'form':property_info_form, 'target_property':target_property})

@login_required
def add_tenant_to_property(request, property_id):
    tenant_profile = request.user.get_profile()
    target_property = get_object_or_404(propertyProfile, id=property_id)
    tenant_profile.living_in = target_property
    tenant_profile.save()
    owner = get_object_or_404(UserProfile, user=target_property.owner)
    return render(request, "tenant/successful_property.html", {'user_profile':tenant_profile, 'property_profile':target_property, 'owner':owner})

def search_properties(request):
    if request.method == 'POST':
        form = PropertySearchform(request.POST)
        if form.is_valid():
            properties = propertyProfile.objects.filter(active=True)
            if form.cleaned_data['title']:
                properties = properties.filter(title=form.cleaned_data['title'])
            if form.cleaned_data['city']:
                properties = properties.filter(city=form.cleaned_data['city'])
            if form.cleaned_data['state']:
                properties = properties.filter(state=form.cleaned_data['state'])
            if form.cleaned_data['zipcode']:
                properties = properties.filter(zipcode=form.cleaned_data['zipcode'])
            return render(request, "property/search_results.html", {'properties':properties})
        else:
            return render(request, "property/search_properties.html", {'form':form})
    else:
        form = PropertySearchform()
        return render(request, "property/search_properties.html", {'form':form})

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
            profile.is_landlord = True
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
            user.save()
            #Save profile data
            profile = user.get_profile()
            profile.zipcode = form.cleaned_data['zip']
            profile.save()
            #Log the user in
            login(request, user)
            return redirect('account')
    else:
        form = UserProfileCreationForm()

    return render(request, "registration/register.html", {'form': form},)


def viewAllProperties(request):
    properties = propertyProfile.objects.filter(active=True)
    return render(request, "property/all_properties.html", {'properties':properties})


