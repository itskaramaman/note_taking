from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:note_id>', views.note, name='note'),
]
