# Generated by Django 4.1.2 on 2023-03-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projectmanagement", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="machinetranslationprojectunannotatedentry",
            name="mt_system_translation",
            field=models.TextField(
                default="machine translation system translation",
                verbose_name="Reference Translation",
            ),
            preserve_default=False,
        ),
    ]