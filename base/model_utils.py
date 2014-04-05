# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import AutoField


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
