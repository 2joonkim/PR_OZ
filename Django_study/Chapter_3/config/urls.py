# config/urls.py

from django.contrib import admin
from django.urls import path, include
from todo.views import todo_list, todo_info
from users import views as users_views

urlpatterns = [
    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', users_views.login, name='login'),
    path('accounts/signup/', users_views.sign_up, name='signup')
]

