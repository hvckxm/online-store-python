from django.urls import path

from web_shop.shop import views

urlpatterns = [
    path('', views.ProductListView.as_view())
]