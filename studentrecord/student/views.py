from django.shortcuts import render

from .models import Student
# Create your views here.
from .serializers import StudentSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import StudentPagination


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter,
                       ]


    search_fields = ['name', 'email', 'department']
    ordering_fields = ['name']
    filterset_fields = ['name', 'age']
    pagination_class = StudentPagination


