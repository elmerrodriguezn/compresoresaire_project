from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products.index'),
    path('<int:id>/', views.single, name='single'),
    path('busqueda', views.search, name='busqueda'),
    path('product_lead', views.lead, name='product_lead'),
]