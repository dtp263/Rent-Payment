from django.db import models
from core.models import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.shortcuts import render
from PIL import Image
import os

def get_property_image_path(instance, filename):
    return os.path.join('static/photos/property_photos', str(instance.id), filename)

def get_user_image_path(instance, filename):
    return os.path.join('static/photos/user_photos', str(instance.id), filename)

class propertyProfileManager(models.Manager):
    def create_propertyProfile(self, user):
        propertyProfile = self.create(owner=user)
        return propertyProfile

    def get_by_naural_key(self, title):
        return self.get(title=title)

class propertyProfile(models.Model):
    # used for natural key handling
    objects = propertyProfileManager()
    
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    # address = models.ForeignKey(addressType)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=5)
    numberOfbedrooms = models.IntegerField(default=1)
    totalcost = models.IntegerField(default=0)
    property_image = models.ImageField(upload_to=get_property_image_path, blank=True, null=True)
    description = models.TextField(default="(No description provided.)")
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core.views.property_profile', args=[str(self.id)])

    @classmethod
    def upload_photo(self):
        return reverse('core.views.upload_property_pic', args=[str(self.id)])

    @classmethod
    def add_tenant(request):
        return reverse('core.views.add_tenant_to_property', args=[str(self.id)])


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ip_address = models.IPAddressField(default='0.0.0.0')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    hometown = models.CharField(max_length=100)
    is_landlord = models.BooleanField(default=False)
    zipcode = models.CharField(max_length=5)
    profile_image = models.ImageField(upload_to=get_user_image_path, blank=True, null=True)
    living_in = models.ForeignKey(propertyProfile, null=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        try:
            existing = UserProfile.objects.get(user=self.user)
            self.id = existing.id #force update instead of insert
        except UserProfile.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs):
    """
    Handler for adding UserProfile information when creating a new user.
    """
    if created:
        UserProfile.objects.create(user=instance)


#Connect to the post_save signal and fire create_user_profile when a new User is created.
post_save.connect(create_user_profile, sender=User)