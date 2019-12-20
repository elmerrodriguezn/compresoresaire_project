from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from api.query import Query
from modules.recaptcha import recaptcha
import xmlrpc.client


def index(request, category_id):
    page = request.GET.get('page', 1)

    query = Query()

    data = query.get(
        'product.template',
        'search_read',
        [
            ['type', '=', 'product'],
            ['x_studio_field_tGMk6', '=', True],
            ['categ_id', '=', int(category_id)]
        ],
        {
            'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'categ_id', 'create_date'],
            'order': 'create_date'
        }
        )

    paginator = Paginator(data, 20)

    pages = paginator.get_page(page)

    context = {"products": pages}

    if data[0]['categ_id'][0] in [72, 73, 74]:
        return render(request, 'products/compressors/index.html', context)
    if data[0]['categ_id'][0] in [80, 83]:
        return render(request, 'products/parts/index.html', context)


def detail(request, category_id, product_id):
    query = Query()

    data = query.get(
        'product.template',
        'search_read',
        [
            ['type', '=', 'product'],
            ['x_studio_field_tGMk6', '=', True],
            ['id', '=', product_id],
        ],
        {
            'fields':
                [
                    #Brand -> x_studio_field_04Kkp
                    #Tank -> x_studio_field_pxZa1
                    #Flow -> x_studio_field_pYf9c
                    #Model -> x_studio_field_RHdO5
                    #Power -> x_studio_field_ZY0DV
                    #Pressure -> x_studio_field_9fT7c

                    'id', 'name', 'default_code', 'description_sale',
                    'description', 'categ_id', 'create_date', 'qty_available',
                    'list_price', 'weight', 'x_studio_field_04Kkp', 'x_studio_field_RHdO5',
                    'x_studio_field_pxZa1', 'x_studio_field_ZY0DV', 'x_studio_field_pYf9c', 'x_studio_field_9fT7c',
                ]
        })

    context = {"product": data[0]}

    if data[0]['categ_id'][0] in [72, 73, 74]:
        return render(request, 'products/compressors/detail.html', context)
    if data[0]['categ_id'][0] in [80, 83]:
        return render(request, 'products/parts/detail.html', context)


def search(request):
    q = request.GET['q']

    query = Query()

    data = query.get(
        'product.template',
        'search_read',
        [
            ['type', '=', 'product'],
            ['categ_id.parent_id', 'in', [71, 79]],
            ['x_studio_field_tGMk6', '=', True],
            ['default_code', 'ilike', q]
        ],
        {
            'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'categ_id', 'create_date'],
            'limit': 20,
        })

    context = {"products": data}

    return render(request, 'products/search/index.html', context)


def filter(request):
    query = Query()

    value = None

    data = ''

    (hp, psig, cfm) = (request.GET['hp'], request.GET['psig'], request.GET['cfm'])

    if 'hp' in request.GET:
        hp = request.GET['hp']
        if hp:
            value = ['x_studio_field_ZY0DV', '=', hp]

    if 'psig' in request.GET:
        psig = request.GET['psig']
        if psig:
            value = ['x_studio_field_9fT7c', '=', psig]

    if 'cfm' in request.GET:
        cfm = request.GET['cfm']
        if cfm:
            value = ['x_studio_field_pYf9c', '=', cfm]

    try:
        data = query.get(
            'product.template',
            'search_read',
            [
                ['type', '=', 'product'],
                ['x_studio_field_tGMk6', '=', True],
                ['categ_id.parent_id', 'in', [71, 79]],
                value,
            ],
            {
                'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'categ_id', 'create_date'],
                'limit': 20})
    except Exception as ex:
        if isinstance(ex, xmlrpc.client.Fault):
            data = ''

    context = {"products": data}

    return render(request, 'products/search/index.html', context)


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


