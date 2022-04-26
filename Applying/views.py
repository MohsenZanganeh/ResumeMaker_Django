from rest_framework.viewsets import ModelViewSet
from .models import Applied_Job

# Create your views here.

class Applied_jobViewSet(ModelViewSet):
    queryset = Applied_Job.objects.all()
    # serializer_class = AppliedJobSerializer()

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
