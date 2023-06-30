from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from . models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'Home.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        client = auth.authenticate(username=username,password=password)
        if client is not None:
            auth.Login(request,client)
            return redirect('/new')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/Login')
    return render(request,"Login.html")


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if (password==confirmpassword):
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
                return redirect('/Login')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('/Login')
        else:
            messages.info(request,"Password is incorrect")
            return redirect('/Register')



    return render(request,'Register.html')

def new(request):
    return render(request,'Newpage.html')

def drop(request):
    if request.method=='POST':
        NAME = request.POST.get('NAME')
        DOB = request.POST.get('DOB')
        AGE = request.POST.get('AGE')
        GENDER = request.POST.get('GENDER')
        PHONENUMBER = request.POST.get('PHONENUMBER')
        EMAIL_ID = request.POST.get('EMAIL_ID')
        ADDRESS = request.POST.get('ADDRESS')
        DISTRICT = request.POST.get('DISTRICT')
        BRANCHES = request.POST.get('BRANCHES')
        ACCOUNT_TYPE = request.POST.get('ACCOUNT_TYPE')
        MATERIALS_PROVIDE = request.POST.get('MATERIALS_PROVIDE')


        Data = Contact(NAME=NAME,DOB=DOB,AGE=AGE,GENDER=GENDER,PHONENUMBER=PHONENUMBER,EMAIL_ID=EMAIL_ID,ADDRESS=ADDRESS,DISTRICT=DISTRICT,BRANCHES=BRANCHES,ACCOUNT_TYPE=ACCOUNT_TYPE,MATERIALS_PROVIDE=MATERIALS_PROVIDE)
        Data.save()

        return redirect('/Message')

    return render(request,'drop.html')

def Message(request):
    return render(request,'Message.html')


