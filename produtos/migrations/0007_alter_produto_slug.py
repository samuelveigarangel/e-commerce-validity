# Generated by Django 4.0.6 on 2022-07-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_alter_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
