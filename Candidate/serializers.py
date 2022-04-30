from rest_framework import serializers
from .models import Candidate,Language,Skill,WorkExperience
from django.core.exceptions import PermissionDenied
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','national_id','detail','career','gender']
    
    def update(self, instance, validated_data):
        if self.context['request'].user.id == instance.user.id:
            return super().update(instance, validated_data)
        raise PermissionDenied()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id','language','level','Candidate']
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','skill','level','Candidate']
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id','title','company_name','start_date','end_date','Candidate']