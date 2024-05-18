from django.core.paginator import Paginator
from django.http.request import HttpRequest


class PaginatorFilter:
    def pagination(self, request: HttpRequest):
        query_params = request.GET.dict()
        s_f_s = query_params["s_f"].replace("[", "").replace("]", "").split(",")
        s_s = query_params["s"].replace("[", "").replace("]", "").split(",")
        page = query_params["page"]
        perPage = query_params["perPage"]
        filter = dict(zip(s_f_s, s_s))
        ## paginator = Paginator(self.__class__.objects.filter(**filter).values(), perPage)
        ## page_obj = paginator.get_page(0)
        ## data = [kw for kw in page_obj.object_list]
        ## payload = {
        ##     "page": {
        ##         "current": page_obj.number,
        ##         "has_next": page_obj.has_next(),
        ##         "has_previous": page_obj.has_previous(),
        ##         "total_page": page_obj.end_index(),
        ##         "next_page": page_obj.next_page_number()
        ##     },
        ##     "data": data
        ## }
        return list(self.__class__.objects.filter(**filter).values())
