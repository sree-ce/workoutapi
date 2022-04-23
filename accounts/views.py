from django.shortcuts import get_object_or_404, render
from accounts.serializers import RegisterSerializer, RegisterSerializerTrainer
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from accounts.models import Customer, User
from accounts.serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['POST'])
def customer_registration(request):
    
        
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration successfull'
            data['username'] = account.username
            data['email'] = account.email
            
            refresh = RefreshToken.for_user(account)
            data['token'] = { 

                'refresh':str(refresh),
                'access':str(refresh.access_token),
            }
   
        else:
            return Response(serializer.errors)
        
        return Response(data)





class profile_viewsets(viewsets.ModelViewSet):
    # def profile_update(self,request,pk):
        permission_classes = [IsAuthenticated]
        queryset =  Customer.objects.all()
        # profile = get_object_or_404(queryset,pk=pk)
        serializer_class = ProfileSerializer
        # return Response(serializer_class.data)



@api_view(['POST'])
def trainer_registration(request):

    if request.method == 'POST':
        serializer = RegisterSerializerTrainer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration successfull'
            data['username'] = account.username
            data['email'] = account.email
            
            refresh = RefreshToken.for_user(account)
            data['token'] = { 
                'refresh':str(refresh),
                'access':str(refresh.access_token),
            }


        else:
            return Response(serializer.errors)
        
        return Response(data)

