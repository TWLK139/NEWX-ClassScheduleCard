def getInfo(request):
    data = request.session
    return {
        'code':0,
        'data':data['data']
    }