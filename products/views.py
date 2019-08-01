from django.shortcuts import render, redirect
from api.queries import *

def index(request):

    return render(request, '')

def single(request, id):
    return render(request, 'products/single.html', context_detail(id))

def search(request):
    q = request.GET['keywords']
    return render(request, 'products/search.html', context_search(q))
    
def lead(request):
    fullName = request.GET['fullName']
    email = request.GET['email']
    phone = request.GET['phone']
    description = 'Producto: ' + request.GET.get('productName', False), 'Número de parte Mesabi: ' + request.GET.get('mpn', False), 'Número de parte OEM: ' + request.GET.get('oempn', False), 'Mensaje: ' + request.GET['msg']
    create_lead(fullName, email, phone, description)
    return redirect('/gracias-por-contactarnos/')