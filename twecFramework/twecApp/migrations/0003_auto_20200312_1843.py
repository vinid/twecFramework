# Generated by Django 3.0.4 on 2020-03-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twecApp', '0002_auto_20200311_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name_document',
        ),
        migrations.AlterField(
            model_name='document',
            name='document_path',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
