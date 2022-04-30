from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin

from .permissions import AppliedJobAuth
from .serializers import AppiedJobSerializer,EmployeeAppiedJobSerializer
from .models import Applied_Job
from Employee.models import Employee,Job
from Candidate.models import Candidate
# Create your views here.

class Applied_jobViewSet(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin,GenericViewSet):
    queryset = Applied_Job.objects.all()
    serializer_class = AppiedJobSerializer
    permission_classes = [AppliedJobAuth]

    def get_queryset(self):
        if self.request.user.user_type == 'E':
            employee = Employee.objects.get(user_id=self.request.user.id)
            job = Job.objects.filter(Employee_id = employee.id).values_list('pk', flat=True)
            print('=====list(job):',job)

            return Applied_Job.objects.filter(job__in = job)
        
        if self.request.user.user_type == 'C':
            candidate = Candidate.objects.get(user_id=self.request.user.id)
            return Applied_Job.objects.filter(candidate_id = candidate.id)

    def get_serializer_context(self):
        return {'request': self.request}
    
    def get_serializer_class(self):
        if self.request.user.user_type == 'E':
            return EmployeeAppiedJobSerializer
        return AppiedJobSerializer
        