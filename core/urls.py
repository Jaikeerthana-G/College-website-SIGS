from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admission/', views.admission, name='admission'),
    path('faculty/', views.faculty, name='faculty'),
    path('gallery/bca/', views.gallery_bca, name='gallery_bca'),
    path('gallery/bca-ai/', views.gallery_bca_ai, name='gallery_bca_ai'),
    path('gallery/bcom/', views.gallery_bcom, name='gallery_bcom'),
]
