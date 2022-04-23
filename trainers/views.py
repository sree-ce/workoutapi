from django.shortcuts import render
from rest_framework.views import APIView
from trainers.models import Workouts
from trainers.serializers import WorkoutSerializer
from rest_framework.response import Response
from rest_framework import viewsets, parsers
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# class WorkoutView(APIView):
    
#     def post(self,request):
#         serializers = WorkoutSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)


class WorkoutViewset(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    queryset = Workouts.objects.all()
    serializer_class = WorkoutSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']