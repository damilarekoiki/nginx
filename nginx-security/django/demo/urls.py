from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TemplateView.as_view(template_name="index.html")),
    path('split-test/', TemplateView.as_view(template_name="index.html")),
]
