from django import forms
from .models import Employee, Number, Workplace
from django.db.models.functions import Concat


class SearchForm(forms.Form):
    full_name = forms.ModelChoiceField(
        queryset = Employee.objects, label='氏名', required=False)
       
    id = forms.ModelChoiceField(
        queryset = Employee.objects, label='従業員番号', required=False)

    workplace = forms.ModelChoiceField(
        queryset = Workplace.objects, label='勤務地', required=False)
