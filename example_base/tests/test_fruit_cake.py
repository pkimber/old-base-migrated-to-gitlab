# -*- encoding: utf-8 -*-
import pytest

from django.utils import timezone

from login.tests.factories import UserFactory
from example_base.models import FruitCake
from .factories import FruitCakeFactory


@pytest.mark.django_db
def test_factory():
    FruitCakeFactory()


@pytest.mark.django_db
def test_str():
    str(FruitCakeFactory())


@pytest.mark.django_db
def test_set_deleted():
    obj = FruitCakeFactory()
    assert 0 == obj.deleted_version
    user = UserFactory()
    max_deleted_version = FruitCake.objects.max_deleted_version(
        'number',
        obj.number,
    )
    obj.set_deleted(user, max_deleted_version)
    obj.refresh_from_db()
    assert obj.deleted is True
    assert obj.user_deleted == user
    assert obj.date_deleted is not None
    assert 1 == obj.deleted_version


@pytest.mark.django_db
def test_undelete():
    obj = FruitCakeFactory()
    user = UserFactory()
    max_deleted_version = FruitCake.objects.max_deleted_version(
        'number',
        obj.number,
    )
    obj.set_deleted(user, max_deleted_version)
    assert obj.deleted_version > 0
    obj.refresh_from_db()
    obj.undelete()
    obj.refresh_from_db()
    assert obj.deleted is False
    assert obj.user_deleted is None
    assert obj.date_deleted is None
    assert 0 == obj.deleted_version
