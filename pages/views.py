from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from api.query import Query


# Create your views here.

def index(request):
    page = request.GET.get('page', 1)
    
    # Template api function
    query = Query()
    data = query.get(
        'product.template',
        'search_read', [
            ['type', '=', 'product'],
            ['categ_id.parent_id', '=', 71],
            ['x_studio_field_tGMk6', '=', True]
        ],
        {
            'fields': ['name', 'default_code', 'description_sale', 'description', 'create_date'], 'order': 'create_date'
        })

    # Django pagination
    paginator = Paginator(data, 20)
    pages = paginator.get_page(page)

    context = {"products": pages}
    
    return render(request, 'pages/index.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


def send_lead(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    phone = request.POST['phone']
    msg = request.POST['msg']
    
    query = Query()
    
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
    
    return redirect('/gracias-por-contactarnos/')


def thanks(request):
    return render(request, 'pages/thanks.html')
