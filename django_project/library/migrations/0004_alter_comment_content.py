# Generated by Django 4.0.5 on 2022-08-17 03:02

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]
