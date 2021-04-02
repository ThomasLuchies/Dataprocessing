# Generated by Django 3.1.7 on 2021-03-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asteroidApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neoReferenceId', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=60)),
                ('absoluteMagnitude', models.CharField(max_length=10)),
                ('estDiaInKmMin', models.CharField(max_length=10)),
                ('estDiaInKmMax', models.CharField(max_length=10)),
                ('estDiaInMMin', models.CharField(max_length=10)),
                ('estDiaInMMax', models.CharField(max_length=10)),
                ('estDiaInMilesMin', models.CharField(max_length=10)),
                ('estDiaInMilesMax', models.CharField(max_length=10)),
                ('estDiaInFeetMin', models.CharField(max_length=10)),
                ('estDiaInFeetMax', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
