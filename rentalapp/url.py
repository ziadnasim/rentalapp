from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'props', views.PropViewSet)
router.register(r'createuser', views.CreateUser)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hello/', views.ProtectedView.as_view(), name='hello'),
    path('hello_world/', views.HELLOWORLDVIEW.as_view(), name='hello_world'),
    path('opost/', views.OnlyPost.as_view(), name='opost'),
    # path('createuser/', views.CreateUser.as_view(), name='createuser'),
    path('hello_world/', views.hello_world),
    path('access/', obtain_auth_token, name='api_token_auth')
]