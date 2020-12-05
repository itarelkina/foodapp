from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    # /food/
    path ( '', views.index, name='index' ),
    # /food/1
]
