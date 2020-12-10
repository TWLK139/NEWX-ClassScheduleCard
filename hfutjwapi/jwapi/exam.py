from requests import post
from json import loads

def getExam(semester, request):
    semester = str(semester)
    userKey = request.session['userKey']
    url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/course/getExamArrangement.action'
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
    exam = post(url, data=datas).text
    exam = loads(exam)['obj']['business_data']
    return {
        'code': 0,
        'data': exam
    }