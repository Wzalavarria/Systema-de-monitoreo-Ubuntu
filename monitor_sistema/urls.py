from django.urls import path
from .views import sistema_view

urlpatterns = [
    path('', sistema_view, name='sistema'),
]
