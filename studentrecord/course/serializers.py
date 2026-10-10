from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Course name cannot be blank')
        return value.strip()

    def validate_code(self, value):
        code = value
        existing = Course.objects.filter(code=code)
        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise serializers.ValidationError('Course code already exists')
        return code



    def validate_duration(self, value):
        if  value <= 0:
            raise serializers.ValidationError('Course duration must be greater than 0')
        return value



    def validate_fee(self, value):
        if value <= 0:
            raise serializers.ValidationError('Course fee can not be negative')
        return value

    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {"code": {"validators": []}}

