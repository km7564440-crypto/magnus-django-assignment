from django.urls import path
from . import views

urlpatterns = [
    path("multiple-tabs/", views.multiple_tabs, name="multiple_tabs"),
    path("menu/", views.menu_demo, name="menu_demo"),
    path("autocomplete/", views.autocomplete, name="autocomplete"),
    path("collapsible/", views.collapsible, name="collapsible"),
    path("images/", views.images, name="images"),
    path("slider/", views.slider, name="slider"),
    path("tooltips/", views.tooltips, name="tooltips"),
    path("popups/", views.popups, name="popups"),
    path("links/", views.links, name="links"),
    path("css-properties/", views.css_properties, name="css_properties"),
    path("iframes/", views.iframes, name="iframes"),
]
