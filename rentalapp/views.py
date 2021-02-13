from django.shortcuts import render

# api call libs
from rest_framework import viewsets
from .serializer import ProfileSerializer
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('name')
    serializer_class = ProfileSerializer
