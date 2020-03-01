from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('produkt/<int:id>/', views.single_product, name='single_product'),
]