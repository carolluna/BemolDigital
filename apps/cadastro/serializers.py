from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'birth', 'cep', 'street', 'home_number', 'neighborhood', 'city', 'phone', 'uf', 'email', 'passw']
