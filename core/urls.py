from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admission/', views.admission, name='admission'),
    path('faculty/', views.faculty, name='faculty'),
]
