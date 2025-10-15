from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<str:name>', views.user_page, name='user_page'),
    path('create', views.create_page, name='create'),
    path('cabinet', views.cabinet, name='cabinet'),

    #examples
    path('bill_gates', views.bill_gates, name='bill_gates'),
    path('curtis_james_jackson', views.curtis_james_jackson, name='curtis_james_jackson'),
    path('leonardo_dicaprio', views.leonardo_dicaprio, name='leonardo_dicaprio'),
    path('homer_jay_simpson', views.homer_jay_simpson, name='homer_jay_simpson'),
    path('matthew_david_mcconaughey', views.matthew_david_mcconaughey, name='matthew_david_mcconaughey'),
]