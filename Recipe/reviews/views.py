from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from reviews import serializers
from reviews.models import Review
from reviews.permissions import IsOwner
from reviews.serializers import ReviewSerializer


class CreateReview(APIView):

    #AUTHENTICATION AND PERMISSION

    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):

        print(request.user)

        u=request.user #current user object

        serializer_instance=ReviewSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save(user=u)
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class ReviewsView(APIView):
    def get(self,request,pk):

        qs=Review.objects.filter(recipe=pk)

        serializer_instance=ReviewSerializer(qs,many=True)

        return Response(serializer_instance.data,status=status.HTTP_200_OK)


#update review

class UpdateReview(APIView):

    #authentication

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]


    def put(self,request,pk):

        r=get_object_or_404(Review,id=pk)

        #manually checks if requested user has permissions to perform the following operation on review object r
        self.check_object_permissions(request,r)

        e=get_object_or_404(Review,id=pk)
        serializer_instance=ReviewSerializer(instance=e,data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



#delete review

class DeleteReview(APIView):
    def delete(self,request,pk):

        e=get_object_or_404(Review,id=pk)
        e.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


