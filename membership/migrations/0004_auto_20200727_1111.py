# Generated by Django 2.2.2 on 2020-07-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20200727_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershiptype',
            name='stripe_monthly_product_id',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membershiptype',
            name='stripe_yearly_product_id',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]
