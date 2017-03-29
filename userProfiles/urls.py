from django.conf.urls import url
from django.contrib.auth.views import login
from userProfiles import views

urlpatterns = [
    url(r'^/?$', views.profile, name='profile'),
    url(r'^login/', views.UserLoginView.as_view(), name='user-login'),
]
