from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['username','first_name','last_name','email','is_active','is_staff','date_joined','is_superuser','groups','user_permissions','password','last_login']

