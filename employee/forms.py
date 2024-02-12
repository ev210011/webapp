from django import forms
from .models import Employee, Workplace


class SearchForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset = Employee.objects, label = '氏名', required = False)
    
    id = forms.ModelChoiceField(
        queryset = Employee.objects, to_field_name='id', label = '従業員番号', required = False)

    workplace = forms.ModelChoiceField(
        queryset=Workplace.objects, label='勤務地', required=False)
    