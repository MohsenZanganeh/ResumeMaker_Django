from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin,DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from django.core.exceptions import PermissionDenied
from .models import Job,Employee
from .serializers import JobSerializer,EmployeeSerializer
from .permissions import EmployeeTypeAuth
# Create your views here.

class EmployeeViewSets(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin,GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [EmployeeTypeAuth]
    
class JobViewSets(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet,ListModelMixin):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [EmployeeTypeAuth]

    def destroy(self, request, *args, **kwargs):
        job = Job.objects.select_related('Employee').get(pk=kwargs['pk'])
        if request.user.id == job.Employee.user_id:            
            return super().destroy(request, *args, **kwargs)
        raise PermissionDenied()

        
