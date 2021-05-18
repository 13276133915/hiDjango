

from django.urls import path
from mainapp.views import user_list1, add_user, del_user, update_user

urlpatterns = [
    path('users', user_list1),
    path('1', user_list1),
    path('add', add_user),
    path('del', del_user),
    path('update',update_user)
]
