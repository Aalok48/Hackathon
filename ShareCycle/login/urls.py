from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('account/login', views.user_login, name = 'user_login'),
    path('account/signup', views.user_signup, name = 'user_signup')
]
