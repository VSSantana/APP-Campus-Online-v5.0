# Generated by Django 3.2.3 on 2021-06-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_app', '0014_whatsappaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='autoria_midia',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
