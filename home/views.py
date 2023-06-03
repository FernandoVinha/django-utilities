from django.shortcuts import render
from .models import CarouselSlide, MarketingItem, Featurette, Language
from django.contrib import messages
from django.utils.translation import get_language

def home(request):
    language = get_language()
    #print(language)
    
    #try:
    #    selected_language = Language.objects.get(code=language)
    #except Language.DoesNotExist:
    selected_language = Language.objects.get(code='pt')  # Use English as default language

    slides = CarouselSlide.objects.filter(language=selected_language)
    marketing_items = MarketingItem.objects.filter(language=selected_language)
    featurettes = Featurette.objects.filter(language=selected_language)
    
    context = {
        'slides': slides,
        'marketing_items': marketing_items,
        'featurettes': featurettes,
        'messages': messages.get_messages(request),
    }
    
    return render(request, 'home.html', context)