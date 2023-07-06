from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.views import APIView
from backend.models import UserManager,User
from backend.renderer import UserRenderer
from backend.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,PostSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.validated_data.get('email')
            if User.objects.filter(email=email).first():
                return Response({'Message':'User with this email already exist'},status=status.HTTP_400_BAD_REQUEST)
            else:
                user=serializer.save()
                token=get_tokens_for_user(user)
                password=serializer.data.get('password')
                user=User(password=password)
                user.set_password(user.password)
                return Response({'token':token,'Message':'Registration Succesfull'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # if useremail.alreadyexisted condition is met then
            # return response('user email already existed')
        
          # encrypted password code here
        
        

class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'message':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PostCreateView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message':'Posted Sucessfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
