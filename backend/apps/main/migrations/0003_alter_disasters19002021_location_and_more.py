# Generated by Django 4.2.2 on 2023-06-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_disasters19002021_adm_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disasters19002021",
            name="location",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="disasters19702021",
            name="location",
            field=models.TextField(blank=True, null=True),
        ),
    ]
