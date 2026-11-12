from django.db import models

# Create your models here.
from doctors.models import Doctor
class Appointment(models.Model):
    patient_name = models.CharField(max_length=20)

    age = models.IntegerField()

    gender_choices = (('male', 'Male'), ('female', 'Female'))

    gender = models.CharField(max_length=20)

    problem = models.TextField()
    phone = models.CharField(max_length=20)
    appointment_date = models.DateField() #appointmentdate

    appointment_time = models.TimeField(null=True)

    token_number = models.IntegerField(null=True)
    # Date in which  record is saved in db table


    created_at = models.DateTimeField(auto_now_add=True)

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)




