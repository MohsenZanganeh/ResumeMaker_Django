from rest_framework import serializers
from .models import Applied_Job
from Candidate.models import Candidate
from Employee.models import Job,Employee

class AppiedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applied_Job
        fields = ['id','job','candidate']

    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
    def create(self, validated_data):
        candidate = Candidate.objects.get(user_id=self.context['request'].user.id)
        validated_data['candidate'] = candidate
        return super().create(validated_data)


class EmployeeAppiedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applied_Job
        fields = ['id','job','candidate','is_accepted']
        read_only_fields = ['job','candidate']
    
    is_accepted = serializers.BooleanField()
