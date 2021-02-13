from django.shortcuts import render

# api call libs
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ProfileSerializer
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')


class ProfileViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) -- commented for not authenticating now

    queryset = Profile.objects.all().order_by('name')
    serializer_class = ProfileSerializer


class ProtectedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'You have entered Aladin !!'}
        return Response(content)
