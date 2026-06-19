from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from . import views
from .models import Student

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