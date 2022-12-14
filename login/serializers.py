from rest_framework import serializers
from login.models import User


class UserCreationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type'}, min_length=4, max_length=12, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': { 'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user
