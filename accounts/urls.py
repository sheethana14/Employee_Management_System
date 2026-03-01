from django.urls import path
from.views import Regview, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',Regview.as_view(), name='register'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('login/',TokenObtainPairView.as_view(), name='login'),
    path('refresh/',TokenRefreshView.as_view(), name='refresh'),
]
