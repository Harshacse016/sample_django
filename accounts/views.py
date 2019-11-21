from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import pyautogui

# Create your views here.
def exe(request):
    #return redirect('/')
    pyautogui.sleep(2)
    pyautogui.move(100,100)
    return render(request,'exe.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == "POST":

        uname = request.POST['uname']
        psw = request.POST['psw']

        user = auth.authenticate(username=uname,password=psw)

        if user is not None:
            auth.login(request,user)
            return redirect('exe')
        else:
            messages.info(request,'invalid credintials')
            return redirect('login')


        return redirect('/')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        gmail = request.POST['gmail']
        pwd = request.POST['pass']
        cpwd = request.POST['cpass']

        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=gmail).exists():
                    messages.info(request,'gmail already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=uname,password=pwd,email=gmail,first_name=fname,last_name=lname)
                    user.save()
                    messages.info(request,'Registeration is successfull')
                    return redirect('login')


        else:
            messages.info(request,'password are not matched')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')
