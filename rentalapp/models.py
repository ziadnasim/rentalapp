from django.db import models


class Profile(models.Model):
    mobile = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    reference_id = models.IntegerField()
    logged_in_at = models.DateField()
    created_at = models.DateField()
    updated_at = models.DateField()
    otp = models.IntegerField()
    otp_expiry = models.DateField()
    status = models.IntegerField()


class House(models.Model):
    name = models.CharField(max_length=200)
    owner_id = models.IntegerField()
    address_id = models.IntegerField()


class Address(models.Model):
    house_id = models.IntegerField()
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    lat = models.FloatField()
    long = models.FloatField()


class Properties(models.Model):
    name = models.CharField(max_length=200)
    index = models.IntegerField()


class HouseProperties(models.Model):
    house_id = models.IntegerField()
    property_id = models.IntegerField()
    value = models.CharField(max_length=200)


class Review(models.Model):
    user_id = models.IntegerField()
    comment = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)


class Wishlist(models.Model):
    user_id = models.IntegerField()
    house_id = models.IntegerField()


class Auth(models.Model):
    user_id = models.IntegerField()
    device_id = models.IntegerField()
