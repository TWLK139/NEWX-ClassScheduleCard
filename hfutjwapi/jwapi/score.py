from requests import post
from json import loads

def getScore(semester, request):
    semester = str(semester)
    userKey = request.session['userKey']
    url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/course/getSemesterScoreList.action'
    if semester == 'all':
        datas = {
            'projectId': '23',
            'userKey': userKey,
            'identity': '0',
        }
    else:
        datas = {
            'projectId': '23',
            'userKey': userKey,
            'identity': '0',
            'semestercode': semester
        }
    cj = post(url, data=datas).text
    scores = loads(cj)['obj']['business_data']['semester_lessons']
    return {
        'code': 0,
        'data': scores
    }