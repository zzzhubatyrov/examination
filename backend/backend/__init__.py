from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class Custom_Pagination(PageNumberPagination):
    page_size_query = 'page'
    max_page_size = 30
    page_size = 30

    def get_paginated_response(self, data, status=status.HTTP_200_OK):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data,
        }, status=status)

