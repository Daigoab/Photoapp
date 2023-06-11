from django.urls import path
from . import views

urlpatterns = [
    path('photoblogs/', views.photoblog, name = 'photoblogs' ),
    path('add_blog/', views.add_blog, name = 'add_blog' ),
    path('photodetails/<int:photo_id>/', views.photodetails, name = 'photodetails' ),
]