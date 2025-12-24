from accounts import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',views.index, name='home' ),
      path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
]