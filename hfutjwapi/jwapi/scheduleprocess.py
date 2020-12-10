from requests import post
from json import loads

def process(schedule):
    courses = []
    codes = set()
    for course in schedule:
        codes.add(course['lesson_code'])
    for code in codes:
        courses.append(getdata(code))
    return {'data':courses}

def getdata(code):
    url = 'http://lesson.newxstudio.com/lesson/public/index.php/index/courses'
    res = post(url, data={
        'number':code
    }).text
    return loads(res)['data']