from django.shortcuts import render
from .models import Student
def home(request):
    
    return render(request,"designapp/home.html")
def about(request):
    obj = Student.objects.get(pk=1)
    obj.rno=1009
    obj.name='stu3'
    obj.branch='IT'
    obj.fee=32000
    obj.save()
    return render(request,"designapp/about.html")
def services(request):
    obj = Student.objects.get(pk=1)
    obj.delete()
    return render(request,"designapp/services.html")
def contact(request):
    obj = Student.objects.filter(rno='3')
    return render(request,"designapp/contact.html",{"studata":obj})
def gallery(request):
    return render(request,"designapp/gallery.html")

def insertstudent(request):
   if request.method=='POST':
      obj = Student(rno=request.POST.get('txtrno'),name=request.POST.get('txtname'),branch=request.POST.get('txtbranch'),fee=request.POST.get('txtfees'))
      obj.save()
      return render(request,"designapp/student.html",{"key":"data inserted succcessfully"})
   else:
     return render(request,"designapp/student.html")

def viewstudent(request):
    res = Student.objects.all()
    return render(request,"designapp/viewstudent.html",{"key":res})