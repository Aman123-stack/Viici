from rest_framework import serializers
from backend.models import User

# User Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','name','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError("password and confirm password does not match")
        return attrs
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)