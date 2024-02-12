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

        name = form.cleaned_data['name']
        if name:
            queryset = Employee.objects.annotate(name=Concat('last_name', 'first_name')).filter(
                Q(last_name__icontains=name) &
                Q(first_name__icontains=name)
            ).order_by('pk').distinct()
        else:
            name = Employee.objects.all().order_by('pk')
        return queryset
    