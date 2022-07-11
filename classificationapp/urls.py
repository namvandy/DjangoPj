from django.urls import path

from classificationapp.views import hello_world

app_name = 'classificationapp'

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),
]