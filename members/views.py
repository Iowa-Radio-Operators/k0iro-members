from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # Update this with your actual members listing view
    else:
        form = MemberForm()
    return render(request, 'members/add_member.html', {'form': form})

@login_required
def member_list(request):
    members = Member.objects.all().order_by('last_name')
    return render(request, 'members/member_list.html', {'members': members})

@login_required
def delete_users(request):
    if request.method == 'POST':
        # Collect the user IDs from the submitted form
        user_ids = request.POST.getlist('users_to_delete')
        if 'confirm' in request.POST:  # Confirm deletion
            Member.objects.filter(id__in=user_ids).delete()
            return redirect('member_list')  # Redirect after deletion
        elif 'cancel' in request.POST:  # Cancel deletion
            return redirect('member_list')  # Redirect back to the list

    # Display all users with checkboxes for selection
    members = Member.objects.all().order_by('last_name')
    return render(request, 'members/delete_users.html', {'members': members})