from django.shortcuts import render

# api call libs
from rest_framework import viewsets
from rest_framework.decorators import api_view
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


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class OnlyPost(APIView):
    def post(self, request, *args, **kwargs):
        posted_data = self.request.data
        city = posted_data['city']
        return_data = [
            {"echo": city}
        ]
        return Response(status=200, data=return_data)
