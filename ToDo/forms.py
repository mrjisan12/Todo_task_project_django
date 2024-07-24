from django import forms 
from ToDo.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['id', 'taskTitle', 'taskDescription', 'is_completed']