from rest_framework import serializers
from .models import Candidate,Language,Skill,WorkExperience

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','national_id','detail','career','gender']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id','language','level','Candidate']

    def Candidate(self):
        return Candidate.objects.get(user_id = self.context['request'].user.id)

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','skill','level','Candidate']

    def Candidate(self):
        return Candidate.objects.get(user_id = self.context['request'].user.id)

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id','title','company_name','start_date','end_date','Candidate']

    def Candidate(self):
        return Candidate.objects.get(user_id = self.context['request'].user.id)