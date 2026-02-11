from django.urls import path
from .views import SignUpView,LoginView,LogoutView,ProfileView,ProfileUpdateView,PasswordChangeView

urlpatterns = [
    path('register/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('profile/update/', ProfileUpdateView.as_view()),
    path('profile/reset_pass', PasswordChangeView.as_view()),
]