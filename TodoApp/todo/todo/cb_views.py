from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from todo.models import Todo
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



class TodoListView(ListView):
    queryset = Todo.objects.all().order_by('-created')
    template_name = 'todo_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(detail__icontains=q)
            )
        return queryset

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_create.html'
    fields = ('category', 'title', 'detail')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('todo:detail', kwargs={'pk': self.object.pk})

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_update.html'
    fields = ('category', 'title', 'detail')

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('todo:detail', kwargs={'pk': self.object.pk})


class TodoDeleteView(DeleteView):
    model = Todo

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('todo:list')