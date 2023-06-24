from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from backend.models import User
from backend.serializers import UserRegistrationSerializer,UserLoginSerializer
class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        email=serializer.validated_data.get('email')
        if serializer.is_valid(raise_exception=True):
            if User.objects.filter(email=email).first():
                return Response({'Message':'User with this email already exist'},status=status.HTTP_400_BAD_REQUEST)
            else:
                user=serializer.save()
                password=serializer.data.get('password')
                hashed_password = make_password(password)
                user=User(password=hashed_password)
            return Response({'Message':'Registration Succesfull'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            
            user=authenticate(email=email,password=password)
            if user is not None:
                return Response({'message':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
