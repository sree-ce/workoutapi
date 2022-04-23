from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from accounts.models import Trainer,Customer,User
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    name = serializers.CharField()
    mobile = serializers.CharField(validators=[mobile_regex])
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    height = serializers.IntegerField()
    health_condition = serializers.CharField()
    
    class Meta:
        model = User
    
        fields = ['name','password','email','username','mobile','age','weight','height','health_condition']

    def save(self):

        password = self.validated_data['password']
        

        if password is None:
            raise serializers.ValidationError({'error': 'password cannot be empty'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'],is_customer = True,mobile = self.validated_data['mobile'],name = self.validated_data['name'])
        account.set_password(password)
        account.save()
        Customer.objects.create(customer = account,age = self.validated_data['age'],weight = self.validated_data['weight'],height = self.validated_data['height'],health_condition = self.validated_data['health_condition'])
        return account




class RegisterSerializerTrainer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    name = serializers.CharField()
    mobile = serializers.CharField(validators=[mobile_regex])
    certification = serializers.CharField()
    stream = serializers.CharField()
    about = serializers.CharField()
    
    class Meta:
        model = User
    
        fields = ['name','password','email','username','mobile','certification','stream','about']

    def save(self):

        password = self.validated_data['password']
        

        if password is None:
            raise serializers.ValidationError({'error': 'password cannot be empty'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})

        trainer = User(email=self.validated_data['email'], username=self.validated_data['username'],is_trainer = True,mobile = self.validated_data['mobile'])
        trainer.set_password(password)
        trainer.save()
        Trainer.objects.create(trainer = trainer,certification = self.validated_data['certification'],stream = self.validated_data['stream'],about = self.validated_data['about'])
        return trainer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','username','mobile']


class ProfileSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only = True)
 
    class Meta:
        model = Customer
        fields = ['customer','age','weight','height','health_condition']
