from django import forms
from .models import Member
import datetime

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'call_sign', 'membership_expires', 'is_active', 'dues_paid']
        widgets = {
            'membership_expires': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Default membership_expires to the end of the current calendar year
        current_year = datetime.date.today().year
        self.fields['membership_expires'].initial = datetime.date(current_year, 12, 31)

