from requests import post
from json import loads

def editinfo(phone, email, request):
    phone = str(phone)
    email = str(email)
    userKey = request.session['userKey']
    url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/appLogin/editPhoneOrEmail.action'
    datas = {
        'phone': phone,
        'email': email,
        'userKey':userKey,
        'identity': 0
    }
    r = post(url, data=datas)
    request.session['data']['account_email'] = email
    request.session['data']['mobile_phone'] = phone
    return {
        'code': 0,
        'msg': "修改个人信息成功！"
    }