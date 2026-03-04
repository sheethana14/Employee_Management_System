from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Form, Formfield
from .serializers import FormfieldSerializer, FormfieldNestedSerializer

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



