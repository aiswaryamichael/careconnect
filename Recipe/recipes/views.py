from functools import partial

from django.core.serializers import serialize
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import recipes
from recipes.models import Recipes
from recipes.serializers import RecipeSerializer


# NON-PRIMARY KEY BASED

class ListCreateRecipeView(APIView):

    def get(self,request):

        qs=Recipes.objects.all()
        serializer_instance=RecipeSerializer(qs,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):

        serializer_instance=RecipeSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


# PRIMARY KEY BASED

class DetailUpdateDeleteRecipeView(APIView):

    def get(self, request,pk):

        e=get_object_or_404(Recipes,id=pk)
        serializer_instance=RecipeSerializer(e)
        return Response(serializer_instance.data)

    def put(self, request,pk):

        e=get_object_or_404(Recipes,id=pk)
        serializer_instance=RecipeSerializer(instance=e,data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk):
        e = get_object_or_404(Recipes, id=pk)
        serializer_instance = RecipeSerializer(instance=e, data=request.data,partial=True)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        e=get_object_or_404(Recipes,id=pk)
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Search

from rest_framework.filters import SearchFilter
from rest_framework import generics

class SearchAPIView(generics.ListAPIView):
    def get(self,request):
        data=request.query_params.get('search')
        print(data)

        m=Recipes.objects.filter(Q(recipe_name__icontains=data) |
                                 Q(ingredients__icontains=data))

        serialize_instance=RecipeSerializer(m,many=True)





