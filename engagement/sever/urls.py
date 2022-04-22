from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('engage',views.engaged, name='engageapi'),
]
