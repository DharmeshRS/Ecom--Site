from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from App.forms import SignUpForm
from .models import AddProductModell,AddCatagoryModel
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        name=request.user.username
        return render(request, "index.html",{"categories":AddCatagoryModel.objects.all()[:6],"productdata":AddProductModell.objects.all(),"name":name})

    else:
        return render(request, "index.html",{"categories":AddCatagoryModel.objects.all()[:6],"productdata":AddProductModell.objects.all()})


def productlist(request):
    product_id=request.GET['product_id']
    print(product_id)
    product_data=AddProductModell.objects.filter(product_category=product_id)
    return render(request, "Product_list.html", {"product_data":product_data})


# Create your views here.
def signup(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Registration Successful...")
    else:
        fm=SignUpForm()
    return render(request,"signup.html",{"form":fm,"categories":AddCatagoryModel.objects.all()})


def userlogin(request):
    # if not request.user.is_authenticated:
    if request.method == "POST":
        authform = AuthenticationForm(request=request, data=request.POST)
        if authform.is_valid():
            uname = authform.cleaned_data['username']
            upass = authform.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfully")
                return HttpResponseRedirect('/')
    else:
        authform = AuthenticationForm()
    return render(request, "login.html", {"form": authform,"categories":AddCatagoryModel.objects.all()})
    # else:
    #     return HttpResponseRedirect('/login/')

def user_profile(request):
    if request.user.is_authenticated:
        abc=request.user.username
        name=User.objects.filter(username=abc)
        print(name)
        return render(request,"profile.html",{"name":name,"categories":AddCatagoryModel.objects.all()})
    else:
        return HttpResponseRedirect('/login/')


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def cartpage(request):
    return render(request,"cart.html")


def updateprofile(request):
    userid = request.GET.get("userid")
    profile_info = User.objects.filter(id=userid)
    print(profile_info)
    return render(request, "update_profile.html", {"profile_info": profile_info})


def save_updateprofile(request):
        id = request.user.id
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        User.objects.filter(id=id).update(first_name=firstname, last_name=lastname, username=username)

        messages.success(request, "Profile Updated Successfully...")
        return HttpResponseRedirect('/profile/')
        # return render(request, "profile.html", {"name": request.user.username, "categories": AddCatagoryModel.objects.all()})


