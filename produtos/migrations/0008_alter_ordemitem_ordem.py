# Generated by Django 4.0.6 on 2022-08-11 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_remove_ordem_transaction_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemitem',
            name='ordem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.ordem', to_field='number_order'),
        ),
    ]