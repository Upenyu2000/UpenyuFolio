from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request,HttpResponseRedirect
from django.urls import reverse

from .models import Folio,About,Project,Stack


# Create your views here.
def index(request):
    folios = Folio.objects.all()
    abouts = About.objects.all()
    projects = Project.objects.all()
    stacks = Stack.objects.all()

    context = {
        'folio': folios,
        'about': abouts,
        'project': projects,
        'stack': stacks,
    }

    return render(request, "home.html", context)
