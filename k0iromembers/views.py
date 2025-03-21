# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from .models import Member
from .forms import MemberForm

def admin_dashboard(request):
    members = Member.objects.all()
    return render(request, 'admin_dashboard.html', {'members': members})

@login_required
def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

@login_required
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)