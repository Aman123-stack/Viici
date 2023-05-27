from django.urls import path,include
from backend.views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register')
]
