from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    def vailidate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Name can not be blank')
        return value

    def vailidate_email(self, value):
        email = value.strip().lower()
        existing = Student.objects.filter(email__iexact=email)
        if existing.exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_phone(self, value):
        import re
        if not re.fullmatch(r'(?:\+91)?[6-9]\d{9}', value):
            raise serializers.ValidationError(
                "Enter a valid 10-digit Indian mobile number, "
                "optionally with +91."
            )
        return value

    def validate_age(self, value):
        if not 1 <= value <= 100:
            raise serializers.ValidationError('Age must be between 1 and 100')
        return value

    class Meta:
        model = Student
        fields = '__all__'



