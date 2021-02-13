from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'photo_url', 'username', 'password', 'reference_id', 'logged_in_at', 'created_at',
                  'updated_at', 'otp', 'otp_expiry', 'status')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
