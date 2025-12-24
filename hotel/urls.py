from hotel import views
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   

    path('',views.index, name='hotel' ),
    path('activity',views.activity, name='activity' ),
   
]