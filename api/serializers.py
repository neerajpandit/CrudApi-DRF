from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=20)
    
    def create(self,validate_data):
        return Employee.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    def validate_roll(self, value):
        if value>=200:
            return serializers.ValidationError('Seat Full')
        return value
    
    #object Level Validation

    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='neeraj' and ct.lower() !='abp':
            raise serializers.ValidationError('City must be abp')
        return data
