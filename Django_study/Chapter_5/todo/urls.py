from django.urls import path
from todo.cb_views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView


urlpatterns = [
    path('todo/', TodoListView.as_view(), name='cbv_todo_list',),
    path('todo/create/', TodoCreateView.as_view(), name='cbv_todo_create'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='cbv_todo_info'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='cbv_todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='cbv_todo_delete'),
]