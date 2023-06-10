# Generated by Django 4.2.2 on 2023-06-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_disasters19002021_reconstruction_costs_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disasters",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("year", models.IntegerField(default=0)),
                ("seq", models.IntegerField(default=0)),
                ("glide", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "disaster_group",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "disaster_subgroup",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "disaster_type",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "disaster_subtype",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "disaster_subsubtype",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("event_name", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
                ("iso", models.CharField(blank=True, max_length=255, null=True)),
                ("region", models.CharField(blank=True, max_length=255, null=True)),
                ("continent", models.CharField(blank=True, max_length=255, null=True)),
                ("location", models.TextField(blank=True, null=True)),
                ("origin", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "associated_dis",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "associated_dis2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "ofda_response",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("appeal", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "declaration",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "aid_contribution",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("dis_mag_value", models.IntegerField(default=0)),
                (
                    "dis_mag_scale",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("latitude", models.CharField(blank=True, max_length=255, null=True)),
                ("longitude", models.CharField(blank=True, max_length=255, null=True)),
                ("local_time", models.CharField(blank=True, max_length=255, null=True)),
                ("river_basin", models.TextField(blank=True, null=True)),
                ("start_year", models.IntegerField(default=0)),
                ("start_month", models.IntegerField(default=0)),
                ("start_day", models.IntegerField(default=0)),
                ("end_year", models.IntegerField(default=0)),
                ("end_month", models.IntegerField(default=0)),
                ("end_day", models.IntegerField(default=0)),
                ("total_deaths", models.IntegerField(default=0)),
                ("no_injured", models.IntegerField(default=0)),
                ("no_affected", models.IntegerField(default=0)),
                ("no_homeless", models.IntegerField(default=0)),
                ("total_affected", models.IntegerField(default=0)),
                ("insured_damages", models.IntegerField(default=0)),
                ("total_damages", models.IntegerField(default=0)),
                (
                    "cpi",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=12),
                ),
                ("adm_level", models.CharField(blank=True, max_length=255, null=True)),
                ("admin1_code", models.TextField(blank=True, null=True)),
                ("admin2_code", models.TextField(blank=True, null=True)),
                ("geo_locations", models.TextField(blank=True, null=True)),
                ("reconstruction_costs", models.IntegerField(default=0)),
            ],
        ),
    ]
