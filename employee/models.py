from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.functions import Concat
from django.db.models import Q


class Workplace(models.Model):
    name = models.CharField('勤務地', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name
        

'''
class Number(models.Model):
    number = models.PositiveIntegerField('従業員番号', default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    
    def __str__(self):
        return str(self.number)
'''


class Employee(models.Model):
    last_name = models.CharField('姓',max_length=20)
    first_name = models.CharField('名',max_length=20)
    full_name = Concat('last_name', 'first_name')
    email = models.EmailField('メールアドレス',blank=True)
    '''
    number = models.OneToOneField(
        Number, verbose_name='従業員番号', on_delete=models.PROTECT, blank=True, null=True,
    )
    '''
    account = models.CharField('アカウント名', max_length=20, blank=True, null=True)
    workplace = models.ForeignKey(
        Workplace, verbose_name='勤務地', on_delete=models.PROTECT, blank=True, null=True,
    )
    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)
    
