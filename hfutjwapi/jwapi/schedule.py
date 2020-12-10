from requests import post
from json import loads

def getSchedule(week, semester, request):
    week = str(week)
    semester = str(semester)
    userKey = request.session['userKey']
    url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/schedule/getWeekSchedule.action'
    if week == '':
        datas = {
            'userKey': userKey,
            'identity': '0',
            'projectId': '23',
            'semestercode': semester,
        }
    datas = {
        'userKey': userKey,
        'identity': '0',
        'projectId': '23',
        'semestercode': semester,
        'weekIndx': week
    }
    sc = post(url, data=datas).text
    schedule = loads(sc)['obj']['business_data']
    return {
        'code':0,
        'data':schedule
    }