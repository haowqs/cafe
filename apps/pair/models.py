from django.db import models

# Create your models here.


class Customers(models.Model):

    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )

    name = models.CharField("姓名", max_length=20, default="god")
    gender = models.CharField("性别", max_length=20, choices=gender_choices)
    image = models.ImageField("用户头像", upload_to='image/%Y%m', default='image/default.png')
    hobby = models.CharField("爱好", max_length=1000, default="喝咖啡")
    life_maxim = models.CharField("人生格言", max_length=1000, default="宁愿做过了后悔，也不要错过了后悔。")

    class Meta:
        db_table = 'customers'
        verbose_name = '顾客'
        verbose_name_plural = verbose_name

