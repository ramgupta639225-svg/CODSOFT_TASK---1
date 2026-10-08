# Create your views here.
from rest_framework import viewsets, filters
from .models import Enrollment
from .serializers import EnrollmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import EnrollmentPagination

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    filter_backends = [
                       DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter
    ]


    search_fields = [ 'status', 'student__name', 'student__email', 'course__name', 'course__code']
    ordering_fields = [ 'status', 'id']
    filterset_fields = [ 'student', 'course', 'status']
    pagination_class = EnrollmentPagination

