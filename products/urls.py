from django.urls import path
from .views import ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView,ProductSearchView,ProductCommentListView,ProductCommentCreateView,CommentListView,CommentUpdateView,CommentDeleteView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('search/', ProductSearchView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('<int:pk>/update', ProductUpdateView.as_view()),
    path('<int:pk>/delete', ProductDeleteView.as_view()),
    
    
    path('<int:id>/comments/', ProductCommentListView.as_view()),
    path('<int:id>/comments/add/', ProductCommentCreateView.as_view()),
    path('comments/', CommentListView.as_view()),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view()),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view()),
]