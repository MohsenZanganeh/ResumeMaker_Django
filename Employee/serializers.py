from rest_framework import serializers
from django.core.exceptions import PermissionDenied
from .models import Employee,Job

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','company_name','Employee_members']

    def update(self, instance, validated_data):
        employee = Employee.objects.get(user_id=self.context['request'].user.id)
        if employee.id == instance.id:            
            return super().update(instance, validated_data)
        raise PermissionDenied()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title','description','Employee']
    
    def create(self, validated_data):
        employee = Employee.objects.get(user_id=self.context['request'].user.id)
        validated_data['Employee'] = employee
        return super().create(validated_data)

    def update(self, instance, validated_data):
        employee = Employee.objects.get(user_id=self.context['request'].user.id)
        validated_data['Employee'] = employee
        if employee.id == instance.Employee.id:            
            return super().update(instance, validated_data)
        raise PermissionDenied()

        