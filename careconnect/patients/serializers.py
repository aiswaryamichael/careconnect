from patients.models import Appointment


from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u




from datetime import datetime
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"
        read_only_fields=['id','appointment_time','token_number','created_at']

    def validate(self,validated_data):
        appointment_date=validated_data['appointment_date']
        todays_date=datetime.now().date()

        if appointment_date<todays_date:
            raise serializers.ValidationError("Invalid date")

        # 25 slot --> appointment full

        a=Appointment.objects.filter(d=validated_data['doctor'],appointment_date=appointment_date).last()
        if a:
            if a.token_number==25:
                raise serializers.ValidationError("slots full")

        # find the last record

        # check its token number reaches 25,if yes raise error

        return validated_data