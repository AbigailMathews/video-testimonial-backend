# Generated by Django 3.2 on 2021-05-28 13:33

from django.db import migrations, models
import listen_first.models


class Migration(migrations.Migration):

    dependencies = [
        ('listen_first', '0005_alter_testimonial_media_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='media_file',
            field=models.FileField(upload_to=listen_first.models.testimonial_path),
        ),
    ]