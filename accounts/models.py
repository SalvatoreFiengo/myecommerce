from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    reseller = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    post_code = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True, null=True)
    street_address1 = models.CharField(max_length=50, blank=True, null=True)
    street_address2 = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=40, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)
        instance.userprofile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.save()
    except:
        Userprofile.objects.create(user=instance)
        try:
           instance.userprofile.save() 
        except: 
            pass

