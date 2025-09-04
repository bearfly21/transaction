from django.shortcuts import render
from .serializers import *
from accounts.models import CustomUser
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response



class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data =request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)
            refresh["email"] = user.email
            return Response(
                {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id":user.id,
                    "email": user.email
                    }
                }
            )
        return Response(serializer.errors, status=400)
    

class ConfirmedEmailView(APIView):
    def get(self, request, token):
        token = Token.objects.get(token = token)
        user = token.user
        user.is_email_confirmed = True
        user.is_active = True
        user.save()
        token.delete()
        return Response("email confirmed")