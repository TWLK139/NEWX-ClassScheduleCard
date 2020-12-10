from django.http import JsonResponse, HttpResponse
from requests import post


# 登录状态检测
def status(request):
    url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/appLogin/login.action'
    try:
        post(url, timeout=2)
    except:
        # exit(0)
        return {
            'code': -2,
            'msg': '连接教务失败！请检查教务目前是否封网！'
        }
    try:
        request.session['userKey']
        return {
            'code': 3,
            'msg': '已经登录！'
        }
    except:
        return {
            'code': 2,
            'msg': '你还没登录！'
        }
