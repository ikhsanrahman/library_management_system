# Generated by Django 4.2.4 on 2023-08-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library_system", "0003_alter_borrowing_borrowed_on_alter_borrowing_due_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowing",
            name="borrowed_status",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="borrowing",
            name="returned_status",
            field=models.BooleanField(default=False),
        ),
    ]
