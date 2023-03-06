from django.shortcuts import render,redirect
from AdminApp.models import Category,UserInformation,Product,Ingredients
from UserApp.models import MyCart

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

def ok(request,did):
  
    prod=Ingredients.objects.get(id=did)
    return render(request,"ok.html",{"prod":prod})


def viewdetails(request,did):
    cate=Category.objects.get(id=did)
    prod=Product.objects.filter(cat=cate)
    return render(request,"explore.html",{"prod":prod})

def showrecipe(request,did):
    prod=Product.objects.get(id=did)
    return render(request,"showrecipe.html",{"prod":prod})

def products(request):
    prod=Ingredients.objects.all()
   
    return render(request,"products.html",{"prod":prod}) 

def cart(request):
    prod=Ingredients.objects.all()
   
    return render(request,"cart.html",{"prod":prod}) 

def show(request):
    item=MyCart.objects.all()
    return render (request,"cart.html",{"item":item})


def cart(request):
    if(request.method =="POST"):
        if("username" in request.session):
            prodid=request.POST["prodid"]
            user=request.session["username"]
            qty=request.POST["qty"]
            user=UserInformation.objects.get(username=user)
            prod=Ingredients.objects.get(id=prodid)
            cart=MyCart()
            cart.users=user
            cart.items=prod
            cart.qty=qty
            cart.save()
            
            return redirect(homepage)
        else:
            return redirect(login)
