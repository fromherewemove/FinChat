# Generated by Django 4.1.1 on 2022-10-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
