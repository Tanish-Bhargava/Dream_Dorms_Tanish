from django.shortcuts import render
from django.shortcuts import render , redirect
from .models import *
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from decimal import Decimal
from django.urls import reverse

def Home(request):
    return render(request , 'Dreamdorms.html')

def base(request):
    # eventlist = searchdb.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        searchman = searchdb.objects.filter(area_name__icontains=searched)
        return render(request, 'base.html', { 'searched': searched , 'searchman':searchman })
    else:
        return render(request , 'base.html')
    
def proper(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searchman = searchdb.objects.filter(Q(area_name__icontains=searched) | Q(property_name__icontains=searched))
        return render(request, 'property.html', { 'searched': searched , 'searchman':searchman })
    else:
        return render(request , 'property.html')
    
def list(request):
    eventlist = searchdb.objects.all()
    return render(request , 'list.html',{'eventlist': eventlist })

def login(request):
    print("View accessed")
    if request.method == "POST":
        print("this is a post")
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, email, password)
        ins = loginn(username=username, email=email, password=password)
        ins.save()
        return redirect(reverse('Home'))
    return render(request, 'login.html')

def temp(request):
    loginlist = loginn.objects.all()
    return render(request, 'temp.html', {'loginlist': loginlist })

def swim(request):
    return render(request , "swimming.html")

def contact(request):
    return render(request , "contact.html")

def booking(request):
    if request.method == "POST":
        print("hello world")
        pname = request.POST.get('pname')
        pemail = request.POST.get('pemail')
        property_code = request.POST.get('property_code')
        comments = request.POST.get('comments')
        
        ins = grapes(pname=pname, pemail=pemail, property_code=property_code, comments=comments)
        ins.save()
        
        print("Data has been written to the database")
        return redirect(reverse('Home'))
    return render(request, 'booking.html')

def broker(request):
    return render(request , "broker.html")



    
    

# Create your views here.
