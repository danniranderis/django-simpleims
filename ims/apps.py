from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ImsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ims'
    verbose_name = _('ims')
