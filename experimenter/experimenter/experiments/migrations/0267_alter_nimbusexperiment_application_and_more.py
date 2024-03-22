# Generated by Django 5.0.3 on 2024-03-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0266_nimbusexperiment_results_pairwise_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nimbusexperiment",
            name="application",
            field=models.CharField(
                choices=[
                    ("firefox-desktop", "Firefox Desktop"),
                    ("fenix", "Firefox for Android (Fenix)"),
                    ("ios", "Firefox for iOS"),
                    ("focus-android", "Focus for Android"),
                    ("klar-android", "Klar for Android"),
                    ("focus-ios", "Focus for iOS"),
                    ("klar-ios", "Klar for iOS"),
                    ("monitor-web", "Monitor Web"),
                    ("vpn-web", "VPN Web"),
                    ("fxa-web", "Firefox Accounts Web"),
                    ("demo-app", "Demo App"),
                ],
                max_length=255,
                verbose_name="Application Type",
            ),
        ),
        migrations.AlterField(
            model_name="nimbusfeatureconfig",
            name="application",
            field=models.CharField(
                blank=True,
                choices=[
                    ("firefox-desktop", "Firefox Desktop"),
                    ("fenix", "Firefox for Android (Fenix)"),
                    ("ios", "Firefox for iOS"),
                    ("focus-android", "Focus for Android"),
                    ("klar-android", "Klar for Android"),
                    ("focus-ios", "Focus for iOS"),
                    ("klar-ios", "Klar for iOS"),
                    ("monitor-web", "Monitor Web"),
                    ("vpn-web", "VPN Web"),
                    ("fxa-web", "Firefox Accounts Web"),
                    ("demo-app", "Demo App"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="nimbusisolationgroup",
            name="application",
            field=models.CharField(
                choices=[
                    ("firefox-desktop", "Firefox Desktop"),
                    ("fenix", "Firefox for Android (Fenix)"),
                    ("ios", "Firefox for iOS"),
                    ("focus-android", "Focus for Android"),
                    ("klar-android", "Klar for Android"),
                    ("focus-ios", "Focus for iOS"),
                    ("klar-ios", "Klar for iOS"),
                    ("monitor-web", "Monitor Web"),
                    ("vpn-web", "VPN Web"),
                    ("fxa-web", "Firefox Accounts Web"),
                    ("demo-app", "Demo App"),
                ],
                max_length=255,
            ),
        ),
    ]
