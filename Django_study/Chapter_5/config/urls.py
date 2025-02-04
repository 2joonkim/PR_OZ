from django.contrib import admin
from django.urls import path, include
from todo.views import todo_list, todo_info, todo_create, todo_update, todo_delete
from users import views as user_views

urlpatterns = [
    path('todo/', todo_list, name='todo_list'),
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('todo/<int:todo_id>/update/', todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', todo_delete, name='todo_delete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', user_views.login, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
    # CBV URL include
    path('cbv/', include('todo.urls')),
]
