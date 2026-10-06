from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def multiple_tabs(request):
    return render(request, "more/multiple_tabs.html")

@login_required
def menu_demo(request):
    return render(request, "more/menu.html")

@login_required
def autocomplete(request):
    tags = ["Java", "Python", "Django", "React", "AWS", "DevOps", "SQL", "Testing"]
    return render(request, "more/autocomplete.html", {"tags": tags})

@login_required
def collapsible(request):
    return render(request, "more/collapsible.html")

@login_required
def images(request):
    return render(request, "more/images.html")

@login_required
def slider(request):
    return render(request, "more/slider.html")

@login_required
def tooltips(request):
    return render(request, "more/tooltips.html")

@login_required
def popups(request):
    return render(request, "more/popups.html")

@login_required
def links(request):
    return render(request, "more/links.html")

@login_required
def css_properties(request):
    return render(request, "more/css_properties.html")

@login_required
def iframes(request):
    return render(request, "more/iframes.html")
