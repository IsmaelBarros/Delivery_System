from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<int:id>", views.category, name="category"),
    path("product/<int:id>", views.product, name="product"),
]
