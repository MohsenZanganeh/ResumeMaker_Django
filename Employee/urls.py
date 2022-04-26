from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('employee', views.EmployeeViewSets, basename='employee')
router.register('job', views.JobViewSets, basename='job')

urlpatterns = router.urls