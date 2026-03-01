from django.shortcuts import render
from rest_framework import generics, permissions
from.serializers import RegSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

class Regview(generics.CreateAPIView):
    queryset =User.objects.all()
    serializer_class = RegSerializer
    permission_classes =[permissions.AllowAny]

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user =request.user
        return Response({
            'username':user.username,
            'email': user.email
        })

