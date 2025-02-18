# Generated by Django 4.2.16 on 2025-01-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("subscriptions", "0004_subscription_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="permissions",
            field=models.ManyToManyField(
                limit_choices_to={
                    "codename__in": ["advanced", "pro", "basic", "basic_ai"],
                    "content_type__app_label": "subscriptions",
                },
                to="auth.permission",
            ),
        ),
    ]
