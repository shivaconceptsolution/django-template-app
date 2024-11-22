from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('insertstudent',views.insertstudent,name='insertstudent'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('editstudent',views.editstudent,name='editstudent'),
    path('deletestudent',views.deletestudent,name='deletestudent'),
    path('stureg',views.stureg,name='stureg'),
    path('stulogin',views.stulogin,name='stulogin'),
    path('stulogout',views.stulogout,name='stulogout'),
    path('stureview',views.stureview,name='stureview'),
    path('stuviewreview',views.stuviewreview,name='stuviewreview'),
    path('stueditreview',views.stueditreview,name='stueditreview')

]
