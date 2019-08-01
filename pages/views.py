from django.shortcuts import render, redirect
from api.queries import *

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', context_limit())

def contact(request):
    return render(request, 'pages/contact.html')

def send_lead(request):
    fullName = request.POST['fullName']
    email = request.POST['email']
    phone = request.POST['phone']
    msg = request.POST['msg']
    create_lead(fullName, email, phone, msg)
    return redirect('/gracias-por-contactarnos/')
    
def thanks(request):
    return render(request, 'pages/thanks.html')