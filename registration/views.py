import secrets
from django.shortcuts import render,redirect,render_to_response,HttpResponse
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from django.template import RequestContext
from newsapi import NewsApiClient
from django.contrib.auth.models import AnonymousUser
from registration.models import Users,Token


def news(request):
        x=request.COOKIES.get('Token')
        print("check")
        if(x!=None):
            temp=Token.objects.filter(Tokens=x)
            temp1=Users.objects.filter(User_id=temp[0].Userid_id)
            newsapi=NewsApiClient(api_key='593f97232929446bb683fe321eaa3a16')
            top=newsapi.get_everything(sources='bbc-news,the-verge',)

            l=top['articles']
            desc=[]
            news=[]
            img=[]
            
            for i in range(len(l)):
                f=l[i]
                news.append(f['title'])
                desc.append(f['description'])
                img.append(f['urlToImage'])
                mylist=zip(news,desc,img)
            return render(request,'welcome.html',context={"mylist":mylist,'user':temp1})
        else:
            print("check2") 
            return redirect("login")    


def login (request):
    if(request.method=='POST'):
        username=request.POST['Username']
        password=request.POST['pass']
        user=Users.objects.filter(User_name=username,Password=password)
        if(user.exists()):
            temp=Token.objects.filter(Userid_id=user[0].User_id)
            print("temp",temp)   
            if(temp.exists()):
                print("me")
                return redirect("home")
            else:
                y=request.COOKIES.get('Token')
                print("cookie",y)
                x=secrets.token_bytes(5)
                print("x",x)
                x=str(x)
                #request.session[username + "chck"] = x
                #print("session")
                g_token=Token(Userid_id=user[0].User_id,Tokens=x)
                g_token.save();
                print("g_token",g_token)
                response=render_to_response('homepage.html',{'data':user})
                response.set_cookie('Token',x)
                return response 
            
        else:
            messages.info(request,"Invalid Credential")
            print("9")
            return render(request,"login.html")
    else:   
        print("8")
        x=request.COOKIES.get('Token')
        print("check")
        if(x!=None):
            temp=Token.objects.filter(Tokens=x)
            temp1=Users.objects.filter(User_id=temp[0].Userid_id)
            return render(request,"homepage.html",{'data':temp1})
        else:
            return render(request,"login.html")




def signup(request):
    if(request.method=="POST"):
        first=request.POST['first_name']
        last=request.POST['last_name']
        username=request.POST['username']
        tel=request.POST['phone']
        email=request.POST['email']
        password=request.POST['pass']
        rpassword=request.POST['rpass']
        gen=request.POST['g']
        dob=request.POST['ddate']
        if(password==rpassword):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username already exist')
                print("7")
                return render(request,'index.html')
            elif (User.objects.filter(email=email).exists()):
                messages.info(request,"E-mail already exist ")
                print("6")
                return render(request,'index.html')
            else:
                user=Users(User_name=username,Password=password,Email=email,
                First_name=first,Last_name=last,Phone_no=tel,Date_of_Birth=dob,Gender=gen)
                user.save();
                messages.success(request,'You Have Registered Successfully')
                print("2")
                return redirect('login')
        else:
            messages.info(request,"Password doesnot matched")
            print("1")
            return render(request,"index.html")
    else:
        print("3")
        x=request.COOKIES.get('Token')
        print("check")
        if(x!=None):
            temp=Token.objects.filter(Tokens=x)
            temp1=Users.objects.filter(User_id=temp[0].Userid_id)
            return render(request,"homepage.html",{'data':temp1})
        else:
            return render(request,"index.html")




def home(request):
    x=request.COOKIES.get('Token') 
    print("check")
    if(x!=None):
        temp=Token.objects.filter(Tokens=x)
        temp1=Users.objects.filter(User_id=temp[0].Userid_id)
        return render(request,"homepage.html",{'data':temp1})
    else:
        return render(request,"homepage.html")



def logout(request):
    data={}
    #request.session["chck"] =
    #print(x)
    x=request.COOKIES.get('Token')
    temp=Token.objects.filter(Tokens=x)
    if(temp.exists()):
        temp.delete()
        response=render_to_response('homepage.html',{'data':data})
        response.delete_cookie('Token')
        return response
    else:
        return render(request,'login.html')