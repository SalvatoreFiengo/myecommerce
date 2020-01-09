from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    reseller = models.BooleanField(default=False)
    has_logged_in = models.BooleanField(default=False, editable=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try: 
        if instance.userprofile.has_logged_in == False:
            instance.userprofile.has_logged_in = True
        instance.userprofile.save()
 
    except:
        Userprofile.objects.create(user=instance)
        try:
            if instance.userprofile.has_logged_in == False:
                instance.userprofile.has_logged_in = True
            instance.userprofile.save()
        except AssertionError as e:
            print(e)

