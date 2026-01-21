from django import forms
from .models import Employee, Attendance
from django.core.exceptions import ValidationError

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'full_name', 'email', 'department']
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. EMP001'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_employee_id(self):
        eid = self.cleaned_data.get('employee_id')
        if Employee.objects.filter(employee_id=eid).exists() and self.instance.pk is None:
             raise ValidationError("Employee ID already exists.")
        return eid

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get("employee")
        date = cleaned_data.get("date")

        if employee and date:
            if Attendance.objects.filter(employee=employee, date=date).exclude(pk=self.instance.pk).exists():
                raise ValidationError("Attendance for this employee on this date already exists.")
        return cleaned_data
