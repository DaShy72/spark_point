from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<str:name>', views.user_page, name='user_page'),
    path('create', views.create_page, name='create'),
    path('cabinet', views.cabinet, name='cabinet'),
]