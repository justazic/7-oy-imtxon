from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Cart,CartItem
from .serializers import CartItemSerializer
from products.models import Product


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        items = cart.items.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)
    
    
class CartAddView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        if not created:
            item.quantity += 1
            item.save()
        
        return Response({'message': 'Mahsulot savatga qoshildi'})
    
    
class CartRemoveView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        product_id = request.data.get('product_id')
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        item.delete()
        
        return Response({'message': 'Mahsulot savatdan ochirildi'})
    
    
class CartClearView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart.items.all().delete()
        return Response({'message': 'Savat tozalandi'})
    
    
class CartUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        item.quantity = quantity
        item.save()
        
        return Response({'message': 'Mahsulot soni yangilandi'})
    