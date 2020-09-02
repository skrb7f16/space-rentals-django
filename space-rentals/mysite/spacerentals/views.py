from django.shortcuts import render, HttpResponse, render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def index(request):
    print(request.user.username)
    if(request.user.is_authenticated):
        context = {
            "navbar": {
                "user": f'<li><a href="#">{request.user.username}</a></li>',
                "button": f'<li><a href="logoutUser">logout</a></li>'
            },
            "overlay": {
                "user": f'<a href="#">{request.user.username}</a>',
                "button": f'<a href="logoutUser">logout</a>'
            }
        }
    else:
        context = {
            "navbar": {
                "user": f'<li><a href="#">{request.user.username}</a></li>',
                "button": f'<li><a href="/#user">login</a></li>'
            },
            "overlay": {
                "user": f'<a href="#">{request.user.username}</a>',
                "button": f'<a href="/#user">login</a>'
            }
        }
    if(request.method == "POST"):
        cat = request.GET.get('cat')
        if(cat == "signup"):
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            if(password == cpassword):
                user = User(username=username, password=password, email=email)
                user.save()
            else:
                messages.error(request, "Passwords should be same")

        if(cat == "login"):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if(request.user != user):
                    logout(request)
                login(request, user)
                messages.success(
                    request, f"{request.user.username} is logged in")
            else:
                messages.error(request, "wrong credentials")
    return render(request, 'index.html',context)


def pgList(request):
    pgs = Pg.objects.all()
    if(request.user.is_authenticated):
        context = {
            "navbar": {
                "user": f'<li><a href="#">{request.user.username}</a></li>',
                "button": f'<li><a href="logoutUser">logout</a></li>'
            },
            "overlay": {
                "user": f'<a href="#">{request.user.username}</a>',
                "button": f'<a href="logoutUser">logout</a>'
            },
            "pgs": pgs
        }
    else:
        context = {
            "navbar": {
                "user": f'<li><a href="#">{request.user.username}</a></li>',
                "button": f'<li><a href="/#user">login</a></li>'
            },
            "overlay": {
                "user": f'<a href="#">{request.user.username}</a>',
                "button": f'<a href="/#user">login</a>'
            },
            "pgs": pgs
        }
    return render(request, 'pgList.html', context)


def pgName(request):
    if(request.user.is_authenticated):
        pid = request.GET.get('id')
        if(pid):
            pid = int(pid)
            pg = Pg.objects.filter(pid=pid).first()
            reviews=Review.objects.filter(to=pid)
            context = {
                "navbar": {
                    "user": f'<li><a href="#">{request.user.username}</a></li>',
                    "button": f'<li><a href="logoutUser">logout</a></li>'
                },
                "overlay": {
                    "user": f'<a href="#">{request.user.username}</a>',
                    "button": f'<a href="logoutUser">logout</a>'
                },
                "pg": pg,
                "reviews":reviews
            }
            if(request.method=="POST"):
                ratings=str(request.POST.get('ratings'))
                desc=request.POST['desc']
                review=Review(by=request.user,desc=desc,ratings=ratings,to=pid)
                review.save()
                messages.success(request,"Yeah Your reviews matter to us thanks!!!")
            return render(request, 'pg.html', context)
    else:
        messages.warning(request, "Please login to see more")
        return redirect('/#user')


def booking(request):
    if(request.user.is_authenticated):
        pid = request.GET.get('id')
        if(pid):
            pid = int(pid)
        pg = Pg.objects.filter(pid=pid).first()
        context = {
            "navbar": {
                "user": f'<li><a href="#">{request.user.username}</a></li>',
                "button": f'<li><a href="logoutUser">logout</a></li>'
            },
            "overlay": {
                "user": f'<a href="#">{request.user.username}</a>',
                "button": f'<a href="logoutUser">logout</a>'
            },
            "pg": pg
        }
        if(request.method == "POST"):
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            timeperiod = request.POST.get('timeperiod')
            type = request.POST.get('for')
            dob = str(request.POST.get('dob'))
            phone = request.POST.get('phone')
            food = request.POST.get('food')
            book = Booking(fname=fname, lname=lname, phone=phone, dob=dob, type=type,
                           food=food, by=request.user, booked=pg, email=email, timeperiod=timeperiod)
            book.save()
            messages.success(request,"Your booking has been done we go the respective pg and ask for ur name and username")
            return redirect(pgList)
        else:
            return render(request, 'booking.html', context)
    else:
        messages.warning(request, "Please login to see more")
        return redirect('/#user')


def logoutUser(request):
    logout(request)
    return redirect(index)
