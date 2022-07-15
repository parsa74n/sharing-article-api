from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegisterView,UserListView,UserDetailView


app_name='accounts'
urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'), #url for login
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'), # url for refreshing token


    path('register/',UserRegisterView.as_view(),name='register'),
    path('list/',UserListView.as_view(),name='list'),
    path('detail/<int:pk>/',UserDetailView.as_view(),name='user-detail')
    
]
