# Generated by Django 3.2 on 2022-01-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_studentinfo_studentrollnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='StudentRollNumber',
            field=models.CharField(max_length=10),
        ),
    ]