from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Attendance
from .forms import EmployeeForm, AttendanceForm
from django.db.models import Count, Q

def dashboard(request):
    total_employees = Employee.objects.count()
    total_present_today = Attendance.objects.filter(date=django.utils.timezone.now().date(), status='Present').count()
    context = {
        'total_employees': total_employees,
        'total_present_today': total_present_today,
    }
    return render(request, 'core/dashboard.html', context)

def employee_list(request):
    employees = Employee.objects.all().order_by('-created_at')
    return render(request, 'core/employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_list')
        else:
            messages.error(request, 'Error adding employee. Please check the form.')
    else:
        form = EmployeeForm()
    return render(request, 'core/employee_form.html', {'form': form, 'title': 'Add Employee'})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully!')
        return redirect('employee_list')
    return render(request, 'core/employee_confirm_delete.html', {'employee': employee})

def attendance_mark(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance marked successfully!')
            return redirect('attendance_list')
        else:
            messages.error(request, 'Error marking attendance.')
    else:
        form = AttendanceForm()
    return render(request, 'core/attendance_form.html', {'form': form, 'title': 'Mark Attendance'})

def attendance_list(request):
    records = Attendance.objects.select_related('employee').all()
    
    # Simple Date Filter
    date_query = request.GET.get('date')
    if date_query:
        records = records.filter(date=date_query)
        
    return render(request, 'core/attendance_list.html', {'records': records})

import django.utils.timezone
