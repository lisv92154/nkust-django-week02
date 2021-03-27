from django.db import models
from django.utils import timezone
#資料庫
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)#CharField 字元欄位
    vid = models.CharField(max_length=20, default= "dT2uJr2rJOE")
    pub_date = models.DateTimeField(default=timezone.now) #timezone.now 目前server時間

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
