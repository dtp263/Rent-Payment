from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.models import propertyProfile, UserProfile

class UserProfileCreationForm(UserCreationForm):
    zip = forms.CharField(max_length=5, min_length=5,
    	help_text='Required. Format as XXXXX or XXXXX-XXXX.')

class PropertyProfileForm(ModelForm):
	class Meta:
		model = propertyProfile
		exclude =  ['propertyImage', 'owner', 'active', 'street_no', 
					'street', 'num_of_bathrooms', 'parking', 
					'cats_allowed', 'dogs_allowed']

class PropertyImageUploadForm(forms.Form):
	class Meta:
		model = propertyProfile
		exclude =  ['owner', 'title', 'city', 'zipcode', 'numberOfbedrooms',
					'totalcost', 'description', 'active']

class ProfilePhotoUploadForm(forms.Form):
	class Meta:
		model = UserProfile
		exclude =  ['user', 'ip_address', 'is_landlord', 'zipcode',
					'first_name', 'last_name', 'hometown', 'living_in', 'active']

class PropertyByTypeSearchForm(forms.Form):
	title = forms.CharField(required=False)
	city = forms.CharField(required=False)
	state = forms.CharField(required=False)
	zipcode = forms.CharField(required=False)
	class Meta:
		model = propertyProfile
		exclude =  ['owner', 'totalcost', 'active', 'property_image', 'description',
					'numberOfbedrooms']

class AccountSettingsForm(ModelForm):
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	hometown = forms.CharField(required=False)
	zipcode = forms.CharField(required=False)
	class Meta:
		model = UserProfile
		exclude =  ['user', 'is_landlord', 'profile_image', 'ip_address', 'living_in',
					'active']

class PropertySettingsForm(ModelForm):
	class Meta:
		model = propertyProfile
		exclude = ['property_image', 'owner', 'active']