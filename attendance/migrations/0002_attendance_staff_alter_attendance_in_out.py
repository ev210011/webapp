# Generated by Django 4.2.9 on 2024-02-11 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("attendance", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance",
            name="staff",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="スタッフ",
            ),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="in_out",
            field=models.IntegerField(
                choices=[("1", "IN"), ("2", "OUT")], default=None, verbose_name="IN/OUT"
            ),
        ),
    ]
