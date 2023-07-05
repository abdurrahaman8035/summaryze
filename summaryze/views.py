from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")


def add_summary(request):
    return render(request, "create_summary.html")


def summary(request):
    return render(request, "summary.html")
