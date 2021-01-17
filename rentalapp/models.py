from django.db import models


class Profile(models.Model):
    mobile = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    reference_id = models.IntegerField()
    logged_in_at = models.DateField()
    created_at = models.DateField()
    updated_at = models.DateField()
    otp = models.IntegerField()
    otp_expiry = models.DateField()
    status = models.IntegerField()


class House(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Profile, related_name='profiles', on_delete=models.PROTECT, null=True)


class Address(models.Model):
    house = models.ForeignKey(House, related_name='houses', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=255)
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
    user = models.ForeignKey(Profile, related_name='wishlist_profiles', on_delete=models.PROTECT, null=True)
    house_id = models.IntegerField()


class Auth(models.Model):
    user = models.ForeignKey(Profile, related_name='auth_profiles', on_delete=models.PROTECT, null=True)
    device_id = models.IntegerField()
