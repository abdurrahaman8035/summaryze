from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Summary
from django.shortcuts import redirect
import textract


def home_page(request):
    """Display the Home Page"""
    return render(request, "index.html")


# Restrict access to logged-in users only
@login_required
def file_upload(request):
    """Display form for file uploads"""
    return render(request, "file_upload.html")


# Restrict access to logged-in users only
@login_required
def summarize(request):
    """Extract text, summarize and display summary"""
    if request.method == "POST":
        document = request.FILES["document"]
        num_of_paragraphs = request.POST.get("num_of_paragraphs", None)

        original_text = textract.process(document)
        summary_text = ""

        summary = Summary.objects.create(
            original_text=original_text, summary_text=summary_text, user_id=request.user
        )
        return redirect("summary", summary_id=summary.pk)
    else:
        return redirect("file_upload")


# Restrict access to logged-in users only
@login_required
def summary(request, summary_id):
    """Display a single summary"""
    summary = Summary.objects.get(id=summary_id)
    context = {"summary": summary}
    return render(request, "summary.html", context)
