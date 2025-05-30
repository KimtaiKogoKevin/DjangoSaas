# Generated by Django 5.0.11 on 2025-04-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0019_usersubscription_current_period_end_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersubscription",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("active", "Active"),
                    ("free_trial", "Free Trial"),
                    ("incomplete", "Incomplete"),
                    ("incomplete_expired", "Incomplete Expired"),
                    ("past_due", "Past Due"),
                    ("canceled", "Cancelled"),
                    ("unpaid", "Unpaid"),
                    ("paused", "Paused"),
                ],
                max_length=120,
                null=True,
            ),
        ),
    ]
