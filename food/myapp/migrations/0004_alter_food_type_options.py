# Generated by Django 5.0.7 on 2024-07-22 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_category_options_alter_event_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food_type',
            options={'verbose_name': 'Food Type', 'verbose_name_plural': 'Food Type'},
        ),
    ]
