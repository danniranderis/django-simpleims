from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from .models import Identifier, Location, Container, Item


def check_scanned_uuid(request, uuid):
    """
    View that checks a scanned uuid for existing identifiers.
    If exists, then redirect to the object, else provide create-btn's.

    :param request: Http-response request
    :param uuid: Provided uuid from the get-params.
    """
    # Check if UUID already exists
    try:
        identifier = Identifier.objects.get(pk=uuid)
        return HttpResponseRedirect(identifier.get_absolute_url())
    except Identifier.DoesNotExist:
        # TODO: redirect to a create-view or snow creat btns.
        pass


class LocationView(LoginRequiredMixin, DetailView):
    """
    Class-based built-in view for viewing Location-obj.
    """
    template_name = 'detail_view.html'
    context_object_name = 'object'
    model = Location

    def get_context_data(self, **kwargs):
        """ Extend context-data """
        context = super().get_context_data(**kwargs)
        context['detail_type'] = 'location'
        context['detail_name'] = _('location')
        return context


class ContainerView(LoginRequiredMixin, DetailView):
    """
    Class-based built-in view for viewing Container-obj.
    """
    template_name = 'detail_view.html'
    context_object_name = 'object'
    model = Container

    def get_context_data(self, **kwargs):
        """ Extend context-data """
        context = super().get_context_data(**kwargs)
        context['detail_type'] = 'container'
        context['detail_name'] = _('container')
        return context


class ItemView(LoginRequiredMixin, DetailView):
    """
    Class-based built-in view for viewing Item-obj.
    """
    template_name = 'detail_view.html'
    context_object_name = 'object'
    model = Item

    def get_context_data(self, **kwargs):
        """ Extend context-data """
        context = super().get_context_data(**kwargs)
        context['detail_type'] = 'item'
        context['detail_name'] = _('item')
        return context
