from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    page_size = 20
    default_limit = 20
    max_page_size = 100
