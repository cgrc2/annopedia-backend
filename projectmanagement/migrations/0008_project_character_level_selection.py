# Generated by Django 4.1.2 on 2023-04-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "projectmanagement",
            "0007_alter_namedentityrecognitionprojectentry_ner_text_highlights",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="character_level_selection",
            field=models.BooleanField(
                null=True, verbose_name="Character or Word level selection"
            ),
        ),
    ]
