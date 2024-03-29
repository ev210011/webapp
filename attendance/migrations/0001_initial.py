# Generated by Django 4.2.9 on 2024-02-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                    "in_out",
                    models.IntegerField(
                        choices=[(1, "IN"), (2, "OUT")],
                        default=None,
                        verbose_name="IN/OUT",
                    ),
                ),
                ("time", models.TimeField(verbose_name="打刻時間")),
                ("date", models.DateField(verbose_name="打刻日")),
            ],
        ),
    ]
