from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='resources'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>',views.meetingdetails, name='meetingdetails'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newMinutes/', views.newMinutes, name='newminutes'),
    path('newResource/', views.newResource, name='newresource'),
    path('newEvent/', views.newEvent, name='newevent'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]