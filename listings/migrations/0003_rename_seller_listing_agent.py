# Generated by Django 4.1.5 on 2023-02-03 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_agent_listing_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='seller',
            new_name='agent',
        ),
    ]
