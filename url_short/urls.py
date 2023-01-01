from django.urls import path
from . import views

urlpatterns = [
    path(r"", views.index, name="index"),
    path(r"url_result", views.url_result, name="url_result"),
    path(r"<str:short_url>", views.redirect_view, name="redirect_view"),
]
