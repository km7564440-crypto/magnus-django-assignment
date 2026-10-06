from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeeForm
from .models import Employee

@login_required
def dashboard(request):
    total = Employee.objects.count()
    return render(request, "dashboard.html", {"total": total})

@login_required
def employee_list(request):
    query = request.GET.get("q", "").strip()
    qs = Employee.objects.all()

    if query:
        qs = qs.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(mobile_number__icontains=query)
        )

    paginator = Paginator(qs, 8)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "employees/list.html", {
        "page_obj": page_obj,
        "query": query,
    })

@login_required
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()
            messages.success(request, "Employee created successfully.")
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "employees/form.html", {
        "form": form,
        "title": "Create Employee",
        "button": "Save",
    })

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, "employees/detail.html", {"employee": employee})

@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "employees/form.html", {
        "form": form,
        "title": "Edit Employee",
        "button": "Update",
    })

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee deleted successfully.")
        return redirect("employee_list")
    return render(request, "employees/delete.html", {"employee": employee})
