# Generated by Django 4.0.6 on 2022-08-12 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0015_rename_quantidade_vendida_produto_sold'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='categoria',
            new_name='category',
        ),
    ]