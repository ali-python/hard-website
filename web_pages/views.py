from django.views.generic import TemplateView, RedirectView, UpdateView, ListView
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth import forms as auth_forms
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import Http404
from django.db import transaction
from .forms import ProjectForm
from .models import Project, ProjectGallery


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(
            IndexView, self).get_context_data(**kwargs)


class IntroductionView(TemplateView):
    template_name = 'web_pages/intro.html'

    def get_context_data(self, **kwargs):
        context = super(
            IntroductionView, self).get_context_data(**kwargs)


class ProjectList(ListView):
    model = Project
    template_name = 'web_pages/projects.html'
    paginate_by = 50
    ordering = 'project_title'


class GalleryList(ListView):
    model = ProjectGallery
    template_name = 'web_pages/gallery.html'
    paginate_by = 100