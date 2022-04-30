from rest_framework.permissions import BasePermission
from Employee.models import Employee

class AppliedJobAuth(BasePermission):
    def has_permission(self,request,view):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS','PUT')
        user_type = request.user.user_type

        if user_type == 'C' and (request.method in ('PUT','PATCH')) == False:
            return True

        if user_type == 'E':
            employee = Employee.objects.filter(user_id=request.user.id).exists()
            if employee:
                if request.method == 'POST':
                    return False
                if request.method in ('PUT', 'DELETE'):
                    pass
                return True
            else:
                if request.method == 'POST':
                    return False

                if request.method in ('PUT','DELETE'):
                    pass
        return False