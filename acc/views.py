from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages
# Create your views here.

def delete(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        messages.warning(request, "패스워드가 달라요 :(")
        return redirect("acc:profile")

def changepw(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password( cp, u.password ):
        np = request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect("acc:login")
    else:
        messages.warning(request, "패스워드가 달라요 :(")
    return redirect("acc:update")



def update(request):
    if request.method == "POST":
        u = request.user
        ue = request.POST.get("umail")
        uc = request.POST.get("ucon")
        up = request.FILES.get("upic")
        u.email , u.content = ue, uc
        if up:
            u.pic.delete()
            u.pic = up
        u.save()
        return redirect("acc:profile")
    return render(request, "acc/update.html")

def profile(request):
    return render(request, "acc/profile.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("con")
        upic = request.FILES.get("pic")
        try:
            User.objects.create_user(username=un, password=up, content=uc, pic=upic)
            return redirect("acc:login")
        except:
            messages.warning(request, "이미 있는 이름 이에요")
    return render(request, "acc/signup.html")

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def login_user(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            return redirect("acc:index")   
        else:
            messages.error(request, "이름이나 패스워드가 맞지 않아요 :(")
    return render(request, "acc/login.html")



def index(request):
    return render(request, "acc/index.html")