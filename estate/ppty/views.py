from django.shortcuts import render
# from django.http import HttpResponse

# from .models import * 
from .models import Location, Buy_property, Sale_property, Rent_property, Mortgage_property
from ppty.models import Buy_property, Sale_property, Rent_property, Mortgage_property

# Create your views here.

def index(request):

    locts = Location.objects.all()

    # loct1 = Location()
    # loct1.name = 'Ajah' 
    # loct1.ppty = 'Duplex'
    # loct1.img = 'property-1.jpg'
    # loct1.features = False

    # loct2 = Location()
    # loct2.name = 'Festac' 
    # loct2.ppty = '3Bed Room Flat of 2unit'
    # loct2.img = 'property-2.jpg'
    # loct2.features = False

    # loct3 = Location()
    # loct3.name = 'Lekki' 
    # loct3.ppty = 'Semi-Detached Duplex'
    # loct3.img = 'property-3.jpg'
    # loct3.features = False

   

    # loct4 = Location()
    # loct4.name = 'Festac' 
    # loct4.ppty = '3Bed Room Flat of 2unit'
    # loct4.img = 'property-4.jpg'
    # loct4.features = 'False'

    # loct5 = Location()
    # loct5.name = 'Lekki' 
    # loct5.ppty = 'Semi-Detached Duplex'
    # loct5.img = 'property-3.jpg'
    # loct5.features = True

    # locts = [loct1, loct2, loct3, loct4, loct5]
   


    
    return render(request, "index.html", {'locts': locts})


# def index(request):
    # return render(request, "index.html", {"name": 'TOLA HOMES'})

def Buy_property_page(request):
    all_properties = Buy_property.objects.all()


    return render(request, "Buy_property.html", {'all_properties': all_properties})

def Sale_property_page(request):
    all_properties = Sale_property.objects.all()


    return render(request, "Sale_property.html", {'all_properties': all_properties})

def Mortgage_property_page(request):
    all_properties = Mortgage_property.objects.all()


    return render(request, "Mortgage_property.html", {'all_properties': all_properties})

def Rent_property_page(request):
    all_properties = Rent_property.objects.all()


    return render(request, "Rent_property.html", {'all_properties': all_properties})



def pay_with_paystack(request):
    return render(request, 'paystack_payment.html', {'name':'paystack'})

def about_us(request):
    return render(request, 'about-us.html', {'name':'about'})

def add_properties(request):
    return render(request, 'add-properties.html', {'name':'add-properties'})

def contact_us(request):
    return render(request, 'contact-us.html', {'name':'contact-us'})

def dashboard(request):
    return render(request, 'dashboard.html', {'name':'dashboard'})





