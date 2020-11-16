from rest_framework.pagination import PageNumberPagination
from common_lib.response import SuccessResponse
from common_lib.exceptions import InvalidPageException
from collections import OrderedDict


class Pagination(PageNumberPagination):
    page_size = 10  # 默认每页显示的数量
    max_page_size = 100  # 每页显示的最大数量
    page_query_param = 'page'  # 搜索的参数关键字
    page_size_query_param = 'size'  # 控制每页显示数量的关键字

    # max_page_size = 100
    # page_query_param = 'current'
    # page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):
        # return Response({
        #     'total': self.page.paginator.count,
        #     'pageSize': self.get_page_size(self.request),
        #     'current': self.page.number,
        #     'data': data
        # })

        return SuccessResponse(
            OrderedDict([('total', self.page.paginator.count),
                         ('pageSize', self.get_page_size(self.request)),
                         ('current', self.page.number),
                         ('next', self.get_next_link()),
                         ('previous', self.get_previous_link()),
                         ('data', data)]))

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except Exception as e:
            raise InvalidPageException(str(e))  # change this

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)
