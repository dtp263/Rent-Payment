from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class addressType(models.Model):
    city = models.TextField()
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

class propertyProfile(models.Model):
    owner = models.OneToOneField(User)
    address = models.ForeignKey(addressType)
    numberOfbedrooms = models.IntegerField()
    totalcost = models.IntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ip_address = models.IPAddressField(default='0.0.0.0')
    islandlord = models.BooleanField()
    zipcode = models.CharField(max_length=5)


    def save(self, *args, **kwargs):
        try:
            existing = UserProfile.objects.get(user=self.user)
            self.id = existing.id #force update instead of insert
        except UserProfile.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)



# class landlordUserProfile(models.Model):
#     user = models.OneToOneField(User)
#     ip_address = models.IPAddressField(default='0.0.0.0')


#     def save(self, *args, **kwargs):
#         try:
#             existing = UserProfile.objects.get(user=self.user)
#             self.id = existing.id #force update instead of insert
#         except UserProfile.DoesNotExist:
#             pass
#         models.Model.save(self, *args, **kwargs)

# class tenantUserProfile(models.Model):
#     user = models.OneToOneField(User)
#     ip_address = models.IPAddressField(default='0.0.0.0')
#     currentLandlord = models.ForeignKey(landlordUserProfile)

    
#     def save(self, *args, **kwargs):
#         try:
#             existing = UserProfile.objects.get(user=self.user)
#             self.id = existing.id #force update instead of insert
#         except UserProfile.DoesNotExist:
#             pass
#         models.Model.save(self, *args, **kwargs)








def create_user_profile(sender, instance, created, **kwargs):
    """
    Handler for adding UserProfile information when creating a new user.
    """
    if created:
        UserProfile.objects.create(user=instance)

#Connect to the post_save signal and fire create_user_profile when a new User is created.
post_save.connect(create_user_profile, sender=User)