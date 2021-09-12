from django.contrib import admin
from .models import (LocationType, ContainerType, Tag, Location,
                     Container, Item, Identifier)


@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ContainerType)
class ContainerTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Identifier)
class IdentifierAdmin(admin.ModelAdmin):
    pass
