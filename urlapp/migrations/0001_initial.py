# Generated by Django 4.0.2 on 2022-02-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('times_followed', models.PositiveIntegerField(default=0)),
                ('short_url', models.CharField(blank=True, max_length=15, unique=True)),
                ('data', models.TextField()),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
