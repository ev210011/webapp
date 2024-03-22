from django.views import generic
from django.db.models.functions import Concat
from django.db.models import Q
from .forms import SearchForm
from .models import Employee


class IndexView(generic.ListView):
    model = Employee
    panaginate_by = 10

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)
        return context
    
    def get_queryset(self):
        form = SearchForm(self.request.GET)
        form.is_valid()

        queryset = super().get_queryset()

        workplace = form.cleaned_data['workplace']
        if workplace:
            queryset = queryset.filter(workplace=workplace)

        id = form.cleaned_data['id']
        if id:
            queryset = queryset.filter(id=id)
       
        full_name = form.cleaned_data['full_name']
        if full_name:
            queryset = queryset.filter(full_name=full_name)
        return queryset
        

'''
        name = form.cleaned_data['name']
        if name:
            queryset = Employee.objects.annotate(full_name=Concat('last_name', 'first_name')).filter(
                Q(last_name__icontains=name) &
                Q(first_name__icontains=name) &
                Q(full_name__icontains=name)
            ).order_by('pk').distinct()
        else:
            queryset = Employee.objects.all().order_by('pk')
        
        return queryset



class EmployeeListView(generic.ListView):
    model = Employee

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)
        return context
    
    def get_queryset(self):
        form = SearchForm(self.request.GET)
        form.is_valid()

        name = self.request.GET.get('queryset')

        if name:
            name = name.replace(' ', '')
            name = name.replace(' ', '')
            queryset = Employee.objects.annotate(full_name=Concat('last_name', 'first_name')).filter(
                Q(last_name__icontains=name) &
                Q(first_name__icontains=name) &
                Q(full_name__icontains=name)
            ).order_by('pk').distinct()
        else:
            queryset = Employee.objects.all().order_by('pk')
        return queryset



class EmployeeListView(generic.ListView):
    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)
        return context
    
    def get_queryset(self):
        form = SearchForm(self.request.GET)
        form.is_valid()

        name = self.request.GET.get('queryset')

        if name:
            queryset = queryset.filter(name=name)
        return queryset.annotate(
            name = Concat('last_name', 'first_name')).filter(
                Q(last_name__icontains=name) &
                Q(first_name__icontains=name) &
                Q(full_name__icontains=name)
            ).order_by('pk').distinct()
'''
