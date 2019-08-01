
from django.core.paginator import Paginator
# Importing api_connection from root project to bring api variables
from api_connection import *
import random

# Template function to query api taking arguments
api_template = lambda model, operation, query='', fields='' : models.execute_kw(db, uid, password, model, operation,[query], fields)

def context_limit():
    # Template api function parameters
    model = 'product.template'
    operation = 'search_read'
    query =[['type', '=', 'product'],['categ_id.parent_id', '=', 71], ['description_sale', '!=', False]]
    fields = { 'fields': ['name', 'default_code', 'description_sale', 'description', 'create_date'], 'order': 'create_date' }

     # Template api function
    data_limit = api_template(model, operation, query, fields)

    context_limit = {
        "products": data_limit
    }
    return context_limit

def context_detail(id):
# Template api function parameters
    model = 'product.template'
    operation = 'search_read'
    query = [['type', '=', 'product'],['categ_id.parent_id', '=', 71],['id', '=', id]]
    fields = {'fields': ['id', 'name', 'default_code', 'description_sale', 'description', 'attachment','create_date'] }

    # Template api function
    data_detail= api_template(model, operation, query, fields)

    context_detail = {
        "detail": data_detail[0]
    }

    return context_detail

def context_search(q):
    # Template api function parameters
    model = 'product.template'
    operation = 'search_read'
    # Query accepting q parameter requested in the view
    query = [['type', '=', 'product'],['categ_id', '=', 139],['x_studio_field_OaF3K', '=', True],['x_studio_field_OaF3K','ilike', q]]
    fields = {'fields': ['name', 'default_code', 'x_studio_field_QlEui'], 'limit': 12 }
    
    # Template api function
    data_search = api_template(model, operation, query, fields)

    context_search = {
        'products': data_search
    }

    return context_search

def create_product_lead(fullName, email, phone, description):
    # Template api function parameters
    model = 'crm.lead'
    operation = 'create'
    # Query accepting q parameter requested in the view
    query = {
       'name': 'compresoresaire.com',
       'contact_name': fullName,
       'email_from': email,
       'phone': phone,
       'description': description 
       }
    
    # Template api function
    api_template(model, operation, query)
    pass

def create_lead(fullName, email, phone, description):
    # Template api function parameters
    model = 'crm.lead'
    operation = 'create'
    # Query accepting q parameter requested in the view
    query = {
       'name': 'compresoresaire.com',
       'contact_name': fullName,
       'email_from': email,
       'phone': phone,
       'description': description 
       }
    
    # Template api function
    api_template(model, operation, query)
    pass
