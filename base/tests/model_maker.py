# -*- encoding: utf-8 -*-
from django.contrib.sites.models import Site


def clean_and_save(model_instance):
    """
    Validate and save a model instance.

    Calling 'save' or 'create' (e.g. 'TimeRecord.objects.create') does not call
    the validation methods.

    We have to call 'full_clean' after 'save' because in some cases, the 'save'
    method updates the row.
    """
    model_instance.save()
    model_instance.full_clean()
    return model_instance


def init_site(pk, name, domain):
    """Use this for setting up initial sites."""
    try:
        site = Site.objects.get(pk=pk)
        site.name = name
        site.domain = domain
        site.save()
    except Site.DoesNotExist:
        site = clean_and_save(
            Site(**dict(pk=pk, name=name, domain=domain))
        )
    return site
