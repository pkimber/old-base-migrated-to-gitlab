# -*- encoding: utf-8 -*-
import factory

from example_base.models import Cake


class CakeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Cake

    quantity = 1
