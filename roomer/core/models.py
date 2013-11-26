from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
import os

def get_property_image_path(instance, filename):
    return os.path.join('photos/property_photos', str(instance.id), filename)

def get_user_image_path(instance, filename):
    return os.path.join('photos/user_photos', str(instance.id), filename)

class addressType(models.Model):
    city = models.TextField(max_length=15)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

class propertyProfileManager(models.Manager):
    def create_propertyProfile(self, title):
        property = self.create(title=title)
        return propertyProfile

    def get_by_naural_key(self, title):
        return self.get(title=title)

class propertyProfile(models.Model):
    # used for natural key handling
    objects = propertyProfileManager()
    
    owner = models.OneToOneField(User)
    title = models.CharField(max_length=100)
    address = models.ForeignKey(addressType)
    numberOfbedrooms = models.IntegerField(default=1)
    totalcost = models.IntegerField(default='n/a')
    property_image = models.ImageField(upload_to=get_property_image_path, blank=True, null=True)
    description = models.TextField(default="(No description provided.)")

    def _unicode_(self):
        return self.title



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ip_address = models.IPAddressField(default='0.0.0.0')
    islandlord = models.BooleanField(default=False)
    zipcode = models.CharField(max_length=5)
    profile_image = models.ImageField(upload_to=get_user_image_path, blank=True, null=True)
    properties = models.ManyToManyField(propertyProfile)



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