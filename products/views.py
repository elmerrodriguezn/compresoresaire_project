from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from api.query import Query
from modules.recaptcha import recaptcha


def index(request, category_id):
    page = request.GET.get('page', 1)

    query = Query()

    data = query.get('product.template', 'search_read',
                     [['type', '=', 'product'], ['x_studio_field_tGMk6', '=', True],
                      ['categ_id', '=', int(category_id)]], {
                         'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'categ_id',
                                    'create_date']})

    paginator = Paginator(data, 20)

    pages = paginator.get_page(page)

    context = {"products": pages}

    return render(request, 'products/index.html', context)


def single(request, category_id, product_id):
    query = Query()

    #['categ_id.parent_id', '=', 71]

    data = query.get('product.template', 'search_read',
                     [
                         ['type', '=', 'product'], ['x_studio_field_tGMk6', '=', True],
                         ['id', '=', product_id],
                         ['categ_id', '=', int(category_id)]

                      ], {
                         'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'categ_id',
                                    'create_date', 'qty_available', 'list_price', 'weight']})

    context = {"product": data[0]}

    return render(request, 'products/single.html', context)


def search(request):
    q = request.GET['q']

    query = Query()

    data = query.get('product.template', 'search_read',
                     [['type', '=', 'product'], ['categ_id.parent_id', '=', 71], ['x_studio_field_tGMk6', '=', True],
                      ['name', 'ilike', q]], {
                         'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'categ_id',
                                    'create_date'], 'limit': 20})

    context = {"products": data}

    return render(request, 'products/search.html', context)


def filter(request):
    query = Query()

    value = ''

    if 'hp' in request.GET:
        hp = request.GET['hp']
        if hp:
            value = "{} HP".format(hp)

    if 'psig' in request.GET:
        psig = request.GET['psig']
        if psig:
            value = "{} PSIG".format(psig)

    if 'cfm' in request.GET:
        cfm = request.GET['cfm']
        if cfm:
            value = "{} CFM".format(cfm)

    data = query.get('product.template', 'search_read',
                     [['type', '=', 'product'], ['categ_id.parent_id', '=', 71], ['x_studio_field_tGMk6', '=', True],
                      ['description_sale', 'like', value]], {
                         'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'categ_id',
                                    'create_date'], 'limit': 20})

    context = {"products": data}

    return render(request, 'products/search.html', context)


def lead(request):
    if request.method == 'POST' and recaptcha(request):
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        description = \
            'Producto: ' + request.POST['product_name'], 'Número de parte: ' + request.POST['pn'], 'Mensaje: ' + request.POST['msg']

        query = Query()

        data = query.create('crm.lead', 'create',
                            {
                                'name': 'compresoresaire.com',
                                'user_id': 14,
                                'contact_name': full_name,
                                'email_from': email,
                                'phone': phone,
                                'description': description
                             })
        return redirect('thanks')
    else:
        return redirect('index')


