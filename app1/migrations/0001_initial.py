# Generated by Django 3.1.3 on 2020-12-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('size', models.PositiveIntegerField(default=0)),
                ('file_type', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
