# Generated by Django 2.2.2 on 2020-07-27 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0010_membershiptype_membership_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpaymenthistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
