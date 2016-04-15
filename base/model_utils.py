# -*- encoding: utf-8 -*-
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import AutoField, Max
from django.utils import timezone


# We want attachments to be stored in a private location and NOT available to
# the world at a public URL.  The idea for this came from:
# http://nemesisdesign.net/blog/coding/django-private-file-upload-and-serving/
# and
# https://github.com/johnsensible/django-sendfile
private_file_store = FileSystemStorage(
    location=settings.SENDFILE_ROOT
)


ftp_file_store = FileSystemStorage(
    location=settings.FTP_STATIC_DIR,
    base_url=settings.FTP_STATIC_URL,
)


class BaseError(Exception):

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr('%s, %s' % (self.__class__.__name__, self.value))


def _get_model_instance_data(obj):
    """
    Helper function for 'copy_model_instance'.
    """
    return dict(
        [(f.name, getattr(obj, f.name))
            for f in obj._meta.fields
                if not isinstance(f, AutoField) and \
                    not f in obj._meta.parents.values()
        ]
    )


def copy_model_instance(obj):
    """
    Copy field values from a model to a new instance.

    Code copied from:
    - http://djangosnippets.org/snippets/1040/
    - http://code.djangoproject.com/ticket/4027
    """
    initial = _get_model_instance_data(obj)
    return obj.__class__(**initial)


def copy_model_instance_to(from_obj, to_class):
    """
    Copy the data for a model instance to a new class which has the same
    fields.

    My variation on the `copy_model_instance` function (above)...
    """
    initial = _get_model_instance_data(from_obj)
    return to_class(**initial)


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimedCreateModifyDeleteModel(TimeStampedModel):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields
    """
    deleted = models.BooleanField(default=False)
    date_deleted = models.DateTimeField(blank=True, null=True)
    user_deleted = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='+',
    )

    def undelete(self):
        if not self.is_deleted:
            raise BaseError(
                "Object '{}' is not deleted".format(self.pk)
            )
        self.deleted = False
        self.date_deleted = None
        self.user_deleted = None
        self.save()

    @property
    def is_deleted(self):
        return self.deleted

    def set_deleted(self, user):
        if self.is_deleted:
            raise BaseError(
                "Object '{}' is already deleted".format(self.pk)
            )
        self.deleted = True
        self.date_deleted = timezone.now()
        self.user_deleted = user
        self.save()

    class Meta:
        abstract = True


class TimedCreateModifyDeleteVersionModelManager(models.Manager):

    def _unique_field_name(self):
        try:
            return self.model.UNIQUE_FIELD_NAME
        except AttributeError:
            raise BaseError(
                "'TimedCreateModifyDeleteVersionModel' needs a "
                "'UNIQUE_FIELD_NAME' to find the 'deleted_version'. "
            )

    def _max_deleted_version(self, obj):
        field_name = self._unique_field_name()
        unique_value = getattr(obj, field_name)
        kwargs = {field_name: unique_value}
        qs = self.model.objects.filter(**kwargs)
        result = qs.aggregate(
            max_id=Max('deleted_version')
        )
        return result.get('max_id') or 0

    def set_deleted(self, obj, user):
        max_deleted_version = self._max_deleted_version(obj)
        obj.set_deleted(user, max_deleted_version)


class TimedCreateModifyDeleteVersionModel(TimedCreateModifyDeleteModel):
    """Keep track of deleted versions.

    Written to solve the problem of re-using invoice numbers without having
    to properly delete a row.

    To use the class::

      # 1. inherit from 'TimedCreateModifyDeleteVersionModel'
      class Invoice(TimedCreateModifyDeleteVersionModel):

          # 2. set the unique field name for the model e.g. invoice number
          UNIQUE_FIELD_NAME = 'number'

          # 3. create your unique field e.g. invoice number
          number = models.IntegerField(default=0)

          class Meta:
              # 4. create a unique index on the field and 'deleted_version'
              unique_together = ('number', 'deleted_version')

    Use the model manager to delete a row from the ``Invoice`` model::

      invoice = InvoiceFactory()
      Invoice.objects.set_deleted(obj, user)

    """

    deleted_version = models.IntegerField(default=0)

    def undelete(self):
        self.deleted_version = 0
        super().undelete()

    def set_deleted(self, user, max_deleted_version=None):
        if max_deleted_version is None:
            raise BaseError(
                "'TimedCreateModifyDeleteVersionModel' needs a "
                "'max_deleted_version' to set the 'deleted_version'. "
                "Use the 'set_deleted' method in the model manager for "
                "a model with deleted version tracking."
            )
        self.deleted_version = max_deleted_version + 1
        super().set_deleted(user)

    class Meta:
        abstract = True
