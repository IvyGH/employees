from django.urls import path

from .views import (
    EmployeeListView, EmployeeCreateView,
    EmployeeUpdateView, EmployeeDeleteView
)

urlpatterns = [
    path('', EmployeeListView.as_view(), name='list_employees'),
    path('create/', EmployeeCreateView.as_view(), name='add_employee'),
    path('<str:slug>/update/', EmployeeUpdateView.as_view(),
         name='update_employee'),
    path('<str:slug>/delete/', EmployeeDeleteView.as_view(),
         name='delete_employee'),
]
