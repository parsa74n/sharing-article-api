from rest_framework.pagination import PageNumberPagination


class ArticlePaginator(PageNumberPagination):

    """
    custom paginator for list of articles
    """
    page_size = 4
