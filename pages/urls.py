# pages/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('kent/', kentPageView, name='kent'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results')
]
