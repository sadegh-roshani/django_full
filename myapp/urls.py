from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.index, name='index'),
    path('create/', views.create, name='create'),

]

