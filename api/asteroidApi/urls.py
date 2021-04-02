from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'classification', views.ClassificationViewSet)
router.register(r'impact', views.ImpactViewSet)
router.register(r'orbit', views.OrbitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]