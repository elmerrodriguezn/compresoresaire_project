from django.urls import path
from . import views

urlpatterns = [
    path('<category_id>/', views.index, name='products.category'),
    path('<category_id>/<product_id>/', views.detail, name='detail'),
    path('busqueda', views.search, name='search'),
    path('filter', views.filter, name='filter'),
    path('product_lead', views.lead, name='product_lead'),
]