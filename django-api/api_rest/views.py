from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

import json

@api_view(['GET'])
def get_products(request):

    if request.method == 'GET':

        products = Product.objects.all()           

        serializer = ProductSerializer(products, many=True)  
        
        return Response(serializer.data)      
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_by_id(request, id_product):

    try:
        product = Product.objects.get(pk=id_product)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST','PUT','DELETE'])
def product_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['product']:           
                
                id_product = request.GET['product']        
                
                try:
                    product = Product.objects.get(pk=id_product)  
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = ProductSerializer(product)          
                return Response(serializer.data)           
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    if request.method == 'POST':

        new_product = request.data
        
        serializer = ProductSerializer(data=new_product)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


    if request.method == 'PUT':

        id_product = request.data['id_product']

        try:
            updated_product = Product.objects.get(pk=id_product)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(updated_product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'DELETE':

        try:
            product_to_delete = Product.objects.get(pk=request.data['id_product'])
            product_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



