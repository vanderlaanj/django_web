# Generated by Django 5.0.4 on 2024-06-20 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='akce',
            options={'ordering': ['datum'], 'verbose_name': 'Akce', 'verbose_name_plural': 'Akce'},
        ),
    ]