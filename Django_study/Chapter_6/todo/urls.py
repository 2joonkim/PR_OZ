from django.urls import path
from todo.cb_views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView, \
    CommentDeleteView, CommentUpdateView, CommentCreateView

urlpatterns = [
    path('todo/', TodoListView.as_view(), name='cbv_todo_list',),
    path('todo/create/', TodoCreateView.as_view(), name='cbv_todo_create'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='cbv_todo_info'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='cbv_todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='cbv_todo_delete'),
    path('comment/<int:todo_id>/create/',  CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete/',  CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update')
]