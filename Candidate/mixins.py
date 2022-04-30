from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied
from .permissions import CandidateTypeAuth
from .models import Candidate


class ViewSetModelCustomized(ModelViewSet):
    permission_classes = [CandidateTypeAuth]
    
    def create(self, request, *args, **kwargs):
        candidate = Candidate.objects.get(user_id=request.user.id)
        request.data._mutable = True
        request.data['Candidate'] = candidate.id
        return super().create(request, *args, **kwargs)
        
    def destroy(self, request, *args, **kwargs):
        get_object = self.get_queryset().get(pk=kwargs['pk'])
        candidate = Candidate.objects.get(user_id=request.user.id)
        if candidate.id == get_object.Candidate_id:
            return super().destroy(request, *args, **kwargs)
        raise PermissionDenied()

    def update(self, request, *args, **kwargs):
        get_object = self.get_queryset().get(pk=kwargs['pk'])
        candidate = Candidate.objects.get(user_id=request.user.id)
        request.data._mutable = True
        request.data['Candidate'] = candidate.id
        if candidate.id == get_object.Candidate_id:
            return super().update(request, *args, **kwargs)
        raise PermissionDenied()
    
    def get_serializer_context(self):
        return {'request': self.request}
