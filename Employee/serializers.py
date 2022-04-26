from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee,Job

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','company_name','Employee_members']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title','description','Employee']

    def Employee(self):
        return Employee.objects.get(user_id = self.context['request'].user.id)