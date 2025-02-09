from django.shortcuts import render  # get_object_or_404
# from django.views import generic
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def AboutDetail(request):
    if request.method == "POST":
        print("POST request received")
        collaborate_form = CollaborateForm(data=request.POST)

        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
