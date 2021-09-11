from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Extended User-model.
    """
    # No customizations yet
    # https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    pass

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
