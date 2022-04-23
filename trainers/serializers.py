from rest_framework import serializers
from trainers.models import Workouts


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workouts
        exclude = ['created_at','updated_at']