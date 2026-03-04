from django.urls import path
from .views import CreateFormView, AddFieldView, ListFormView

urlpatterns = [
    path('form/create/', CreateFormView.as_view()),
    path('form/add/', AddFieldView.as_view()),
    path('form/',ListFormView.as_view()),
]
