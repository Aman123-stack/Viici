from rest_framework import serializers
from backend.models import User,Post

# User Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','Firstname','Lastname','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','Firstname','Lastname']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
