from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, "index.html")


@login_required
def add_summary(request):
    return render(request, "create_summary.html")


@login_required
def summary(request):
    return render(request, "summary.html")
