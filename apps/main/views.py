from django.shortcuts import render, get_object_or_404
from .models import Volume, Article  # Assuming you create these
from django.urls import reverse

def home_view(request):
    return render(request, 'main/home.html')

def board_view(request):
    return render(request, 'main/board.html')

def volume_list_view(request):
    volume_list = Volume.objects.all()
    context = {
        'volume_list': volume_list,
        'breadcrumbs' : [
            {'label': 'Home', 'url': 'home'},
            {'label': 'Archives', 'url': None},
        ], 
        'active_tab' : 'archives',
    }
    return render(request, 'main/volume.html', context )

def article_list_view(request, volume_id):
    volume = get_object_or_404(Volume, pk=volume_id)
    article_list = Article.objects.filter(volume=volume_id)
    context = {
        'article_list' : article_list,
        'volume' : volume,
        'breadcrumbs' : [
            {'label':'Home', 'url':'home'},
            {'label':'Archives', 'url':'volume_list'},
            {'label': f'Volume {volume.number}', 'url': None},
        ],
        'active_tab' : 'archives',
    }
    return render(request, 'main/article_list.html', context)

def article_detail_view(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)
    volume = article_detail.volume

    context = {
    'article_detail': article_detail,
    'breadcrumbs': [
        {'label': 'Home', 'url': 'home'},
        {'label': 'Archives', 'url': 'volume_list'},
        {'label': f'Volume {volume.number}', 'url': 'article_list', 'args': [volume.pk]},
        {'label': article_detail.title[:50] + '...', 'url': None},
    ],
    'active_tab': 'archives',
    }
    return render(request, 'main/article_detail.html', context)

def submission_view(request):
    return render(request, 'main/submission.html')

def contact_view(request):
    return render(request, 'main/contact.html')