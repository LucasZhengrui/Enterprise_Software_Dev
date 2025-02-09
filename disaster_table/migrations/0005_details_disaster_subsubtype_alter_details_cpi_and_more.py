# Generated by Django 4.1.7 on 2023-03-21 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_table', '0004_alter_details_total_damages_usd'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='Disaster_Subsubtype',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='CPI',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='details',
            name='OFDA_Response',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='Total_Damages_usd',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='Total_Damages',
            field=models.TextField(default='0'),
        ),
    ]
