# Generated by Django 4.0.6 on 2022-08-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0019_rename_quantidade_ordemitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
