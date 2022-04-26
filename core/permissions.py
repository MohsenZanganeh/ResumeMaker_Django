from rest_framework.permissions import BasePermission, SAFE_METHODS

class CandidateTypeAuth(BasePermission):
    def has_permission(self,request,view):

        if request.user.user_type == 'E' and request.method == 'GET':
            return True

        if request.user.user_type == 'C':
            return True

        return False

class EmployeeTypeAuth(BasePermission):
    def has_permission(self,request,view):

        if request.user.user_type == 'C' and request.method == 'GET':
            return True

        if request.user.user_type == 'E':
            return True

        return False

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method == SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)