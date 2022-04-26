from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('candidate', views.CandidateViewSet, basename='candidate')
router.register('work_experience', views.WorkExperienceViewSet, basename='work_experience')
router.register('skill', views.SkillViewSet, basename='skill')
router.register('language', views.LanguageViewSet, basename='language')

urlpatterns = router.urls