from django.shortcuts import render,redirect
from urllib import request
from hotel.models import Hotel_table, Activity_table

# Create your views here.
def index(request):
    htable=Hotel_table.objects.all()
    return render(request,'stay.html',{'htable':htable})


def activity(request):
    act=Activity_table.objects.all()
    return render(request, 'activity.html',{'act':act})