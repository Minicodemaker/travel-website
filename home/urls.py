from home import views
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    path('',views.index, name='home' ),
    path('about/',views.about, name='about' ),
    path('contact/',views.contact, name='contact' ),
      path('location/<slug:slug>/',views.location, name='location' ),
       path('search/',views.search, name='search' ),
    
    

]



