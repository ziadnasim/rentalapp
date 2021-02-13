from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('mobile', 'name', 'photo_url', 'username', 'password', 'reference_id', 'logged_in_at', 'created_at',
                  'updated_at', 'otp', 'otp_expiry', 'status')
