from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.profile, name='profile'),
    url(r'^createProfile', views.UserRegistrationView.as_view(), name='user-registration'),
]
