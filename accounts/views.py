from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password= request.POST.get("password")

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            print(user)
            return redirect('/')  
        else:  
            
            messages.info(request,'invalid credentials')
            return redirect('login') 
    else:
        return render(request,'login.html')   
    


def register(request):
    if (request.method== 'POST'):
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        username= request.POST.get("username")
        email= request.POST.get("email")
        password1= request.POST.get("password1")
        password2= request.POST.get("password2")
        if password1==password2:
            user=User.objects.create_user(username=username, email=email, password=password1, first_name=first_name,last_name=last_name)
            user.save()
            messages.info(request,'User Created')
            return redirect('login')
    else:
        return render(request, 'register.html')
    
    # if request.method =='POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['username']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']
    #     email = request.POST['email']

    #     if password1==password2:
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request,'Username Taken')
    #             return redirect('register')
    #         elif User.objects.filter(email=email).exists():
    #             messages.info(request,'Email Taken')
    #             return redirect('register')
    #         else:

    #             user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
    #             user.save();
    #             messages.info(request,'User Created')
    #             return redirect('login')


    #     else:
    #         messages.info(request,'Password Not Matching')
    #         return redirect('register')
    # else:
    #     return render(request, 'index.html')
    
    
def logout(request):
    auth.logout(request)
    return render(request,'logout.html')