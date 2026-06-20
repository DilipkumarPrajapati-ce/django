from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from . import views
from .models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def addstudentfrom(request):
    return render(request ,'add-student.html')

def addstudentprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    Student.objects.create(name=txt1,mobile=txt2,email=txt3,address=txt4)
    return HttpResponse("thank you")


def homepage(request):
    return render(request,"home.html")

def aboutpage(request):
    return render(request,"about.html")


def saveSessionData(request):
    request.session['username'] = "shivay"
    return HttpResponse("session creater")

def gatSessionData(request):
    if request.session.has_key('username'):
       MSG = request.session['username'] 
       return HttpResponse(MSG)
    else:
        return HttpResponse("session variate not found")

def deletSessionData(request):
    request.session['username'] 
    return HttpResponse("session removed")

def getSessionData2(request):
    MSG = request.session['username'] 
    return HttpResponse(MSG)

def loginpage(request):
    return render(request,"login.html")

def loginprocess(request):
    txt1 = request.POST['email']
    request.session['myemail'] = txt1
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,"dashboard.html")
    else:
        return redirect(loginpage)
    
def logout(request):
    del request.session ['myemail']
    return redirect(loginpage)

def mailsenddemo(request):
          subject = 'Django Mail Demo'
          message = ' Hello How are you ?'
          email_from = settings.EMAIL_HOST_USER
          recipient_list = ['dilipkumarprajapati.24.ce@iite.indusuni.ac.in',]
          send_mail( subject, message, email_from, recipient_list )
          return HttpResponse("Mail Sent Successfully")
def contactpage (request):
     return render(request, 'contact.html')

def contactpageprocess (request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    mymsg = "Hello has Contact you", txt1," Mobile No is ",txt2," Message is ",txt3
    subject ='Contact us From Website'
    email_from = settings.EMAIL_HOST_USER
    
    message = mymsg
    recipient_list = ['dilipkumarprajapati.24.ce@iite.indusuni.ac.in',]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Thank you for Contacting us.")

def user_registe(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return redirect('login')
 
 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def user_home(request):
    return render(request, 'user_home.html')

