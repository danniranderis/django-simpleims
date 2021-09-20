from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
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
        return HttpResponseRedirect(reverse('ims:create_selector',
                                            args={uuid}))


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
        context['update_btn_url'] = reverse('ims:location:update',
                                            args={context['object'].pk})
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
        context['update_btn_url'] = reverse('ims:container:update',
                                            args={context['object'].pk})
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
        context['update_btn_url'] = reverse('ims:item:update',
                                            args={context['object'].pk})
        return context


class LocationListView(LoginRequiredMixin, ListView):
    """
    Class-based view for listing locations on the webpage.
    """
    template_name = 'location_list.html'
    model = Location


class ContainerListView(LoginRequiredMixin, ListView):
    """
    Class-based view for listing containers on the webpage.
    """
    template_name = 'container_list.html'
    model = Container


class ItemListView(LoginRequiredMixin, ListView):
    """
    Class-based view for listing items on the webpage.
    """
    template_name = 'item_list.html'
    model = Item


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class-based view for editing locations on the webpage.
    """
    model = Location
    fields = '__all__'
    template_name = 'location_update_form.html'


class ContainerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class-based view for editing containers on the webpage.
    """
    model = Container
    fields = '__all__'
    template_name = 'container_update_form.html'


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class-based view for editing items on the webpage.
    """
    model = Item
    fields = '__all__'
    template_name = 'item_update_form.html'
