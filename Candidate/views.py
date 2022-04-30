from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .permissions import CandidateTypeAuth
from .mixins import ViewSetModelCustomized
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Candidate,Language,Skill,WorkExperience
from .serializers import CandidateSerializer,LanguageSerializer,SkillSerializer,WorkExperienceSerializer
# Create your views here.

class CandidateViewSet(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin,GenericViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [CandidateTypeAuth]
    
    @action(detail=False,methods=['GET'])
    def me(self,request):
        candidate = get_object_or_404(Candidate,user_id = request.user.id)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)
    

class WorkExperienceViewSet(ViewSetModelCustomized):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class SkillViewSet(ViewSetModelCustomized):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer  

class LanguageViewSet(ViewSetModelCustomized):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer