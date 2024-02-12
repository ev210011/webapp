from django.db import models
from django.contrib.auth import get_user_model

class Attendance(models.Model):
    class Meta:
        db_table = 'attendance'

    IN_OUT = (
        (1, '出勤（IN）'),
        (0, '退勤（OUT）'),
    )
    staff = models.ForeignKey(get_user_model(), verbose_name='従業員', on_delete=models.CASCADE, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name='打刻時間')
    date = models.DateField(verbose_name='打刻日')

    def __str__(self):
        return '{0} {1}'.format(self.staff, self.in_out)
