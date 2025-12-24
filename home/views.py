from django.utils import timezone
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import Contact_table, Destination
from django.contrib import messages
# Create your views here.
def index(request):
    dest = Destination.objects.all()
    return render(request,"index.html", {'dest' : dest})
    

def contact(request):

    if (request.method=='POST'):
        name= request.POST.get("name")
        password= request.POST.get("password")
        email= request.POST.get("email")
        desc= request.POST.get("desc")
        now=timezone.now()
        ob1= Contact_table(name=name, email=email,password=password,desc=desc,date=now)
        ob1.save()
       
        messages.success(request,"submitted successfully")
        print("Success: Your form has been submitted successfully!") 
        return redirect('contact')
    
    contact = Contact_table.objects.all()
    return render( request ,"contact.html",{'contact':contact})
         
   
    
    

def about(request):
    return render( request,"about.html")


def location(request,slug):
    dest= Destination.objects.filter(slug=slug)
    return render(request,"location.html", {'d' : dest})


# def search(request):
    # query = request.GET.get("search", "").strip()

    # print(query)
    
    # dest= Destination.objects.filter(name__icontains="paris")
   
    # return render (request, 'info.html', {'d':dest})


def search(request):
    query = request.GET.get("search", "").strip()
    if query:
        dest = Destination.objects.filter(name__icontains=query)  
        if dest.exists():
            print("Results:", dest,query)
            return render(request, 'info.html', {'dest': dest, 'query': query})
        
        else:
            messages.info(request,"search result: not found")
            return render(request, 'info.html', {'dest': dest, 'query': query})
        
           
