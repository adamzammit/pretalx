from django.dispatch import receiver
from pretalx.common.signals import register_data_exporters

from django_cas_ng.signals import cas_user_authenticated

@receiver(cas_user_authenticated)
def cas_update(sender, **kwargs):
    print("CAS UPDATE")
    print(kwargs)


@receiver(register_data_exporters, dispatch_uid="exporter_builtin_csv_speaker")
def register_speaker_csv_exporter(sender, **kwargs):
    from .exporters import CSVSpeakerExporter

    return CSVSpeakerExporter
