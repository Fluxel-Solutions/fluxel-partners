# Generated by Django 3.1.2 on 2020-10-22 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'status'},
        ),
        migrations.AlterModelOptions(
            name='typecategory',
            options={'verbose_name_plural': 'type categories'},
        ),
        migrations.RemoveField(
            model_name='typecategory',
            name='order_type',
        ),
    ]
