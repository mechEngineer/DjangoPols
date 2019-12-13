from django.urls import path
from . import views

# Path definiton
urlpatterns = [
    path('', views.index, name='index'),
]
