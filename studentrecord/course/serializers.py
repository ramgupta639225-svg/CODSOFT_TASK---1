from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    def vailidate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Name cannot be blank')
        pass

    def validate_code(self, value):
        code = value
        existing = Course.objects.filter(code=code)
        if existing:
            raise serializers.ValidationError('Code already exists')
        return code

    class Meta:
        model = Course
        fields = '__all__'




