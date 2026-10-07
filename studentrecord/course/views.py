from .models import Course
from .paginations import CoursePagination
from .serializers import CourseSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,
                        filters.SearchFilter,
                        filters.OrderingFilter,
                        ]

    filterset_fields = ['name', 'code', 'duration_unit']
    search_fields = ['name', 'code', 'duration']
    ordering_fields = ['name']
    pagination_class = CoursePagination





