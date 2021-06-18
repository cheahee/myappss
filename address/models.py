from django.db import models

# Create your models here.
class Address(models.Model):
    # idx(필드명,컬럼명) = 자료형(속성)
    idx = models.AutoField(primary_key=True)
    # 길이제한, 빈값을 허용, nulll값 허용
    name = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)