from rest_framework import serializers
from .models import Product,Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        source='category', 
        write_only=True
    )
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'category_id', 'image']
        
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'product']