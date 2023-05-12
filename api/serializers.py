from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=20)
    
    def create(self,validate_data):
        return Employee.objects.create(**validate_data)