# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView

from django.views.generic import View

from braces.views import (
    AjaxResponseMixin,
    JSONResponseMixin,
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .forms import DocumentForm
from .models import Document


class HomeView(BaseMixin, TemplateView):

    template_name = 'example/home.html'


class DashView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView):

    template_name = 'dash/dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(document_list=Document.objects.order_by('file'))
        return context


class SettingsView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView):
    """Has to be there to log in nothing to do so duplicate home"""
    template_name = 'dash/settings.html'


class FileDropDemoView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = DocumentForm
    model = Document
    template_name = 'dash/filedrop_demo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(document_list=Document.objects.order_by('file'))
        return context

    def get_success_url(self):
        return reverse('filedrop.demo')


class AjaxFileUploadView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        JSONResponseMixin, AjaxResponseMixin, View):
    """
    View for uploading files via AJAX.
    """
    def post_ajax(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        document = Document.objects.create(file=uploaded_file)

        response_dict = {
            'message': 'File uploaded successfully!',
            'file_path': document.file.name,
            'document_id': document.id
        }

        return self.render_json_response(response_dict, status=200)
