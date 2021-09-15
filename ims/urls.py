from django.urls import include, path
from .views import (check_scanned_uuid, LocationView, ContainerView, ItemView)

app_name = 'ims'

location_patterns = [
    path('<pk>/', LocationView.as_view(), name='detail'),
]

container_patterns = [
    path('<pk>/', ContainerView.as_view(), name='detail'),
]

item_patterns = [
    path('<pk>/', ItemView.as_view(), name='detail'),
]

urlpatterns = [
    # path('', ),
    path('uuid/<uuid:uuid>', check_scanned_uuid, name='scanned_uuid'),
    path('location/', include((location_patterns, 'ims'),
                              namespace='location')),
    path('container/', include((container_patterns, 'ims'),
                               namespace='container')),
    path('item/', include((item_patterns, 'ims'), namespace='item')),
]
