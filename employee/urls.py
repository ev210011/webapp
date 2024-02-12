from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path('employee',views.IndexView.as_view(), name='index'),
]