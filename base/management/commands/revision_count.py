# -*- encoding: utf-8 -*-

from django.core.management.base import BaseCommand

from django.apps import apps
# from reversion import revisions as reversion
from reversion.models import Version
from reversion.errors import RegistrationError


class Command(BaseCommand):

    help = "Count reversion records for each model"

    def handle(self, *args, **options):
        total_count = 0
        print_pattern = "{:<15} {:<30s} {:>10d}"
        title_pattern = "{:<15} {:<30s} {:>10s}"
        self.stdout.write(title_pattern.format("App", "Model", "Revisions"))
        self.stdout.write(title_pattern.format("===", "=====", "========="))
        prev_app = None
        for model in sorted(
                apps.get_models(),
                key=lambda mod: mod.__module__ + '.' + mod.__name__):
            app_name = model._meta.app_label
            model_name = model.__name__

            try:
                qs = Version.objects.get_for_model(model)
                count = qs.count()
                total_count += count
                if prev_app and prev_app != app_name:
                    self.stdout.write("")
                self.stdout.write(print_pattern.format(
                    app_name if prev_app != app_name else "",
                    model_name, count
                ))
                prev_app = app_name
            except RegistrationError:
                # model is not registered with reversion ignore
                pass
        self.stdout.write("")
        self.stdout.write(print_pattern.format("Total Records", "", total_count))
