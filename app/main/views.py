from django.shortcuts import render
from goods.models import Category

def index(request):

    content = {
        'title' : 'Home - Hand',
        'content' : 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', content)

def about(request):
    content = {
        'title' : 'About',
        'content' : 'About us',
        'text_on_page' : 'bla bla bla'
    }
    return render(request, 'main/about.html', content)