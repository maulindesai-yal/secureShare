# Generated by Django 5.0.7 on 2024-07-25 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_accessrequest_shareddocument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='shareddocument',
            name='document',
        ),
        migrations.RemoveField(
            model_name='shareddocument',
            name='shared_with',
        ),
        migrations.DeleteModel(
            name='AccessRequest',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='SharedDocument',
        ),
    ]
