from rest_framework.permissions import BasePermission, SAFE_METHODS
from . import views
from .models import Candidate 

class CandidateTypeAuth(BasePermission):
    def has_permission(self,request,view):
        special_views = [
            type(views.WorkExperienceViewSet()),
            type(views.SkillViewSet()),
            type(views.LanguageViewSet())
        ]

        if request.user.user_type == 'E' and request.method in SAFE_METHODS:
            return True
        
        if request.user.user_type == 'C':
            candidate = Candidate.objects.get(user_id=request.user.id)
            if candidate is not None and request.method == 'POST':
                if type(view) in special_views:
                    return True

                return False
            return True
        

        return False