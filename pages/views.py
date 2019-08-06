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
        'search_read',
        [['type', '=', 'product'],['categ_id.parent_id', '=', 71], ['description_sale', '!=', False]],
        { 'fields': ['name', 'default_code', 'description_sale', 'description', 'create_date'], 'order': 'create_date' })

    # Django pagination
    paginator = Paginator(data, 12)
    pages = paginator.get_page(page)

    context = {
        "products": pages
    }
    
    return render(request, 'pages/index.html', context)

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