from django.urls import path
from .views import homepage, add_summary, summary

urlpatterns = [
    path("", homepage, name="home"),
    path("new-summary/", add_summary, name="new-summary"),
    path("summary/", summary, name="summary"),
]