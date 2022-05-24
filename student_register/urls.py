from django.urls import path
from .views import index, student_delete, student_add_update

urlpatterns = [
    path('', index, name='home'),
    path('add/', student_add_update, name='add'),
    path('update/<int:id>', student_add_update, name='update'),
    path('delete/<int:id>', student_delete, name='delete'),
]