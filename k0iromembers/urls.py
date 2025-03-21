from django.urls import path
from . import views
from k0iromembers.views import member_list
from k0iromembers.views import CustomLogoutView


urlpatterns = [
    path('add_member/', views.add_member, name='add_member'),
    path('member_list/', views.member_list, name='member_list'),
]
