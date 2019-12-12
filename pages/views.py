from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from api.query import Query
from modules.recaptcha import recaptcha


def index(request):

    query = Query()

    data = query.get(
        'product.template',
        'search_read', [
            ['type', '=', 'product'],
            ['x_studio_field_tGMk6', '=', True],
            ['categ_id.parent_id', 'in', [71, 79]],
        ],
        {
            'fields': ['name', 'default_code', 'description_sale', 'description', 'create_date', 'categ_id', 'categ_id.name'],
            'order': 'create_date'
        })

    context = {"products": data}

    return render(request, 'pages/index.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


def send_lead(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    phone = request.POST['phone']
    msg = request.POST['msg']
    
    query = Query()
    if request.method == 'POST' and recaptcha(request):
        data = query.create(
            'crm.lead',
            'create',
            {
                'name': 'compresoresaire.com',
                'contact_name': full_name,
                'email_from': email,
                'phone': phone,
                'description': msg
            })
        return redirect('thanks')
    else:
        return redirect('index')


def thanks(request):
    return render(request, 'pages/thanks.html')
