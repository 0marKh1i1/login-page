from rest_framework import serializers
from django.contrib.auth import get_user_model , authenticate
from rest_framework.exceptions import ValidationError


UserModel = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        user_obj = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],)
        user_obj.save()
        return user_obj
            
                                                 
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    ##
    def check_user(self, validated_data):
        user = authenticate(
            username=validated_data['username'], 
            password=validated_data['password'])
        if not user:
            raise ValidationError('Invalid Credentials')
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username',)