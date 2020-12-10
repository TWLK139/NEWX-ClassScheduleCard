from requests import post
from json import loads
from time import strftime, localtime
from jwapi.models import Record
# 获取现在信息
def getNow(request):
    userKey = request.session['userKey']
    username = request.session['username']
    day = strftime("%Y-%m-%d", localtime())
    url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/publicdata/getSemesterAndWeekList.action'
    datas = {
        'userKey': userKey,
        'projectId': '23',
    }
    now = post(url, datas).text
    now = loads(now)['obj']['business_data']
    semestercode = now['cur_semester_code']
    weekIndx = now['cur_week_index'] - 1 if semestercode == '036' else now['cur_week_index']    #036学期周数比预定少1

    try:
        with open("status.txt", "r") as f:
            statusinfo = eval(f.read())
            applystatus = statusinfo['status']
            version = statusinfo['version']

    except:
        pass

    try:
        Record.objects.get(username=username, date=day)
    except:
        record = Record(
            username=username,
            date=day
        )
        record.save()


    return {
        'code':0,
        'semestercode':semestercode,
        'weekIndx':weekIndx,
        'applystatus':applystatus,
        'version':version
    }
