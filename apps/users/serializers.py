from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Defines the model
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_student')
        extra_kwargs = {'password': {'write_only': True, 
                'min_length': 8,
                #This is for the web
                'style': {'input_type': 'password'}}}

    #This is called when POST is coming
    def create(self, validated_data):
        is_student = validated_data.pop('is_student')
        user = models.User.objects.create_user(
            email = validated_data['email'],
            password=validated_data['password'],
        )
        user.is_student = is_student
        user.save()
        return user
