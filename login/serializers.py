from rest_framework import serializers
from login.models import User


class UserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):

        username_exists = User.objects.filter(email=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User with Username Exists")

        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with Email Exists")
        
        return super().validate(attrs)