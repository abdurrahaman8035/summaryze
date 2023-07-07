from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from utils.generate_summary import generate_summary
from .models import Summary
import textract


def home_page(request):
    """Display the Home Page"""
    return render(request, "index.html")


# Restrict access to logged-in users only
@login_required
def summarize(request):
    """Extract text, summarize and display summary"""
    if request.method == "POST":
        document = request.FILES.get("document", None)

        summary = Summary.objects.create(
            original_text="",
            summary_text="",
            user_id=request.user,
            document=document,
        )
        
        # Perform text extraction from the handout
        extracted_text = textract.process("./" + summary.document.url).decode("utf-8")

        # Generate summary using GPT-3 API
        # generated_summary = generate_summary(extracted_text)

        # Save extracted text and generated summary to Database
        summary.original_text = extracted_text
        # summary.summary_text = generated_summary
        summary.save()
        return redirect("summary", summary_id=summary.pk)
    else:
        return render(request, "file_upload.html")


# Restrict access to logged-in users only
@login_required
def summary(request, summary_id):
    """Display a single summary"""
    summary = Summary.objects.get(id=summary_id)
    context = {"summary": summary}
    return render(request, "summary.html", context)
