# Generated by Django 3.1.6 on 2021-02-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_baseinfo_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseinfo',
            name='produce',
            field=models.CharField(default='', max_length=50, verbose_name='制造商'),
        ),
    ]