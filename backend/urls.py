from django.urls import path,include
from backend.views import UserRegistrationView,UserLoginView,UserProfileView,PostCreateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('<int:userid>/post',PostCreateView.as_view(),name='Post'),
]