from unicodedata import name
from django.urls import path
from .views import (
    form_handler_view,
    get_applications,
    delete_application,
    )

app_name = 'data_collector'

urlpatterns = [
    path("", form_handler_view, name="form_handler"),
    path("applications/", get_applications, name="applications"),
    path("delete/<int:id>/", delete_application, name="delete"),
]