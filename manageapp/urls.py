from .views import ProjectViewSet, TodoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'todo', TodoViewSet)