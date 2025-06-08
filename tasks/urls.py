from django.urls import path
from django.views.generic import TemplateView

app_name = "tasks"

urlpatterns = [
    path("", TemplateView.as_view(template_name="tasks/index.html"), name="index"),
    path("help/", TemplateView.as_view(template_name="tasks/help.html"), name="help"),
]
