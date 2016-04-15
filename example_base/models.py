# -*- encoding: utf-8 -*-
from django.db import models

from base.model_utils import (
    TimedCreateModifyDeleteModel,
    TimedCreateModifyDeleteVersionModel,
    TimedCreateModifyDeleteVersionModelManager,
)


class FruitCake(TimedCreateModifyDeleteVersionModel):

    UNIQUE_FIELD_NAME = 'number'

    description = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    quantity = models.IntegerField()
    objects = TimedCreateModifyDeleteVersionModelManager()

    class Meta:
        ordering = ('description',)
        unique_together = ('number', 'deleted_version')
        verbose_name = 'Fruit Cake'
        verbose_name_plural = 'Fruit Cakes'

    def __str__(self):
        return '{}'.format(self.description)


class LemonCake(TimedCreateModifyDeleteModel):

    description = models.CharField(max_length=100)
    quantity = models.IntegerField()

    class Meta:
        ordering = ('description',)
        verbose_name = 'Lemon Cake'
        verbose_name_plural = 'Lemon Cakes'

    def __str__(self):
        return '{}'.format(self.description)
