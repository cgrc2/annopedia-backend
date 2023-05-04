# Generated by Django 4.1.2 on 2023-03-02 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("annotators", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Project Name")),
                ("description", models.TextField(verbose_name="Project Description")),
                (
                    "url",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="Project URL",
                    ),
                ),
                (
                    "talk_markdown",
                    models.TextField(
                        blank=True, null=True, verbose_name="Project Talk Markdown"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Project Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Project Created at"
                    ),
                ),
                (
                    "administrators",
                    models.ManyToManyField(
                        blank=True,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Project Administrators",
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="ProjectEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Project Entry Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Project Entry Created at"
                    ),
                ),
                (
                    "annotator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="annotators.annotator",
                        verbose_name="Annotator",
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectmanagement.project",
                        verbose_name="Project",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="UnannotatedProjectEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Unannotated Text")),
                (
                    "context",
                    models.TextField(blank=True, null=True, verbose_name="Context"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Unannotated Entry Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Unannotated Entry Created at"
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectmanagement.project",
                        verbose_name="Project",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="MachineTranslationProject",
            fields=[
                (
                    "project_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projectmanagement.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("projectmanagement.project",),
        ),
        migrations.CreateModel(
            name="MachineTranslationProjectEntry",
            fields=[
                (
                    "projectentry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projectmanagement.projectentry",
                    ),
                ),
                ("fluency", models.FloatField(verbose_name="Fluency")),
                ("adequacy", models.FloatField(verbose_name="Adequacy")),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("projectmanagement.projectentry",),
        ),
        migrations.CreateModel(
            name="MachineTranslationProjectUnannotatedEntry",
            fields=[
                (
                    "unannotatedprojectentry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projectmanagement.unannotatedprojectentry",
                    ),
                ),
                (
                    "pre_annotation_adequacy",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Pre-annotation adequacy"
                    ),
                ),
                (
                    "pre_annotation_fluency",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Pre-annotation fluency"
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("projectmanagement.unannotatedprojectentry",),
        ),
        migrations.CreateModel(
            name="TextClassificationProject",
            fields=[
                (
                    "project_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projectmanagement.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("projectmanagement.project",),
        ),
        migrations.AddField(
            model_name="projectentry",
            name="unannotated_source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="projectmanagement.unannotatedprojectentry",
                verbose_name="Unannotated Source",
            ),
        ),
        migrations.CreateModel(
            name="HistoricalProjectEntry",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        blank=True,
                        editable=False,
                        verbose_name="Project Entry Created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        blank=True,
                        editable=False,
                        verbose_name="Project Entry Created at",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "annotator",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="annotators.annotator",
                        verbose_name="Annotator",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="projectmanagement.project",
                        verbose_name="Project",
                    ),
                ),
                (
                    "unannotated_source",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="projectmanagement.unannotatedprojectentry",
                        verbose_name="Unannotated Source",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical project entry",
                "verbose_name_plural": "historical project entrys",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Category Name"),
                ),
                (
                    "description",
                    models.CharField(
                        max_length=255, verbose_name="Category Description"
                    ),
                ),
                (
                    "key_binding",
                    models.CharField(max_length=255, verbose_name="Key Bindnig"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Category Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Category Created at"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectmanagement.project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TextClassificationProjectUnannotatedEntry",
            fields=[
                (
                    "unannotatedprojectentry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projectmanagement.unannotatedprojectentry",
                    ),
                ),
                (
                    "pre_annotation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="projectmanagement.category",
                        verbose_name="Pre-annotation classification",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("projectmanagement.unannotatedprojectentry",),
        ),
        migrations.CreateModel(
            name="TextClassificationProjectEntry",
            fields=[
                (
                    "projectentry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="projectmanagement.projectentry",
                    ),
                ),
                (
                    "classification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="projectmanagement.category",
                        verbose_name="Classification",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("projectmanagement.projectentry",),
        ),
    ]