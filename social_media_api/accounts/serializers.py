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
        read_only_fields = ['followers']  # Prevent modifying followers directly


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    # Explicitly define the password field as a CharField
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']  # Include required fields

    def create(self, validated_data):
        """
        Create and return a new user instance, using the create_user method.
        """
        # Ensure we use the manager's create_user method for proper password hashing
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  # Handle optional email
            password=validated_data['password']
        )
        # Automatically create an auth token for the new user
        Token.objects.create(user=user)
        return user

