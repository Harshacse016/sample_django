from django.urls import path
from . import views

urlpatterns = [
    path('Home', views.home, name='home'),
    path('add',views.add,name="add"),
]
