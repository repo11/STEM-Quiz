from rest_framework.routers import DefaultRouter
from .views import AttemptViewSet, QuestionViewSet, QuizViewSet
router=DefaultRouter(); router.register('questions',QuestionViewSet); router.register('attempts',AttemptViewSet,basename='attempts'); router.register('',QuizViewSet)
urlpatterns=router.urls
