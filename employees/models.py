from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")
    address = models.TextField(blank=True)
    country = models.CharField(max_length=80, default="India")
    city = models.CharField(max_length=80, blank=True)
    other_city = models.BooleanField(default=False)

    # Stored as comma-separated values for a simple interview assignment.
    skills = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(upload_to="employees/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def skill_list(self):
        return [s.strip() for s in self.skills.split(",") if s.strip()]
