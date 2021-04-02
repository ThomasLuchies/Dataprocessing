from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'classifications', views.ClassificationViewSet)
router.register(r'impacts', views.ImpactViewSet)
router.register(r'orbits', views.OrbitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]