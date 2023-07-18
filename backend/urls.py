from django.urls import path
from backend.views import UserRegistrationView,UserLoginView,UserProfileView,PostCreateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('post/',PostCreateView.as_view(),name='UserPost')
]