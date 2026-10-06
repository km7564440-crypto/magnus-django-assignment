from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "mobile_number", "country", "city", "created_at")
    search_fields = ("first_name", "last_name", "email", "mobile_number")
    list_filter = ("gender", "country", "other_city")
