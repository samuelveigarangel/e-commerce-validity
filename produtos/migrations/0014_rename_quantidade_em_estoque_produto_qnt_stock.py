# Generated by Django 4.0.6 on 2022-08-12 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0013_rename_preco_produto_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='quantidade_em_estoque',
            new_name='qnt_stock',
        ),
    ]
