from .models import CustomUser, Token
from rest_framework import serializers
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.is_active = False
        user.save()
        confirm = Token.objects.create(user=user)
        self.send_confirmation_email(user.email, confirm.token)
        return user

    def send_confirmation_email(self, email, token):
    
        confirm_link = f"http://127.0.0.1:8000/auth/{token}"
        send_mail(
            "confirm your email",
            f"verification token: {confirm_link}",
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [email]
                  )
        
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email = email, password = password)
        if not user:
            raise serializers.ValidationError("invalid credentials")
        if not user.is_email_confirmed:
            raise serializers.ValidationError("email is not confirmed")
        data['user'] = user
        return data

