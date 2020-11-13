from django.urls import path

from .views import *

urlpatterns = [
    path('', LogPageView.as_view(), name='log'),
]
