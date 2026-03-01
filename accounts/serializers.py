from django.contrib.auth import get_user_model
User =get_user_model()
from rest_framework import serializers

class RegSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['username', 'email','password']
       kwargs ={'password':{'write_only':True}}

   def create(self,validated_data):
        return User.objects.create_user(
            username = validated_data['username'],
            email =validated_data['email'],
            password =validated_data['password']
        )