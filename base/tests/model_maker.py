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
