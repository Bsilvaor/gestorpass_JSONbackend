# Generated by Django 5.0.1 on 2024-02-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userJSON', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='clave',
            field=models.CharField(default='255', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.DeleteModel(
            name='Password',
        ),
    ]
