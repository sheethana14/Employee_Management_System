from django.urls import path
from .views import CreateFormView, AddFieldView, DeleteEmployeeView, ListFormView

urlpatterns = [
    path('form/create/', CreateFormView.as_view()),
    path('form/add/', AddFieldView.as_view()),
    path('form/',ListFormView.as_view()),
    path('employee/delete/<int:pk>/', DeleteEmployeeView.as_view())
]
