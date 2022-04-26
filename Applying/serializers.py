from rest_framework import serializers
from .models import Applied_Job
from Candidate.models import Candidate
from Employee.models import Job

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applied_Job
        fields = ['id','job','candidate']

    Job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())
