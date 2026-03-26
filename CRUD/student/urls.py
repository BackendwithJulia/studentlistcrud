from django.urls import path
from .views import create_student, update_student, student_list, delete_student

urlpatterns = [
    path('', student_list , name="list"),
    path('create/', create_student, name="create"),
    path('update/<int:primarykey>/', update_student, name="update"),
    path('delete/<int:primarykey>/', delete_student, name="delete")
]