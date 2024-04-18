from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineViewSet, ProductionLogViewSet, OEEViewSet

router = DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'productionlogs', ProductionLogViewSet)
router.register(r'oee', OEEViewSet, basename='oee')

urlpatterns = [

    path('', include(router.urls)),

]