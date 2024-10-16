from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True},}

    def create(self, validated_data):
        # handles secure creation of the user with password hashing
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],  # 'create_user' will hash the password
            role = validated_data['role']
        )
        return user

    def update(self, instance, validated_data):
        # Update username, email, and role
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        
        #check if password is being updated
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password) # hash the password before saving

        instance.save()
        return instance