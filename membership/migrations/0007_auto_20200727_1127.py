# Generated by Django 2.2.2 on 2020-07-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_membershipdetail_membership_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipdetail',
            name='membership_term',
            field=models.CharField(choices=[('M', 'Monthly'), ('Y', 'Yearly')], max_length=50),
        ),
    ]
