# Generated by Django 2.1.4 on 2019-01-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190117_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='pp',
            field=models.CharField(default='/static/Images/def.jpeg', max_length=255),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
