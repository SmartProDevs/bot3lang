# Generated by Django 2.2.7 on 2021-12-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0014_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='heading_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]
