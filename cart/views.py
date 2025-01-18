from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from shop.models import PopularityVote, Product
from .serializers import AddToCartSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def add_to_cart(request):
    serializer = AddToCartSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        # increment product popularity
        product_id = serializer.validated_data['product_id']
        product = Product.objects.get(id=product_id)
        vote, created = PopularityVote.objects.get_or_create(product=product, user=request.user)
        if created:
            vote.count = 1
        else:
            vote.count += 1
        vote.save()
        return Response({
            'message': 'Product added to cart successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
