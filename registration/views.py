import secrets
from django.shortcuts import render,redirect,render_to_response,HttpResponse
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from django.template import RequestContext
from newsapi import NewsApiClient
from django.contrib.auth.models import AnonymousUser
from registration.models import Users,Token


def check(req):
    temp=list(req.keys())
    temp1=list(req.values())
    temp2=[]
    for i in range(len(temp1)):
        if(temp1[i]==None):
            temp2.append(temp[i])
        elif(temp1[i]==""):
            temp2.append(temp[i])
    if(len(temp2)==0):
        return True
    else:
        return temp2


def news(request):
        x=request.COOKIES.get('Token')
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
            return redirect("login")    


def login (request):
    if(request.method=='POST'):
        username=request.POST['Username']
        password=request.POST['pass']
        user=Users.objects.filter(User_name=username,Password=password)
        if(user.exists()):
            temp=Token.objects.filter(Userid_id=user[0].User_id)
            if(temp.exists()):
                return redirect("home")
            else:
                y=request.COOKIES.get('Token')
                x=secrets.token_bytes(5)
                x=str(x)
                g_token=Token(Userid_id=user[0].User_id,Tokens=x)
                g_token.save();
                response=render_to_response('homepage.html',{'data':user})
                response.set_cookie('Token',x)
                return response 
            
        else:
            if(password==""):
                messages.info(request,"Password Field is Missing")
                return render(request,"login.html")
            elif(username==""):
                messages.info(request,"Username Field is Missing")
                return render(request,"login.html")
            else: 
                messages.info(request,"Invalid Credential")
                return render(request,"login.html")
    else:   
        x=request.COOKIES.get('Token')
        if(x!=None):
            temp=Token.objects.filter(Tokens=x)
            temp1=Users.objects.filter(User_id=temp[0].Userid_id)
            return render(request,"homepage.html",{'data':temp1})
        else:
            return render(request,"login.html")




def signup(request):
    if(request.method=="POST"):
        temp=check(request.POST)
        if(temp != True):
            for i in temp:
                stemp=""
                stemp=stemp+i+" is missing "
                messages.info(request,stemp)
            return render(request,"index.html")

        else:

            first=request.POST.get('first_name',None)
            last=request.POST.get('last_name',None)
            username=request.POST.get('username',None)
            try:
                tel=request.POST.get('phone',None)
                xtemp=int(tel)
            except ValueError:
                messages.info(request,"Inalid content in Phone No. Field")
                return render(request,"index.html")           
            email=request.POST.get('email',None)
            password=request.POST.get('pass',None)
            rpassword=request.POST.get('rpass',None)
            gender = request.POST.get('g', None)
            dob=request.POST.get('ddate',None)
            if(password==rpassword):
                if(User.objects.filter(username=username).exists()):
                    messages.info(request,'Username already exist')
                    return render(request,'index.html')
                elif (User.objects.filter(email=email).exists()):
                    messages.info(request,"E-mail already exist ")
                    return render(request,'index.html')
                else:
                    user=Users(User_name=username,Password=password,Email=email,
                    First_name=first,Last_name=last,Date_of_Birth=dob,Phone_no=tel,Gender=gender)
                    user.save();
                    messages.success(request,'You Have Registered Successfully')
                    return redirect('login')
            else:
                messages.info(request,"Password doesnot matched")
                return render(request,"index.html")
    else:
        x=request.COOKIES.get('Token')
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
    x=request.COOKIES.get('Token')
    temp=Token.objects.filter(Tokens=x)
    if(temp.exists()):
        temp.delete()
        response=render_to_response('homepage.html',{'data':data})
        response.delete_cookie('Token')
        return response
    else:
        return render(request,'login.html')