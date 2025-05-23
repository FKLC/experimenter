# Generated by Django 3.0.4 on 2020-04-06 23:36

import django.contrib.postgres.fields
from django.db import migrations, models

import experimenter.legacy.legacy_experiments.models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0089_experiment_total_enrolled_clients"),
    ]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="platforms",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=200),
                blank=True,
                default=experimenter.legacy.legacy_experiments.models.default_all_platforms,
                null=True,
                size=None,
            ),
        ),
    ]
