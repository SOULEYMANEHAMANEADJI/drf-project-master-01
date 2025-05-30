from django.db import models

# Create your models here.

class Gender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True, unique=True)
    ninea = models.CharField(max_length=20, default="EMP001")
    emp_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, default="Software Design")
    emp_dob = models.DateField()
    emp_gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE
    )

    def __str__(self):
        return self.emp_name