from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products.index'),
    path('<int:id>/', views.single, name='single'),
    path('busqueda', views.search, name='search'),
    path('product_lead', views.lead, name='product_lead'),
]