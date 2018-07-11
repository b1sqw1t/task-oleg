from django.db import models
from django.contrib.auth import settings


class Cat(models.Model):
    class Meta:
        verbose_name = ('Кот')
        verbose_name_plural = ('Коты')

    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Хозяин')
    Name = models.CharField(max_length=30, verbose_name='Кличка')
    Age = models.PositiveSmallIntegerField(default=0,verbose_name='Возраст')
    Breed = models.CharField(max_length=50, verbose_name='Порода')
    Hairiness = models.CharField(max_length=50,verbose_name='Волосатость')
    Created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Создан')
    Changed = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Изменен')


    def __str__(self):
        return "Кот %s, Хозяин %s" %(self.Name,self.User.username)