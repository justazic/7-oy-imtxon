from django.urls import path
from .views import OrderCreateView, OrderListView,OrderDetailView,OrderStatusUpdateView, OrderCancelView

urlpatterns = [
    path('create/', OrderCreateView.as_view()),
    path('', OrderListView.as_view()),
    path('<int:id>/', OrderDetailView.as_view()),
    path('<int:id>/status/', OrderStatusUpdateView.as_view()),
    path('<int:id>/cancel/', OrderCancelView.as_view()),
]