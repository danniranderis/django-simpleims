from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import (check_scanned_uuid, LocationView, ContainerView,
                    ItemView, LocationListView, ContainerListView,
                    ItemListView, LocationUpdateView, ContainerUpdateView,
                    ItemUpdateView)

app_name = 'ims'

location_patterns = [
    path('', LocationListView.as_view(), name='list'),
    path('<pk>/', LocationView.as_view(), name='detail'),
    path('<pk>/update/', LocationUpdateView.as_view(), name='update'),
]

container_patterns = [
    path('', ContainerListView.as_view(), name='list'),
    path('<pk>/', ContainerView.as_view(), name='detail'),
    path('<pk>/update/', ContainerUpdateView.as_view(), name='update'),
]

item_patterns = [
    path('', ItemListView.as_view(), name='list'),
    path('<pk>/', ItemView.as_view(), name='detail'),
    path('<pk>/update/', ItemUpdateView.as_view(), name='update'),
]

urlpatterns = [
    # path('', ),
    path('uuid/<uuid:uuid>/', check_scanned_uuid, name='scanned_uuid'),
    path('uuid/<uuid:uuid>/create_selector/', login_required(
        TemplateView.as_view(template_name='create_selector.html')),
         name='create_selector'),
    path('locations/', include((location_patterns, 'ims'),
                               namespace='location')),
    path('containers/', include((container_patterns, 'ims'),
                                namespace='container')),
    path('items/', include((item_patterns, 'ims'), namespace='item')),
]
