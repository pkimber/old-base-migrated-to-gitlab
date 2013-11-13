from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


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


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
