from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.category, name='category'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
]




