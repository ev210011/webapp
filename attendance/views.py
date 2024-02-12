from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Attendance
from .forms import AttendanceForm
from datetime import datetime
from django.utils import timezone


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        form = AttendanceForm
        context = {
            'form': form,
            "user": request.user,
        }
        return render(request, 'attendance/index.html', context)
index = IndexView.as_view()


class ResultView(View):
    def post(self, request):
        form = AttendanceForm(request.POST)
        now = datetime.now()
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        obj = form.save(commit=False)
        obj.in_out = request.POST["in_out"]
        obj.staff = request.user
        obj.date = datetime.now().date()
        obj.time = datetime.now().time()
        #obj.save()
        if request.POST["in_out"] == '1':
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
        else:
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした(^-^)！"
        context = {
            'comment': comment,
        }
        obj.save()
        return render(request, 'attendance/result.html', context)
result = ResultView.as_view()
