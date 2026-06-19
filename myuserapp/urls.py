from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage),
    path('home',views.homepage),
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('contactprocess',views.contactpageprocess),
    path('saveSession',views.saveSessionData), 
    path('getSession',views.gatSessionData),
    path('login',views.loginpage),
    path('loginprocess',views.loginprocess),
    path('dashbord',views.dashboard),
    path('maildemo',views.mailsenddemo),
    path('addstudent',views.addstudentfrom),
    path('addstudentfrom',views.addstudentprocess),
    path('add-student-process',views.addstudentprocess)
]