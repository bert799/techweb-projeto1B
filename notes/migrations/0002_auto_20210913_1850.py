# Generated by Django 3.2.7 on 2021-09-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.TextField(default='Escreva Algo', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
