from django.shortcuts import render,redirect
from .models import Student,Reg
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
def editstudent(request):
    sid=request.GET["id"]
    res = Student.objects.get(pk=sid)
    if request.method=="POST":
        res.rno=request.POST.get("txtrno")
        res.name=request.POST.get("txtname")
        res.branch=request.POST.get("txtbranch")
        res.fee = request.POST.get("txtfees")
        res.save()
        return redirect("/designapp/viewstudent")
    return render(request,"designapp/editstudent.html",{"key":res})


def deletestudent(request):
    sid=request.GET["id"]
    res = Student.objects.get(pk=sid)
    res.delete()
    return redirect("/designapp/viewstudent")

def stureg(request):
   if request.method=='POST':
      obj = Reg(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'),mobileno=request.POST.get('txtmobile'),name=request.POST.get('txtname'))
      obj.save()
      return render(request,"designapp/stureg.html",{"key":"data inserted succcessfully"})
   else:
     return render(request,"designapp/stureg.html")
def stulogin(request):
    if request.method=='POST':
      obj = Reg.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'))
      if obj.count()>0:
         return redirect('/designapp/viewstudent')
      else:
        return render(request,"designapp/stulogin.html",{"key":"invalid userid and password"})
    else:
      return render(request,"designapp/stulogin.html")