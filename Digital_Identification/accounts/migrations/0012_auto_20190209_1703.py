# Generated by Django 2.1.4 on 2019-02-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190209_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='family_role',
            field=models.CharField(choices=[('m', 'Mother'), ('f', 'Father'), ('c', 'Child')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Family'),
        ),
    ]