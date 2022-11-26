from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    # path('add',views.add, name='add'),
    path('payment',views.pay_with_paystack, name='paystack-payment'),
    path('about',views.about_us, name='about-us'),
    path('add_properties',views.add_properties, name='add-properties'),
    path('contact-us',views.contact_us, name='contact-us'),
    

]