from rest_framework.viewsets import ModelViewSet
from .models import Job,Employee
from .serializers import JobSerializer,EmployeeSerializer
from .permissions import EmployeeTypeAuth
# Create your views here.

class EmployeeViewSets(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [EmployeeTypeAuth]

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
        
class JobViewSets(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [EmployeeTypeAuth]

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
        
