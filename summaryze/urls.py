from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home_page, summarize, summary

urlpatterns = [
    path("", home_page, name="home"),
    path("summary/<int:summary_id>/", summary, name="summary"),
    path("summarize/", summarize, name="summarize"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
