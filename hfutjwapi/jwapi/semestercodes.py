from requests import post
from json import loads

def getCodes(request):
    userKey = request.session['userKey']
    url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/course/getSemesterScoreList.action'
    datas = {
        'projectId': '23',
        'userKey': userKey,
        'identity': '0',
    }
    cj = post(url, data=datas).text
    scores = loads(cj)['obj']['business_data']['semester_lessons']
    codes = []
    for score in scores:
        dt = {}
        dt['code'] = score['code']
        dt['name'] = score['name']
        dt['season'] = score['season']
        dt['year'] = score['year']
        codes.append(dt)
    return {
        'code':0,
        'data':codes
    }



