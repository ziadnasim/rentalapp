from datetime import date

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.admin import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    photo_url = models.CharField(max_length=255, null=True, blank=True)
    reference_id = models.IntegerField(null=True, blank=True)
    logged_in_at = models.DateField(null=True, blank=True)
    created_at = models.DateField()
    updated_at = models.DateField(null=True, blank=True)
    otp = models.IntegerField()
    otp_expiry = models.DateField(null=True, blank=True)
    status = models.IntegerField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, created_at=date.today(), otp=111111, status=1)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class House(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Address(models.Model):
    house = models.ForeignKey(House, related_name='houses', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=255)  # -------------------- why this name
    location = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()


class Properties(models.Model):
    name = models.CharField(max_length=255)
    index = models.IntegerField()


class HouseProperties(models.Model):
    address = models.ForeignKey(Address, related_name='addresses', on_delete=models.PROTECT, null=True)
    property = models.ForeignKey(Properties, related_name='properties', on_delete=models.PROTECT, null=True)
    value = models.CharField(max_length=255)


class Review(models.Model):
    user = models.ForeignKey(House, related_name='review_houses', on_delete=models.PROTECT, null=True)
    comment = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house_id = models.IntegerField()


class Auth(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device_id = models.IntegerField()
