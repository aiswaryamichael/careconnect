from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
 from doctors.permissions import IsAdminUserOrReadOnly
# Create your views here.
#API VIEWS for

#Creating doctor

#Reading all doctors
from rest_framework.response import Response
from rest_framework import status
from doctors.serializers import DoctorSerializer
from doctors.models import Doctor
from rest_framework.views import APIView
class DoctorListCreate(APIView):
    authentication_classes=[BasicAuthentication] #username,password
    permission_classes=[IsAdminUserOrReadOnly]
    #listing all doctors
    def get(self,request):
        d=Doctor.objects.all()
        serializer_instance=DoctorSerializer(d,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer_instance=DoctorSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#Reading a specific doctor

#Updating a doctor

#Deleting a doctor
class DoctorRetrieveUpdateDelete(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes=[BasicAuthentication] #username/password
    def get(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        self.check_object_permissions(request, d)

        serializer_instance=DoctorSerializer(d)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)

        self.check_object_permissions(request,d)

        serializer_instance=DoctorSerializer(instance=d,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        self.check_object_permissions(request, d)
        d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#filtering doctors based on specialization
#Filtering based on specialization
class DoctorFilter(APIView):
    def get(self,request):
        data=request.query_params.get('search')

        d=Doctor.objects.filter(specialization=data)

        serializer_instance=DoctorSerializer(d,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

from doctors.serializers import UserSerializer
#APiview for creating admin user
class AdminRegister(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

