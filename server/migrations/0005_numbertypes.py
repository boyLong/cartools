# Generated by Django 3.1.6 on 2021-03-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_baseinfo_produce'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberTypeS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumberType', models.CharField(max_length=50, verbose_name='号码种类')),
            ],
        ),
    ]