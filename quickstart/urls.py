from django.conf.urls import url, include
from rest_framework import routers
import quickstart.views as views


router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('groups', views.GroupView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
