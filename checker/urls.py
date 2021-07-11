from django.urls import path
from .views import main, urls_create, urls_list

app_name = 'checker'

urlpatterns = [
    path('', main),
    path('urls_create', urls_create, name = 'urls_create'),
    path('urls_list', urls_list, name = 'urls_list'),
]
