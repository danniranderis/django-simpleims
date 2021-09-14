from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    context_object_name = 'location'
    model = Location


class ContainerView(LoginRequiredMixin, DetailView):
    """
    Class-based built-in view for viewing Container-obj.
    """
    context_object_name = 'container'
    model = Container


class ItemView(LoginRequiredMixin, DetailView):
    """
    Class-based built-in view for viewing Item-obj.
    """
    context_object_name = 'item'
    model = Item
