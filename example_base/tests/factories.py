# -*- encoding: utf-8 -*-
import factory

from example_base.models import FruitCake, LemonCake


class FruitCakeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = FruitCake

    quantity = 1


class LemonCakeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LemonCake

    quantity = 1
