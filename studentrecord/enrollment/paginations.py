from rest_framework.pagination import PageNumberPagination


class EnrollmentPagination(PageNumberPagination):
    page_size = 3