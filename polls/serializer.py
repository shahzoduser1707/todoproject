from rest_framework import serializers
from .models import todoModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoModel
        fields = ('__all__')
        