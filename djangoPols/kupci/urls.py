from django.urls import path
from . import views

app_name = 'kupci'
# Path definiton
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/edit/', views.ResultView.as_view(), name='result'),
]

""" Class Based DeatilView expects parameter to be called pk """
