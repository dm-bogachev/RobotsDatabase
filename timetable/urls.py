from django.urls import path

from .views import *

urlpatterns = [
    path('', StaffListView.as_view(), name='staff_list'),
    path('d', StaffDetailView.as_view(), name='staff_detail'),
]