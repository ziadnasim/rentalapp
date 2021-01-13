from django.db import models

class Profile(models.Model):
    mobile = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    reference_id = models.IntegerField()
    logged_in_at= models.DateField()
    created_at = models.DateField()
    updated_at = models.DateField()
    otp = models.IntegerField()
    otp_expiry = models.DateField()
    status = models.IntegerField()

class House(models.Model):
    name = models.CharField(max_length=255)
    owner_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address_id = models.IntegerField()

class Address(models.Model):
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()

class Properties(models.Model):
    name = models.CharField(max_length=255)
    index = models.IntegerField()

class HouseProperties(models.Model):
    house_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    property_id = models.IntegerField()
    value = models.CharField(max_length=255)

class Review(models.Model):
    user_id = models.ForeignKey(House, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)

class Wishlist(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    house_id = models.IntegerField()

class Auth(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    device_id = models.IntegerField()