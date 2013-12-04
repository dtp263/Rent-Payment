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
		exclude = ['propertyImage', 'owner']

class PropertyImageUploadForm(forms.Form):
	class Meta:
		model = propertyProfile
		exclude = ['owner', 'title', 'city', 'zipcode', 'numberOfbedrooms', 'totalcost', 'description']

class ProfilePhotoUploadForm(forms.Form):
	class Meta:
		model = UserProfile
		exclude = ['user', 'ip_address', 'is_landlord', 'zipcode']