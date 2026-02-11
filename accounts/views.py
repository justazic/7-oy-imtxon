from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignUpSerializer,ProfileUpdateSerializer


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
                'status': status.HTTP_201_CREATED,
                'username': user.username,
                'message': 'Akkount yaratildi'
        })
        
        
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user =  authenticate(username=username, password=password)
        if not user:
            raise ValidationError({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Login yoki parol xato'
            })
            
        refresh = RefreshToken.for_user(user)
        return Response({
            'status':status.HTTP_200_OK,
            'refresh':str(refresh),
            'access': str(refresh.access_token),
            'message': 'Tizimga kirdingiz'
        })
        
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'message': 'Refresh token tuborilmadi', 'status': status.HTTP_400_BAD_REQUEST})
        
        token = RefreshToken(refresh_token)
        token.blacklist()
        
        return Response({'message': 'Siz tizimdan chiqdingiz'})
    
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user =  request.user
        return Response({
            'status': status.HTTP_200_OK,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })
        
        
class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        serializer = ProfileUpdateSerializer(instance=request.user,data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'status': status.HTTP_200_OK,
            'username': user.username,
            'message': 'Profil toliq yangilandi'
        })
    
    def patch(self, request):
        serializers = ProfileUpdateSerializer(instance=request.user, data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        return Response({
            'status': status.HTTP_200_OK,
            'username': user.username,
            'message': 'Profil yangilandi'
        })
        
        
class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not user.check_password(old_password):
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Eski parol xato'
            })
            
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Parol yangilandi'})
    