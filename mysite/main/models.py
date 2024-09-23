from django.db import models

# Create your models here.
class Notice(models.Model):
    # id = models.AutoField(primary_key=True)
    # 제목
    title = models.CharField(max_length=200)
    # 내용
    contents = models.TextField()
    # 조회수
    views = models.IntegerField()
    # 생성일
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Program(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    subtext = models.TextField()
    schedule =  models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.title