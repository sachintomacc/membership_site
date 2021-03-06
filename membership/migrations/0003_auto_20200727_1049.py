# Generated by Django 2.2.2 on 2020-07-27 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0002_auto_20200727_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberpaymenthistory',
            name='payment_id',
        ),
        migrations.AddField(
            model_name='memberpaymenthistory',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memberpaymenthistory',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='membershipdetail',
            name='stripe_customer_id',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membershipdetail',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
