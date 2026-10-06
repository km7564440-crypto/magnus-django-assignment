from django import forms
from .models import Employee

SKILLS = [
    ("AWS", "AWS"),
    ("DevOps", "DevOps"),
    ("Full Stack Developer", "Full Stack Developer"),
    ("Middleware", "Middleware"),
    ("QA-Automation", "QA-Automation"),
    ("WebServices", "WebServices"),
]

class EmployeeForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(
        choices=SKILLS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Employee
        fields = [
            "first_name", "last_name", "email", "mobile_number",
            "date_of_birth", "gender", "address", "country",
            "city", "other_city", "skills", "photo"
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.skills:
            self.initial["skills"] = [s.strip() for s in self.instance.skills.split(",")]

    def clean_mobile_number(self):
        value = self.cleaned_data["mobile_number"].strip()
        digits = "".join(ch for ch in value if ch.isdigit())
        if len(digits) < 10 or len(digits) > 15:
            raise forms.ValidationError("Enter a valid mobile number.")
        return digits

    def save(self, commit=True):
        obj = super().save(commit=False)
        selected = self.cleaned_data.get("skills", [])
        obj.skills = ", ".join(selected)
        if commit:
            obj.save()
        return obj
