from django.db import models

class Record(models.Model):
    # 学号
    username = models.CharField(max_length=10)

    # 日期
    date = models.CharField(max_length=10)