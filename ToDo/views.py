from django.shortcuts import render
from ToDo.models import TaskModel
from .forms import TaskForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views import View

# Create your views here.

class MyHomeView(TemplateView):
    template_name = 'home.html'
    
class TaskFormView(CreateView):
    model = TaskModel
    template_name = 'add_task.html'
    form_class = TaskForm 
    success_url = reverse_lazy('ShowTask')
    
class ShowTaskView(ListView):
    model = TaskModel
    template_name = 'show_task.html'
    context_object_name = 'data'
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=False)
    
class TaskEditView(UpdateView):
    model = TaskModel
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('ShowTask')
    pk_url_kwarg = 'pk'

    
class CompleteTaskView(ListView):
    model = TaskModel
    template_name = 'completed_task.html'
    context_object_name = 'data'
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=True)
    
class MarkTaskCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(TaskModel, pk=pk)
        task.is_completed = True
        task.save()
        return redirect('CompletedTask')
    
class DeleteTask(DeleteView):
    model = TaskModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('ShowTask')
    
class DeleteCompletedTask(DeleteView):
    model = TaskModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('CompletedTask')