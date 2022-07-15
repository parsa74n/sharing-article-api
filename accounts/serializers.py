from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        max_length=128, required=True, write_only=True)
    password2 = serializers.CharField(
        max_length=128, required=True, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'phone_number',
                  'email', 'password1', 'password2', 'gender']
        extra_kwargs = {'gender': {'required': False}}

    def validate(self, data):
        if data['password1'] and data['password2'] and data['password1'] != data['password2']:
            raise serializers.ValidationError("passwords does'nt match!!!")
        return data

    def validate_phone_number(self, data):
        for i in data:
            if not i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                raise serializers.ValidationError('invalid phone number!!')
        return data


class UserDetailSerializer(serializers.ModelSerializer):
    """
    detail serializer for users. this serializer includes links of user's articles.
    """
    articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='article:detail',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'articles','gender']


class UserListSerializer(serializers.ModelSerializer):
    user_link = serializers.HyperlinkedIdentityField(
        view_name='accounts:user-detail')

    class Meta:
        model = User
        fields = ['username', 'user_link']
