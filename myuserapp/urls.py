from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage),
    path('home',views.homepage,name='home'),
    path('contact',views.contactpage,name='contact'),
    path('contactprocess',views.contactpageprocess),
    path('saveSession',views.saveSessionData,name='saveSessio'), 
    path('getSession',views.gatSessionData,name='getSession'),
    path('login',views.loginpage,name='login'),
    path('loginprocess',views.loginprocess),
    path('dashbord',views.dashboard,name='dashbord'),
    path('maildemo',views.mailsenddemo),
    path('addstudent',views.addstudentfrom,name='addstudent'),
    path('addstudentfrom',views.addstudentprocess),
    path('add-student-process',views.addstudentprocess),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_registe, name='register'),
    path('home/', views.user_home, name='home'),
    path('logout/', views.user_logout, name='logout'),

]