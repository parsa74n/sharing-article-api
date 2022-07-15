from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class UserPaginator(PageNumberPagination):
    page_size=5