from rest_framework import serializers
from .models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):



    def validate(self, data):
        student = data.get ('student', getattr(self.instance, 'student', None))
        course = data.get ('course', getattr(self.instance, 'course', None))

        existing = Enrollment.objects.filter(student=student, course=course)
        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise serializers.ValidationError("This student is already enrolled in this course")
        return data

    class Meta:
        model = Enrollment
        fields = '__all__'

