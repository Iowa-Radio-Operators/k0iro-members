from django.contrib import admin
from django.urls import path, include
from members.views import *
from django.contrib.auth.views import LoginView, LogoutView
from members.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member_list, name='home'),
    path('members/', include('members.urls')),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
]
