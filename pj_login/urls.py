from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

in_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_required(in_view), name="in"),
    path('', include("django.contrib.auth.urls")),
    path('', include('employee.urls')),
    path('attendance/', include('attendance.urls')),
]
