from django.urls import path
from .views import home_page, summarize, file_upload, summary

urlpatterns = [
    path("", home_page, name="home"),
    path("file_upload/", file_upload, name="file_upload"),
    path("summary/<int:summary_id>/", summary, name="summary"),
    path("summarize/", summarize, name="summarize"),
]
