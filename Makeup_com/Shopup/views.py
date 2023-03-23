from django.shortcuts import render
from Shopup.models import shine
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def main(request):
    if request.session.get("user_id", False) != False:
        user = User.objects.get(id=request.session["user_id"])
        return render(request, 'Shop.html', {"post": shine.objects.all(), "name": user})
    else:
        return render(request, 'Shop.html')


def additem(request):
    if request.method == "POST":
        data = request.POST
        add = shine(name=data["name"], brand_id=data["brand"], volume=data["volume"], price=data["price"], info=data["info"])
        add.save()
    return render(request, 'additem.html')


def login(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])
        if user !=None:
            request.session["user_id"] = user.id 
    return render(request, "relog.html")


def reg(request):
    if request.method == "POST":
        data = request.POST
        authenticate(username = data["username"], password = data["password"])
        add = User(username = data["username"])
        add.set_password(data["password"])
        add.save()
    return render(request, "reg.html")


def acc(request):
    if request.session.get("user_id", False) != False:
        return render(request, "account.html")
    else:
        return login(request)
