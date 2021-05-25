# Generated by Django 3.2 on 2021-05-25 03:31

from django.db import migrations, models
import listen_first.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_id', models.BigIntegerField()),
                ('media_file', models.FileField(upload_to=listen_first.models.testimonial_path)),
                ('media_type', models.CharField(choices=[('A', 'Audio'), ('V', 'Video')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('reviewed', models.BooleanField(default=False)),
            ],
        ),
    ]
