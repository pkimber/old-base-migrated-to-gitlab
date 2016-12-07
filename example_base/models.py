# -*- encoding: utf-8 -*-
import os.path

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


class Document(TimedCreateModifyDeleteModel):
    file = models.FileField(upload_to='document')
    description = models.CharField(max_length=256)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return '{}: {}'.format(self.file, self.description)

    def filename(self):
        if self.file and self.file.name:
            return os.path.basename(self.file.name)
        return ''

    def is_image(self):
        import imghdr
        from django.conf import settings
        try:
            if imghdr.what(os.path.join(settings.MEDIA_ROOT, self.file.name)):
                return True
        except:
            pass

        return False
