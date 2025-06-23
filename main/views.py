from django.shortcuts import render
from .models import CarouselImage, PartnerLogo, AboutUs, MainPage
from utils.secure_utils import generate_nonce, create_csp

def index(request):
    nonce = generate_nonce()
    carousel_images = CarouselImage.objects.all()
    top_logos = PartnerLogo.objects.filter(row=1)
    bottom_logos = PartnerLogo.objects.filter(row=2)
    text = MainPage.objects.first()
    csp = create_csp(nonce)
    response = render(request, 'main/home.html', {
        'carousel_images': carousel_images,
        'top_logos': top_logos,
        'bottom_logos': bottom_logos,
        'text': text,
        'nonce': nonce,
    })
    response['Content-Security-Policy'] = csp
    return response

def about(request):
    about_us = AboutUs.objects.first()
    nonce = generate_nonce()
    csp = create_csp(nonce)
    response = render(request, 'main/about.html',{'about_us': about_us, 'nonce': nonce, })
    response['Content-Security-Policy'] = csp
    return response

def contacts(request):
    nonce = generate_nonce()
    csp = create_csp(nonce)
    response = render(request, 'main/contacts.html',{'nonce': nonce, })
    response['Content-Security-Policy'] = csp
    return response

def custom_404_view(request, exception):
    print("Custom 404 handler triggered")
    nonce = generate_nonce()
    csp = create_csp(nonce)
    response = render(request, '404.html', status=404, context={'nonce': nonce})
    response['Content-Security-Policy'] = csp
    return response
