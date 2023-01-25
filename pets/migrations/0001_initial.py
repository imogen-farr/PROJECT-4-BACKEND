# Generated by Django 4.1.5 on 2023-01-22 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environments', '0001_initial'),
        ('lifespans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('animal', models.CharField(max_length=50)),
                ('cover_image', models.CharField(max_length=300)),
                ('environments', models.ManyToManyField(related_name='pets', to='environments.environment')),
                ('lifespans', models.ManyToManyField(related_name='pets', to='lifespans.lifespan')),
            ],
        ),
    ]
