from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .models import Word
from .filters import WordFilter
from .forms import WordForm

class WordFilterView(FilterView):
    model = Word
    filterset_class = WordFilter
    queryset = Word.objects.all().order_by('-created_at')

    strict = False

    paginate_by = 25

    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]
        return super().get(request, **kwargs)

class WordDetailView(DetailView):
    model = Word

class WordCreateView(CreateView):
    model = Word
    form_class = WordFrom
    success_url = reverse_lazy('index')

class WordUpdateView(UpdateView):
    model = Word
    form_class = WordForm
    success_url = reverse_lazy('index')

class WordDeleteView(DeleteView):
    model = Word
    success_url = reverse_lazy('index')
