# from django.shortcuts import render
# from accounts.models import Customer,User
# from rest_framework.response import Response
# from Users.serializers import ProfileSerializer
# from rest_framework.decorators import api_view

# # Create your views here.
# @api_view(["GET","PUT"])
# def profile_view(request,pk):

#     if request.method == "GET":
        
#         try:
#             profile = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({'error':'profile does not exist'})
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     if request.method == "PUT":
    
#         profile = User.objects.get(pk=pk)
#         serializer = ProfileSerializer(profile,data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

    

# @api_view(['POST'])
# def workout_view(request):
#     if request.method == 'POST':
#         pass
