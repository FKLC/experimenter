# Generated by Django 3.2.15 on 2022-10-13 17:50

import copy

from django.db import migrations


def analysis_add_basis(apps, schema_editor):
    NimbusExperiment = apps.get_model("experiments", "NimbusExperiment")
    windows = ["daily", "weekly", "overall"]
    default_analysis_basis = "enrollments"
    for experiment in NimbusExperiment.objects.all():
        new_data = {}
        results = experiment.results_data
        if results is not None and "v2" not in results:
            data = results["v1"]
            new_data["v1"] = copy.deepcopy(data)
            if data is not None:
                for key, value in data.items():
                    if (
                        value is not None
                        and key in windows
                        and default_analysis_basis not in value
                    ):
                        data[key] = {}
                        data[key][default_analysis_basis] = value
                    else:
                        data[key] = value

            new_data["v2"] = data
            experiment.results_data = new_data
            experiment.save()


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0223_analysis_add_schema_version"),
    ]

    operations = [
        migrations.RunPython(analysis_add_basis),
    ]
