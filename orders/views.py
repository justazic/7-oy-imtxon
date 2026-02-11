from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer

# Create your views here.


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        cart = get_object_or_404(Cart, user=request.user)
        
        if not cart.items.exists():
            return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Savat bosh' 
            })
            
        order = Order.objects.create(user=request.user)
        
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.items.all().delete()
        return Response({'message': 'Buyurtma yaratildi'})
    
    
class OrderListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)    
            

class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        order = get_object_or_404(Order, id=id, user=request.user)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    
class OrderStatusUpdateView(APIView):
    permission_classes = [IsAdminUser]
    
    def patch(self, request, id):
        order = get_object_or_404(Order, id=id)
        status_value = request.data.get('status')
        
        order.status = status_value
        order.save()
        
        return Response({'message': 'Status yaratildi'})
    
    
class OrderCancelView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        order = get_object_or_404(Order, id=id, user=request.user)
        order.delete()
        return Response({'message': 'Buyurtma bekor qilindi'})