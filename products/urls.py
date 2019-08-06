from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.single, name='single'),
    path('busqueda', views.search, name='search'),
    path('filter', views.filter, name='filter'),
    path('product_lead', views.lead, name='product_lead'),
]