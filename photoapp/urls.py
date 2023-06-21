from django.urls import path
from django.shortcuts import redirect
from . import views 
from .views import add_comment

urlpatterns = [
    path('photoblogs/', views.photoblog, name = 'photoblogs' ),
    path('add_blog/', views.add_blog, name = 'add_blog' ),
    path('photodetails/<int:photo_id>/', views.photodetails, name = 'photodetails' ),
    path('like/<int:photoblog_id>/', views.like_view, name='like'),
    path('photodetails/<int:photoblog_id>/like/', views.like_view, name='like'),
    path('add_comment/<int:photoblog_id>/', views.add_comment, name='add_comment'),
    path('create_profile/', lambda request: redirect('photoblogs/'), name='create_profile'),
]