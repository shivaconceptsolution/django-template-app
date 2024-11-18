from django.shortcuts import render,redirect
from .models import Student,Reg,Review
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
   if request.session.has_key('userkey'):
     if request.method=='POST':
      obj = Student(rno=request.POST.get('txtrno'),name=request.POST.get('txtname'),branch=request.POST.get('txtbranch'),fee=request.POST.get('txtfees'))
      obj.save()
      return render(request,"designapp/student.html",{"key":"data inserted succcessfully"})
     else:
       return render(request,"designapp/student.html")
   else:
      return redirect('/designapp/stulogin')

def viewstudent(request):
     if request.session.has_key('userkey'):
       res = Student.objects.all()
       return render(request,"designapp/viewstudent.html",{"key":res})
     else:
        return redirect('/designapp/stulogin')

def editstudent(request):
    if request.session.has_key('userkey'):
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
    else:
        return redirect('/designapp/stulogin')


def deletestudent(request):
    if request.session.has_key('userkey'):
     sid=request.GET["id"]
     res = Student.objects.get(pk=sid)
     res.delete()
     return redirect("/designapp/viewstudent")
    else:
     return redirect('/designapp/stulogin')


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
         request.session['userkey']=request.POST.get('txtemail')
         return redirect('/designapp/stureview')
      else:
        return render(request,"designapp/stulogin.html",{"key":"invalid userid and password"})
    else:
      return render(request,"designapp/stulogin.html")
def stulogout(request):
    del request.session['userkey']
    return redirect('/designapp/stulogin')
def stureview(request):
    if request.method=="POST":
        data = Review.objects.filter(email=request.session['userkey'])
        if data.count()==0:
          obj = Review(rating=request.POST["rating"],email=request.session['userkey'],message=request.POST['txtmsg'])
          obj.save()
          return render(request,'designapp/stureview.html',{"key":"feedback submitted successfully"}) 
        else:
           r=Review.objects.filter(email=request.session['userkey']) 
           return render(request,'designapp/editreview.html',{"stureview":r})   
    return render(request,'designapp/stureview.html')