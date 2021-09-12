from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _


class TypeAbstract(models.Model):
    """
    Abstract model for creating standard models with name/slug.
    """
    name = models.CharField(
        _('name'),
        max_length=50,
        unique=True,
        db_index=True,
    )
    slug = AutoSlugField(
        populate_from='name',
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class LocationType(TypeAbstract):
    """
    Model for the different types of locations.
    """
    pass


class ContainerType(TypeAbstract):
    """
    Model for the different types of containers.
    """
    pass


class Tag(TypeAbstract):
    """
    Model for item-tags.
    """
    pass


class Identifier(models.Model):
    """
    Model for all physical identifiers linked to this IMS.
    """
    identifier = models.UUIDField(
        _('identifier'),
        primary_key=True,
        editable=False,  # When created, impossible to edit
    )

    def __str__(self):
        return str(self.identifier)


class Location(models.Model):
    """
    Model for all defined locations where items etc. can be stored.
    """
    identifier = models.OneToOneField(
        'ims.Identifier',
        on_delete=models.CASCADE,  # Delete location if identifier is deleted
        related_name='location',
        verbose_name=_('identifier'),
        editable=False,
    )
    name = models.CharField(
        _('location name'),
        max_length=100,
    )
    description = models.TextField(
        _('description'),
        blank=True,
    )
    location_type = models.ForeignKey(
        'ims.LocationType',
        on_delete=models.PROTECT,  # Disallow del for loc-types if in use
        related_name='locations',
        verbose_name=_('location type'),
    )
    # https://xkcd.com/2170/
    longitude = models.DecimalField(
        _('longitude'),
        max_digits=9,
        decimal_places=6,
        blank=True,
        help_text=_('Optionally. Longitude as decimal up-to 6 decimals.'),
    )
    latitude = models.DecimalField(
        _('latitude'),
        max_digits=9,
        decimal_places=6,
        blank=True,
        help_text=_('Optionally. Latitude as decimal up-to 6 decimals.'),
    )
    parent_location = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,  # Disallow del if location has child's
        related_name='sub_locations',
        blank=True,
        verbose_name=_('parent location'),
        help_text=_('locations can be marked as sub-locations '
                    'by providing a parent locations here.'),
    )

    def __str__(self):
        return self.name


class Container(models.Model):
    """
    Model for all containers that can have items and be placed in a location.
    """
    identifier = models.OneToOneField(
        'ims.Identifier',
        on_delete=models.CASCADE,  # Delete container if identifier is deleted
        related_name='container',
        verbose_name=_('identifier'),
        editable=False,
    )
    name = models.CharField(
        _('container name'),
        max_length=100,
    )
    description = models.TextField(
        _('description'),
        blank=True,
    )
    container_type = models.ForeignKey(
        'ims.ContainerType',
        on_delete=models.PROTECT,  # Disallow del for container-types if in use
        related_name='containers',
        verbose_name=_('container type'),
    )

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Model for all items tracked in the IMS.
    """
    identifier = models.OneToOneField(
        'ims.Identifier',
        on_delete=models.CASCADE,  # Delete item if identifier is deleted
        related_name='item',
        verbose_name=_('identifier'),
        editable=False,
    )
    name = models.CharField(
        _('item name'),
        max_length=100,
    )
    description = models.TextField(
        _('description'),
        blank=True,
    )
    container = models.ForeignKey(
        'ims.Container',
        on_delete=models.PROTECT,  # Disallow del container if items is linked
        related_name='items',
        blank=True,
        verbose_name=_('container'),
    )
    location = models.ForeignKey(
        'ims.Location',
        on_delete=models.PROTECT,  # Disallow del location if items is linked
        related_name='items',
        blank=True,
        verbose_name=_('location'),
        help_text=_('if item is linked to a container with a location, '
                    'there is no need to explicitly assign the item a '
                    'location as it is inherited.'),
    )
    tags = models.ManyToManyField(
        'ims.Tag',
        related_name='items',
        blank=True,
        verbose_name=_('tags'),
        help_text=_('optionally add tags for easy sorting/searching etc.'),
    )

    def __str__(self):
        return self.name
