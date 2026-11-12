from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authtoken.models import Token


# Create your views here.
#API VIEWS for

#Creating doctor

#Reading all doctors
from rest_framework.response import Response
from rest_framework import status

from doctors.models import Doctor
from rest_framework.views import APIView
from patients.serializers import AppointmentSerializer
#Appointment create View
from datetime import time,datetime,timedelta
from patients.models import Appointment
class AppointmentCreate(APIView):
        authentication_classes = [BasicAuthentication,]
        permission_classes=[IsAuthenticated]  #only authenticated users can
                                              #create appointment
        def post(self, request):
            serializer_instance = AppointmentSerializer(data=request.data)
            if serializer_instance.is_valid():
                #Token_number
                data=serializer_instance.validated_data #data after validation

                d=data['doctor'] #fetches doctor from client data
                date=data['appointment_date']#fetches date from client data
                token=0
                appointment_time=time(9,0,0)  #9am
                print(appointment_time)
                #find the doctor appointments on that particular date using filter query
                a=Appointment.objects.filter(doctor=d,appointment_date=date).last() #find the last record


                if a:#if found
                    token=a.token_number+1

                    appointment_time=(datetime.combine(date,a.appointment_time)+timedelta(minutes=15)).time()
                else:#if no record
                    token=1

                #appointment time

                serializer_instance.save(token_number=token,appointment_time=appointment_time)
                response={
                      "message":"Booking Confimed Successfully",
                    "booking_data":serializer_instance.data
                }

                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

#Api view for creating a user
class PatientRegister(APIView):
    def post(self,request):
        pass




#model(default -User)
#serializer
#view
#path


class obtain_auth_token(APIView):
    def post(self,request):

        #fetches  the username and password from user data

        u=request.data['username']
        p=request.data['password']

        #checks whether matching user exits in user table

        user=authenticate(username=u,password=p)
            # authenticate() checks whether user exists or not
            #if matching user exists it returns user object
            #else none


        #if user exists
        if user:
            #generates token and sends as response
            token,created=Token.objects.get_or_create(user=user)
            print(token,created)
            return Response({'token':token.key},status=status.HTTP_201_CREATED)

        #else
        else:
            #sends response as invalid user credential
            return Response({'token':'Invalid Credentials,Unable to login'},status=status.HTTP_400_BAD_REQUEST)








