from pprint import pprint
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions  import CandidateTypeAuth
from .models import Candidate,Language,Skill,WorkExperience
from .serializers import CandidateSerializer,LanguageSerializer,SkillSerializer,WorkExperienceSerializer
# Create your views here.

class CandidateViewSet(CreateModelMixin,UpdateModelMixin,GenericViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [CandidateTypeAuth]
    
    @action(detail=False)
    def me(self,request):
        candidate = get_object_or_404(Candidate,user_id = request.user.id)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class WorkExperienceViewSet(CreateModelMixin,UpdateModelMixin,GenericViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [CandidateTypeAuth]

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
        
class SkillViewSet(CreateModelMixin,UpdateModelMixin,GenericViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [CandidateTypeAuth]

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
        
class LanguageViewSet(CreateModelMixin,UpdateModelMixin,GenericViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [CandidateTypeAuth]

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)