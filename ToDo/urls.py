from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyHomeView.as_view(), name='HomePage'),
    path('add_task/', views.TaskFormView.as_view(), name='AddTask'),
    path('show_tasks/', views.ShowTaskView.as_view(), name='ShowTask'),
    path('edit_tasks/<int:pk>', views.TaskEditView.as_view(), name='EditTask'),
    path('delete_tasks/<int:pk>', views.DeleteTask.as_view(), name='DeleteTask'),
    path('delete_completed_tasks/<int:pk>', views.DeleteCompletedTask.as_view(), name='DeleteCompletedTask'),
    path('completed_task/', views.CompleteTaskView.as_view(), name='CompletedTask'),
    path('completed_task/<int:pk>', views.MarkTaskCompleteView.as_view(), name='CompleteTask'),
]
