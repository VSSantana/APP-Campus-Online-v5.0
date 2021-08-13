# Generated by Django 2.2.4 on 2019-12-07 16:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campus_app', '0011_auto_20191120_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='cod_usuario',
        ),
        migrations.AddField(
            model_name='noticia',
            name='usuarios',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]