from jwapi.models import Record

def getRecords():
    records = list(Record.objects.all().values())
    records.sort(key=lambda keys:keys['id'], reverse=True)
    length = Record.objects.all().count()
    return {
        'code' : 0,
        'count' : length,
        'data' : records
    }