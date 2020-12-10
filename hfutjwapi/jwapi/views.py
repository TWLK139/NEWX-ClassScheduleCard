from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from jwapi.login import doLogin
from jwapi.kick import kickdevices
from jwapi.isLogin import status
from jwapi.schedule import getSchedule
from jwapi.score import getScore
from jwapi.editInfo import editinfo
from jwapi.info import getInfo
from jwapi.exam import getExam
from jwapi.now import getNow
from jwapi.semestercodes import getCodes
from jwapi.records import getRecords
from jwapi.scheduleprocess import process

# 学期对应字典
semesters = {
    "037": "2020-2021学年第一学期",
    "036": "2019-2020学年第二学期",
    "035": "2019-2020学年第一学期",
    "034": "2018-2019学年第二学期",
    "033": "2018-2019学年第一学期",
    "032": "2017-2018学年第二学期",
    "031": "2017-2018学年第一学期",
    "030": "2016-2017学年第二学期",
    "029": "2016-2017学年第一学期"
}


# 首页显示
def index(request):
    # 判断是否已登录
    isLogin = status(request)
    if isLogin['code'] == 2:
        return HttpResponse("<h1>Hello HFUTApi!<br>这里是默认首页</h1>")
    elif isLogin['code'] == -2:
        return HttpResponse("<h1>Hello HFUTApi!<br>这里是默认首页<br>教务断网中。。。</h1>", status=500)
    else:
        return HttpResponse("<h1>你好," + request.session['data']['user_name'] + "!</h1>")


# 登录
def login(request):
    # 判断是否已登录
    isLogin = status(request)
    if isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    if isLogin['code'] == 3:
        request.session.flush()
        # return JsonResponse(isLogin)
    # 进行登录操作
    uesrname = request.POST.get('username')
    password = request.POST.get('password')
    getLogin = doLogin(uesrname, password, request)
    return JsonResponse(getLogin)


# 踢出已登录端
def kick(request):
    # 判断是否已登录
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    kicknow = kickdevices(request)
    return JsonResponse(kicknow)


# 注销登录
def logout(request):
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    request.session.flush()
    return JsonResponse({
        'code': 0,
        'msg': '注销成功！'
    })


# 获取课表
def schedule(request):
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    weekIndx = request.POST.get('weekIndx')
    semestercode = request.POST.get('semestercode')
    schedule = getSchedule(weekIndx, semestercode, request)
    return JsonResponse(schedule)


# 获取课表(新)
def getschedule(request):
    week = ''
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    semestercode = request.POST.get('semestercode')
    schedule = getSchedule(week, semestercode, request)
    result = process(schedule['data'])
    return JsonResponse(result)
    # return HttpResponse(result['data'])


# 获取成绩
def score(request):
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    semestercode = request.POST.get('semestercode')
    score = getScore(semestercode, request)
    return JsonResponse(score)


# 获取考试安排
def exam(request):
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    semestercode = request.POST.get('semestercode')
    exam = getExam(semestercode, request)
    return JsonResponse(exam)


# 修改个人信息
def edit(request):
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    editResult = editinfo(phone, email, request)
    return JsonResponse(editResult)


# 个人信息
def info(request):
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    info = getInfo(request)
    return JsonResponse(info)


# 当前信息
def now(request):
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    now = getNow(request)
    return JsonResponse(now)


# 获取静态数据
def normaldatas(request):
    with open("./static/data.json", encoding='utf-8') as f:
        data = f.read()
    try:
        semestercode = request.GET.get('semestercode')
        for i in eval(data)['data']:
            if int(semestercode) == int(i['code']):
                result = {
                    'code': 0,
                    'msg': '查询成功!',
                    'data': i
                }
                return JsonResponse(result)
        result = {
            'code': 1,
            'msg': '查询失败!'
        }
        return JsonResponse(result)

    except:
        return JsonResponse(eval(data))


# 获取某个人经历过的学期
def scodes(request):
    isLogin = status(request)
    if isLogin['code'] == 2:
        return JsonResponse(isLogin)
    elif isLogin['code'] == -2:
        return JsonResponse(isLogin, status=500)
    codes = getCodes(request)
    return JsonResponse(codes)


# 获取使用记录
def getrecords(request):
    records = getRecords()
    return JsonResponse(records)


# 工作室报名状态获取
def getapplystatus(request):
    try:
        with open("status.txt", "r") as f:
            statusinfo = eval(f.read())
            applystatus = int(statusinfo['status'])
            version = int(statusinfo['version'])
        if applystatus == 0:
            return JsonResponse({
                'status': 0,
                'msg': '报名系统处于开放状态',
                'version': version
            })
        elif applystatus == -1:
            return JsonResponse({
                'status': -1,
                'msg': '报名系统已关闭',
                'version': version
            })
        else:
            exit(0)

    except:
        return JsonResponse({
            'status': 1,
            'msg': '出现异常！',
            'version': version
        })


# 工作室报名状态设置
def setapplystatus(request):
    with open("status.txt", "r") as f:
        statusinfo = eval(f.read())
    if request.method == 'GET':
        return render(request, 'setstatus.html', {'status': statusinfo['status'], 'version': statusinfo['version']})
    elif request.method == 'POST':
        status = str(request.POST.get('status'))
        version = request.POST.get('version')
        try:
            if status:
                statusinfo['status'] = 0 if status == 'true' else -1
            if version or version == 0:
                statusinfo['version'] = int(version)
            with open("status.txt", "w", encoding="utf-8") as f:
                f.write(str(statusinfo))
            return JsonResponse({
                'code': 0,
                'msg': '修改成功！'
            })
        except:
            return JsonResponse({
                'code': 1,
                'msg': '出现异常！'
            })
