from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, UserListSerializer, UserDetailSerializer
from .models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .paginator import UserPaginator


class UserRegisterView(APIView):
    """
    view for registering 
    (every one can see this view)
    """

    def post(self, request):
        ser_data = UserSerializer(data=request.POST)
        print(ser_data)
        if ser_data.is_valid():
            user = User.objects.create_user(
                username=ser_data.validated_data['username'],
                phone_number=ser_data.validated_data['phone_number'],
                email=ser_data.validated_data['email'],
                password=ser_data.validated_data['password1'],
            )

            if ser_data.validated_data.get('gender'):
                user.gender = ser_data.validated_data.get('gender')
                user.save()

            return Response(ser_data.data)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView, UserPaginator):
    """
    view for listing users 
   (everyone can see this view) 
    """

    def get(self, request):
        users = User.objects.all()
        paginated_data = self.paginate_queryset(
            users, request=request, view=self)
        ser_data = UserListSerializer(
            instance=paginated_data, many=True, context={'request': request})
        return self.get_paginated_response(ser_data.data)


class UserDetailView(APIView):
    """
    view for user details 
    (everyone can see this view)
    """

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        ser_data = UserDetailSerializer(
            instance=user, context={'request': request})
        return Response(ser_data.data, status=status.HTTP_200_OK)
