
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create_account", views.createAccount, name="create_account"),
    path("create_post", views.create_post, name="create_post"),
    path("record_reminder", views.record_reminder, name="record_reminder"),
    path("change_status", views.change_status, name="change_status"),
    path("delete_reminder", views.delete_reminder, name="delete_reminder"),


]