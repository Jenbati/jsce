from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('board/', views.board_view, name='board'),
    path('volume_list/', views.volume_list_view, name='volume_list'),
    path('article_list/<int:volume_id>/', views.article_list_view, name='article_list'),
    path('article_detail/<int:article_id>/', views.article_detail_view, name='article_detail'),
    path('submission/', views.submission_view, name='submission'),
    path('contact/', views.contact_view, name='contact'),
]