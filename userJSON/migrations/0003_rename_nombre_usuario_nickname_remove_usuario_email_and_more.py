# Generated by Django 5.0.1 on 2024-02-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userJSON', '0002_usuario_clave_alter_usuario_email_delete_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='nickname',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='clave',
            field=models.CharField(max_length=255),
        ),
    ]
