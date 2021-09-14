from django.test import TestCase
from django.db.utils import IntegrityError
from .models import (Identifier, Location, LocationType, Container,
                     ContainerType, Item, Tag)


class IdentifierTestCase(TestCase):
    def setUp(self):
        Identifier.objects.create(
            identifier='c152988d-c208-4442-b441-f1fdd4f1dcd9')

    def test_identifier_obj_string(self):
        """
        Test that a created identifier returns correct object-string.
        """
        c152988d = Identifier.objects.get(
            pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        self.assertEqual(c152988d.__str__(),
                         'c152988d-c208-4442-b441-f1fdd4f1dcd9')

    def test_entity_type_empty(self):
        """
        Test that a created identifier not linked to an entity, does not
        return an entity-type.
        """
        c152988d = Identifier.objects.get(
            pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        self.assertIsNone(c152988d.get_identifier_entity_type)

    def test_entity_type_location(self):
        """
        Test that a created identifier linked to a location, does
        return an entity-type of 'location'.
        """
        c152988d = Identifier.objects.get(
            pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        location_type = LocationType.objects.create(name='test-type')
        Location.objects.create(identifier=c152988d,
                                location_type=location_type,
                                name='test-location')
        i = Identifier.objects.get(pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        self.assertEqual(i.get_identifier_entity_type, 'location')

    def test_entity_pk_empty(self):
        """
        Test get_related_entity_pk with an identifier with no linked entity.
        """
        c152988d = Identifier.objects.get(
            pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        self.assertIsNone(c152988d.get_related_entity_pk)

    def test_entity_pk_location(self):
        """
        Test get_related_entity_pk with an identifier linked to a location.
        """
        c152988d = Identifier.objects.get(
            pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        location_type = LocationType.objects.create(name='test-type')
        Location.objects.create(identifier=c152988d,
                                location_type=location_type,
                                name='test-location')
        i = Identifier.objects.get(pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        self.assertEqual(i.get_related_entity_pk, 1)

    def test_identifier_absolute_url(self):
        """
        Test get_absolute_url for an identifier with a location linked.
        """
        c152988d = Identifier.objects.get(
            pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        location_type = LocationType.objects.create(name='test-type')
        Location.objects.create(identifier=c152988d,
                                location_type=location_type,
                                name='test-location')
        i = Identifier.objects.get(pk='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        self.assertEqual(i.get_absolute_url(), '/ims/location/1/')


class LocationTypeTestCase(TestCase):
    def test_location_type_obj_string(self):
        """
        Test that a created location-type returns correct object-string.
        """
        location_type = LocationType.objects.create(name='test-loc-type')
        self.assertEqual(location_type.__str__(), 'test-loc-type')


class ContainerTypeTestCase(TestCase):
    def test_container_type_obj_string(self):
        """
        Test that a created container-type returns correct object-string.
        """
        container_type = ContainerType.objects.create(name='test-con-type')
        self.assertEqual(container_type.__str__(), 'test-con-type')


class TagTestCase(TestCase):
    def test_tag_obj_string(self):
        """
        Test that a created tag returns correct object-string.
        """
        tag = Tag.objects.create(name='test-tag-type')
        self.assertEqual(tag.__str__(), 'test-tag-type')


class LocationTestCase(TestCase):
    def setUp(self):
        identifier = Identifier.objects.create(
            identifier='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        location_type = LocationType.objects.create(name='test-type')
        Location.objects.create(identifier=identifier,
                                location_type=location_type,
                                name='test-location')

    def test_location_obj_string(self):
        """
        Test that a created location returns correct object-string.
        """
        location = Location.objects.get(name='test-location')
        self.assertEqual(location.__str__(), 'test-location')


class ContainerTestCase(TestCase):
    def setUp(self):
        identifier = Identifier.objects.create(
            identifier='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        container_type = ContainerType.objects.create(name='test-type')
        Container.objects.create(identifier=identifier,
                                 container_type=container_type,
                                 name='test-container')

    def test_container_obj_string(self):
        """
        Test that a created container returns correct object-string.
        """
        container = Container.objects.get(name='test-container')
        self.assertEqual(container.__str__(), 'test-container')


class ItemTestCase(TestCase):
    def setUp(self):
        identifier = Identifier.objects.create(
            identifier='c152988d-c208-4442-b441-f1fdd4f1dcd9')
        location_type = LocationType.objects.create(name='test-type')
        container_type = ContainerType.objects.create(name='test-type')
        Item.objects.create(identifier=identifier, name='test-item')

    def test_item_obj_string(self):
        """
        Test that a created item returns correct object-string.
        """
        item = Item.objects.get(name='test-item')
        self.assertEqual(item.__str__(), 'test-item')

    def test_item_creation_no_identifier(self):
        """
        Test that creation of item with no identifier is impossible.
        """
        with self.assertRaises(IntegrityError):
            item = Item.objects.create(name='item creation with no identifier')
