# Generated by Django 4.0.6 on 2022-09-15 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0004_alter_produto_options_categoria_slug_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="categoria",
            old_name="nome",
            new_name="name",
        ),
    ]