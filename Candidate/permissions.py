from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser
from . import views
from .models import Candidate


class CandidateTypeAuth(BasePermission):
    def has_permission(self, request, view):

        if isinstance(request.user, AnonymousUser):
            return False

        special_views = [
            type(views.WorkExperienceViewSet()),
            type(views.SkillViewSet()),
            type(views.LanguageViewSet())
        ]

        user_type = request.user.user_type

        if user_type == 'E' and request.method in SAFE_METHODS:
            return True

        if user_type == 'C':

            # candidate = Candidate.objects.filter(
            #     user_id=request.user.id).exists()

            # if candidate:
            #     if request.method == 'POST':
            #         if type(view) in special_views:
            #             return True
            #         return False

            #     if request.method in ('PUT', 'DELETE'):
            #         return True

            #     return True
            # else:
            #     if request.method == 'POST':
            #         if type(view) not in special_views:
            #             return True
            #         return False

            #     if request.method in ('PUT','DELETE'):
            #             return False

            return True