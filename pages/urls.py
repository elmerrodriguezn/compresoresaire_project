from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contact, name="contact"),
    path('send_lead/', views.send_lead, name='send_lead'),
    path('gracias-por-contactarnos/', views.thanks, name='thanks'),
]