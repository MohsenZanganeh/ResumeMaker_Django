from rest_framework.permissions import BasePermission, SAFE_METHODS
from . import views
from .models import Employee 
from django.contrib.auth.models import AnonymousUser

class EmployeeTypeAuth(BasePermission):
    def has_permission(self,request,view):
        if isinstance(request.user,AnonymousUser):
            return False

        special_views = [
            type(views.JobViewSets())
        ]

        user_type = request.user.user_type
        
        if user_type == 'C' and request.method in SAFE_METHODS:
            return True

        if user_type == 'E':
            
            employee = Employee.objects.filter(user_id=request.user.id).exists()
            if employee and request.method == 'POST':
                if type(view) in special_views:
                    return True
                return False

            return True
        

        return False
