# Generated by Django 4.1.2 on 2023-03-13 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "projectmanagement",
            "0002_machinetranslationprojectunannotatedentry_mt_system_translation",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="category",
            unique_together={
                ("project", "name", "description"),
                ("project", "name"),
                ("project", "key_binding"),
            },
        ),
    ]
