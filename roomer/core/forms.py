from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.localflavor.us.forms import USZipCodeField

class UserProfileCreationForm(UserCreationForm):
    zip = USZipCodeField(required=True, label='Zip Code',
        help_text='Required. Format as XXXXX or XXXXX-XXXX.')
    

class LandlordCreationForm(UserCreationForm):
	zip = USZipCodeField(required=True, label='Zip Code',
        help_text='Required. Format as XXXXX or XXXXX-XXXX. LANDLORD') 

class TenantCreationForm(UserCreationForm):
    zip = USZipCodeField(required=True, label='Zip Code',
        help_text='Required. Format as XXXXX or XXXXX-XXXX.  TENNANT')
