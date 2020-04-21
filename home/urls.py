from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:note_id>/', views.note, name='note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete-note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit-note'),
    path('pdf/<int:note_id>/', views.save_pdf, name='pdf-note'),
]
