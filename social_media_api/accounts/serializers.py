from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers', 'following']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
            token = Token.objects.create(user=user)
        return user, token

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)
