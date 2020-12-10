from django.contrib.sessions.models import Session
from django.utils import timezone
from django.db.models import Q

def kickdevices(request):
    count = 0
    # 获取最新session_id
    session_key = request.session.session_key
    # 删除非当前设备session
    for session in Session.objects.filter(~Q(session_key=session_key), expire_date__gte=timezone.now()):
        data = session.get_decoded()
        if data.get('userKey', None) == str(request.session['userKey']):
            count+=1
            session.delete()
    return {
        'code':0,
        'msg':'共踢除'+str(count)+'台设备'
    }