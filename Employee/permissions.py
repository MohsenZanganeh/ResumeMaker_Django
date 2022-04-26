from rest_framework.permissions import BasePermission, SAFE_METHODS
from . import views
from .models import Employee 

class EmployeeTypeAuth(BasePermission):
    def has_permission(self,request,view):
        
        special_views = [
            type(views.JobViewSets())
        ]
        
        if request.user.user_type == 'C' and request.method in SAFE_METHODS:
            return True

        if request.user.user_type == 'E':
            employee = Employee.objects.get(user_id=request.user.id)
            if employee is not None and request.method == 'POST':
                if type(view) in special_views:
                    return True

                return False
            return True
        

        return False
