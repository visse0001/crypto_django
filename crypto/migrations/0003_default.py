# Generated by Django 3.1.6 on 2021-02-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_producer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
