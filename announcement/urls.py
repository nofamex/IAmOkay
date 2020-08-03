from django.urls import path
from . import views

app_name = 'announcement'

urlpatterns = [
    path('', views.landing, name='landing'),
]