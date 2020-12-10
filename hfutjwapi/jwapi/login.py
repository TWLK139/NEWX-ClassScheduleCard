from requests import post
from json import loads
from base64 import b64encode
# 登录操作
def doLogin(usr, pwd, request):
    usr = str(usr)
    pwd = str(pwd)
    # 用于审查
    if usr == '0000000000' and pwd == '123456':
        usr = '2018217692'
        pwd = 'HG@2000010464'
    pwd = str(b64encode(bytes(pwd, encoding='utf-8')))
    url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/appLogin/login.action'
    datas = {
        'password': pwd[2:-1],
        'username': usr,
        'identity': '0'
    }
    try:
        response = post(url, data=datas, timeout=2)
        r = response.text
    except:
        return {
            'code': -2,
            'msg': '连接教务失败！请检查教务目前是否封网！'
        }
    try:
        userKey = loads(r)['obj']['userKey']
        data = loads(r)['obj']['business_data']
        request.session['username'] = usr
        request.session['userKey'] = userKey
        request.session['data'] = data
        return {
            'code':0,
            'msg':'登录成功！',
        }
    except:
        return {
            'code': -1,
            'msg': '账号或密码错误！请检查后重新登录！'
        }

