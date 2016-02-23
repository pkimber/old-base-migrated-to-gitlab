# -*- encoding: utf-8 -*-
import pytest

from .factories import CakeFactory


@pytest.mark.django_db
def test_factory():
    CakeFactory()


@pytest.mark.django_db
def test_str():
    str(CakeFactory())
