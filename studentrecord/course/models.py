from django.db import models
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(null=False)
    duration = models.PositiveIntegerField(null=False)
    duration_unit = models.CharField(max_length=10, choices=[
                                                                ('day', 'Day'),
                                                                ('week', 'Week'),
                                                                ('month', 'Month')
                                                            ]
                                     )
    fee = models.DecimalField(max_digits=10,decimal_places=2, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
