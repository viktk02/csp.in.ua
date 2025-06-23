from django.shortcuts import render
from .models import CarouselImage, PartnerLogo, AboutUs, MainPage

def index(request):
    carousel_images = CarouselImage.objects.all()
    top_logos = PartnerLogo.objects.filter(row=1)
    bottom_logos = PartnerLogo.objects.filter(row=2)
    text = MainPage.objects.first()
    return render(request, 'main/home.html', {
        'carousel_images': carousel_images,
        'top_logos': top_logos,
        'bottom_logos': bottom_logos,
        'text': text
    })


def about(request):
    about_us = AboutUs.objects.first()
    return render(request, 'main/about.html',{
        'about_us': about_us
    })

def contacts(request):
    return render(request, 'main/contacts.html')

def custom_404_view(request, exception):
    print("Custom 404 handler triggered")
    return render(request, '404.html', status=404)


