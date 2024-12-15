from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing and updating user information.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers']  # Prevent modifying the followers directly

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']  # Include only the necessary fields

    def create(self, validated_data):
        """
        Create and return a new user instance.
        """
        # Use the create_user method for creating a new user
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Automatically create an authentication token for the user
        Token.objects.create(user=user)
        return user

