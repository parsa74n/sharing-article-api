from operator import imod
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from .models import Article
from accounts.permissions import IsOwnerPermission
from django.shortcuts import get_object_or_404
from .paginator import ArticlePaginator


class CreateArticleView(APIView):
    """
    view for creating article. just authenticated users can create articles.
    """

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = request.POST
        ser_data = ArticleDetailSerializer(data=data)
        if ser_data.is_valid():
            Article.objects.create(title=ser_data.validated_data['title'],
                                   description=ser_data.validated_data['description'],
                                   owner=request.user)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors)


class ListArticleView(APIView,ArticlePaginator):
    """
    view for list of articles. everyone can see this view.

    """

    def get(self, request):
        
        data = Article.objects.all()
        results = self.paginate_queryset(data, request, view=self)
        ser_data = ArticleListSerializer(
            instance=results, many=True, context={'request': request})
        return self.get_paginated_response(ser_data.data)


class DeleteArticleView(APIView):
    """
    veiew for deleting article. just owner of article can delete article.
    """

    permission_classes = [IsOwnerPermission, ]

    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        self.check_object_permissions(request, article)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetailArticleView(APIView):
    """
    view for article detail. everyone can see this view.

    """
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        ser_data = ArticleDetailSerializer(instance=article)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class PartialUpdateArticleView(APIView):
    """
    view for partial update(patch method) of article. just owner of article can update the article.
    """

    permission_classes = [IsOwnerPermission, ]

    def patch(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        self.check_object_permissions(request, article)
        ser_data = ArticleDetailSerializer(
            instance=article, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateArticleView(APIView):
    """
    view for update (put method) of article. just owner of article can update the article.
    """

    permission_classes = [IsOwnerPermission, ]

    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        self.check_object_permissions(request, article)
        ser_data = ArticleDetailSerializer(instance=article, data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
