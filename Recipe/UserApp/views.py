from django.shortcuts import render,redirect
from AdminApp.models import Category,UserInformation,Product


# Create your views here.
def homepage(request):
     prod=Category.objects.all()
     return render(request,"homepage.html",{"prod":prod})

def login(request):
    if(request.method=='GET'):
        return render(request,"login.html",{})
    else:
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        try:
            user=UserInformation.objects.get(username=uname, password=pwd)
        except:
            return redirect(login)
        else:
            request.session["username"]=uname
            return redirect(homepage)


def signup(request):
    if(request.method=="GET"):
        return render(request,"signup.html",{})
    else:
        uname=request.POST['uname']
        email=request.POST['email']
        pwd=request.POST['pwd']
        s1=UserInformation()
        s1.username=uname
        s1.email=email
        s1.password=pwd
        s1.save()
        # return HttpResponse("Inserted successfully")

        return redirect(homepage)

def signout(request):
    request.session.clear()
    return redirect(homepage)

# def style(request):
#     return render(request,"homepage.html",{})
# def explore(request):
#      prod=Category.objects.all()
#      return render(request,"explore.html",{"prod":prod})

def test(request):
     prod=Category.objects.all()
     return render(request,"test.html",{"prod":prod})

def viewdetails(request,did):
    cate=Category.objects.get(id=did)
    prod=Product.objects.filter(cat=cate)
    return render(request,"explore.html",{"prod":prod})

def showrecipe(request,did):
    
    id=Category.objects.get(id=did)
    
    prod=Product.objects.filter(cat=cat1)
    return render(request,"showrecipe.html",{"prod":prod})

# def showrecipe(request,did):
#     cate=Category.objects.get(id=did)
#     prod=Product.objects.filter(cat=cate)
#     return render(request,"showrecipe.html",{"prod":prod}) 