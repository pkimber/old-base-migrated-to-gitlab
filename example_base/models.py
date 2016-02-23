# -*- encoding: utf-8 -*-
from django.db import models

from base.model_utils import TimedCreateModifyDeleteModel


class Cake(TimedCreateModifyDeleteModel):

    description = models.CharField(max_length=100)
    quantity = models.IntegerField()

    class Meta:
        ordering = ('description',)
        verbose_name = 'Cake'
        verbose_name_plural = 'Cakes'

    def __str__(self):
        return '{}'.format(self.description)
