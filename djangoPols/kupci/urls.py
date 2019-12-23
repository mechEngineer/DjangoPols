from django.urls import path
from . import views

app_name = 'kupci'
# Path definiton
urlpatterns = [
    path('', views.index_kupci, name='index'),
    path('novi/', views.TvrtkeCreateView.as_view(), name='tvrtka_nova'),
    # path('<int:pk>/edit/', views.ResultView.as_view(), name='result'),
]

""" Class Based DeatilView expects parameter to be called pk """
