from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('add/', views.add_member, name='add_member'),  # Route to add members
    path('list/', views.member_list, name='member_list'),  # Route for members list
    path('delete/', views.delete_users, name='delete_users'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
