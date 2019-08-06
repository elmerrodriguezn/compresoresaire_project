from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from api.query import Query

def index(request):
    return render(request, '')

def single(request, id):
    query = Query()
    data = query.get(
        'product.template',
        'search_read',
        [['type', '=', 'product'],['categ_id.parent_id', '=', 71],['id', '=', id]],
        {'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'attachment','create_date'] })

    context = {"product": data[0]}
    
    return render(request, 'products/single.html', context)

def search(request):
    q = request.GET['q']
    query = Query()
    data = query.get(
        'product.template',
        'search_read',
        [['type', '=', 'product'],['categ_id.parent_id', '=', 71],['name','ilike', q]],
        {'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'attachment','create_date'] })

    context = {"products": data}
    return render(request, 'products/search.html', context)

def lead(request):
    fullName = request.POST['fullName']
    email = request.POST['email']
    phone = request.POST['phone']
    description = 'Producto: ' + request.POST['productName'], 'Número de parte: ' + request.POST['pn'], 'Mensaje: ' + request.POST['msg']
    
    query = Query()
    data = query.create(
        'crm.lead',
        'create',
        {
            'name': 'compresoresaire.com',
            'contact_name': fullName,
            'email_from': email,
            'phone': phone,
            'description': description
        })
    return redirect('/gracias-por-contactarnos/')