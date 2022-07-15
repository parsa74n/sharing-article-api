from django.urls import path
from .views import CreateArticleView, ListArticleView, DeleteArticleView, DetailArticleView, PartialUpdateArticleView, UpdateArticleView


app_name = 'article'

urlpatterns = [
    path('create/', CreateArticleView.as_view(), name='create-article'),
    path('list/', ListArticleView.as_view(), name='article-list'),
    path('delete/<int:pk>/', DeleteArticleView.as_view(), name='delete'),
    path('detail/<int:pk>/', DetailArticleView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateArticleView.as_view(), name='update'),
    path('update/partial/<int:pk>/',
         PartialUpdateArticleView.as_view(), name='partial-update'),
]
