from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):

    """
    serializer for list of articles.
    the serializer includes link of article detail and includes username of owner's article
    """

    article_link = serializers.HyperlinkedIdentityField(
        view_name='article:detail')
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        model = Article
        fields = ['title', 'owner', 'article_link']


class ArticleDetailSerializer(serializers.ModelSerializer):

    """
    serializer for articles detail.
    """

    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        model = Article
        fields = ['title', 'description', 'owner', 'created', 'updated']
