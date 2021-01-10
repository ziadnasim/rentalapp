from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ProfileSerializer
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('name')
    serializer_class = ProfileSerializer
