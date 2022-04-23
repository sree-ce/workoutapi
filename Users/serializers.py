from rest_framework import serializers
from accounts.models import Customer, User
from .models import CustomerProfile



class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','name','email','username','mobile']
