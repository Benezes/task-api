from django.urls import path
from todo_api.views import TaskView

urlpatterns = [
    path('', TaskView.as_view()),
    path('<int:id>', TaskView.as_view()),
]
