
from datetime import datetime
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import time

# 定義一個黑名單
ban = {}
BAN_SECOND = 2 # 3秒內
BAN_LIMIT = 10 # 請求超過10次
BAN_TIME = 60 # 被ban 60秒

# 經過順序 先process_request->process_view->view->process_response
class ProcessViewNoneMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        # print("aaa")
        self.get_response = get_response

    # def __call__(self, request):
    #     print("bbb")
    #     return self.get_response(request)

    def process_request(self, request):
        # 取IP
        IP = str(request.META.get("REMOTE_ADDR"))
        # 如果第一次來，只紀錄
        if ban.get(IP) is None:
            ban[IP] = {"total": 1, "time": int(time.time())}
        print(ban[IP].get("total"))
        if ban[IP]["time"] > int(time.time()) - BAN_SECOND:
            print("三秒內")
            if ban[IP]["total"] > BAN_LIMIT:
                ban[IP]["ban"] = int(time.time()) + BAN_TIME
                return self.ban_response
            ban[IP]["total"] += 1
        else:
            tm = ban[IP].get("ban")
            if tm is not None and tm > int(time.time()):
                return self.ban_response
            del ban[IP]
    
    @property
    def ban_response(self):
        return HttpResponse("你已經被Ban", status=403) # 403 Forbidden

    def process_view(self, request, view_func, view_args, view_kwargs):
        # view_func 指的就是客戶端通過urls.py指到哪個view的方法
        return None
    
    def process_response(self, request, response):
        print('---33333')
        return response

    def process_exception(self,request, exception):
        pass
        # Logic executed if an exception/error occurs in the view