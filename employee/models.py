from django.db import models
from django.utils import timezone


class Workplace(models.Model):
    name = models.CharField('勤務地', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField('名',max_length=20)
    last_name = models.CharField('姓',max_length=20)
    email = models.EmailField('メールアドレス',blank=True)
    workplace = models.ForeignKey(
        Workplace, verbose_name='勤務地', on_delete=models.PROTECT, blank=True, null=True,
    )
    created_at = models.DateTimeField('日付',default=timezone.now)
    

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)
    