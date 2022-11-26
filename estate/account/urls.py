from django.urls import path

from . import views
from django.contrib import admin

from django.contrib.auth import views as auth_views

from ppty import views as ppty_view

urlpatterns = [
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('profile',views.profile, name='profile'),
    path('Buy_property',ppty_view.Buy_property_page, name='buy_property'),
    path('Mortgage_property',ppty_view.Mortgage_property_page, name='Mortgage_property'),
    path('Rent_property',ppty_view.Rent_property_page, name='Rent_property'),
    path('Sale_property',ppty_view.Sale_property_page, name='Sale_property'),
    path('setting',views.setting, name='setting'),
    path('500/page-does-not-exist-error/page/', admin.site.urls),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path('add-properties',views.add_properties, name='add-properties'),


  # reset password urls
    path('change_password/<token>/',views.change_password, name='change_password'),
    path('forget_password',views.forget_password, name='forget_password'),

    ####
]