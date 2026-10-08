from django.urls import path, include
from .views import EnrollmentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'enrollments', EnrollmentViewSet)




urlpatterns = [
    path('', include(router.urls)),

]


