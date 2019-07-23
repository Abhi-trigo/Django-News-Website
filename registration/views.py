from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from django.template import Context

# Create your views here.
def login (request):
    if(request.method=='POST'):
        username=request.POST['Username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('here 2')
            return render(request,'welcome.html')
        else:
            messages.info(request,"Invalid Credential")
            print("here 1")
            return render(request,'login.html')
    else:   
        print("here 3") 
        return render(request,'login.html')

def signup(request):
    if(request.method=="POST"):
        first=request.POST['first_name']
        last=request.POST['last_name']
        username=request.POST['username']
        tel=request.POST['phone']
        email=request.POST['email']
        password=request.POST['pass']
        rpassword=request.POST['rpass']
        #gen=request.POST['g']
        dob=request.POST['ddate']
        if(password==rpassword):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username Taken')
                return render(request,"index.html")
            elif (User.objects.filter(email=email).exists()):
                messages.info(request,"E-mail taken")
                return render(request,'index.html')
            else:
                user=User.objects.create_user(username=username ,password=password,email=email,
                first_name=first,last_name=last)
                user.save();
                messages.success(request,'You Have Registered Successfully')
                return render(request,'login.html')
        else:
            messages.info(request,"Password does nsot matched")
            return redirect(" ")
    else:
        return render(request,'index.html')


def home(request):


    return render(request,"welcome.html")