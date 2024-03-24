# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    # path('results/<int:choice>/<str:gmat>/', results, name='results'),
    path('results/<int:age>/<int:height>/<int:weight>/<int:ap_hi>/<int:ap_lo>/<int:smoke>/<int:active>/', results, name='results')
]
