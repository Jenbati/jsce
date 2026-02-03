from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.Dashboard_View.as_view(), name='dashboard'),
    path('author_dashboard/', views.Author_Dashboard_View.as_view(), name='author_dashboard'),

    # Profile view
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.user_profile, name='edit_profile'),
]