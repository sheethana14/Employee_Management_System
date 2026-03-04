from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Form, Formfield
from .serializers import FormfieldSerializer, FormfieldNestedSerializer
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


class CreateFormView(generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class= FormfieldSerializer
    permission_classes =[permissions.IsAuthenticated]

class AddFieldView(generics.CreateAPIView):
    queryset = Formfield.objects.all()
    serializer_class= FormfieldSerializer
    permission_classes =[permissions.IsAuthenticated]

class ListFormView(generics.ListAPIView):
    queryset = Formfield.objects.all()
    serializer_class= FormfieldSerializer
    permission_classes =[permissions.IsAuthenticated]

class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
      search = self.request.query_params.get('search')
      queryset = Employee.objects.all()
      if search:
          queryset= queryset.filter(data_icontains= search)
      return queryset

class DeleteEmployeeView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
