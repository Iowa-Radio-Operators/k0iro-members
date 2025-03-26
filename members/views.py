from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
import pandas as pd

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
    # Get the sort field from the query parameters (default to 'last_name')
    sort_by = request.GET.get('sort', 'last_name')
    # Retrieve members sorted by the specified field
    members = Member.objects.all().order_by(sort_by)
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

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login page after logging out
    return render(request, 'members/logout.html')  # Show the custom logout page

@login_required
def export_members_to_excel(request):
    # Retrieve all members
    members = Member.objects.all().values(
        'first_name', 'last_name', 'email', 'phone_number', 
        'call_sign', 'membership_expires', 'is_active', 'dues_paid'
    )
    # Convert queryset to a DataFrame
    df = pd.DataFrame(members)
    # Create a response object with Excel content
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=members.xlsx'
    # Write DataFrame to Excel
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Members')
    return response