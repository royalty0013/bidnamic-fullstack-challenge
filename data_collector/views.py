from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import DataCollectorForm
from .models import ClientData
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required(login_url='/')
def form_handler_view(request):
    context = {}
    if request.method == "POST":
        form = DataCollectorForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Form has been submitted successfully")
            return redirect("/data_collector/")
        else:
            messages.add_message(request, messages.ERROR, "Invalid form submission")
    else:
        form = DataCollectorForm(request.user)
        context["form"] = form
        return render(request, "data_collector/homepage.html", context)

@login_required(login_url='/')
def get_applications(request):
    context = {}
    client_data = ClientData.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(client_data, 5)
    try:
        applications = paginator.page(page)
    except PageNotAnInteger:
        applications = paginator.page(1)
    except EmptyPage:
        applications = paginator.page(paginator.num_pages)
    context["applications"] = applications
    return render(request, "data_collector/applications.html", context)

def delete_application(request, id):
    obj = get_object_or_404(ClientData, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse("data_collector:applications"))
