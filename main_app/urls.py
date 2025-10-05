from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<str:name>', views.my_page, name='my_page'),
]