from rest_framework import serializers
from .models import Form, Formfield
from .models import Employee

class FormfieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formfield
        fields = '__all__'

class FormfieldNestedSerializer(serializers.ModelSerializer):

        fields = FormfieldSerializer(many=True, read_only=True)
        class Meta:
             model =Form
             fields =['id','name','fields']

class EmployeeSerializer(serializers.ModelSerializer):
     class Meta:
          model = Employee
          fields = '__all__'
          