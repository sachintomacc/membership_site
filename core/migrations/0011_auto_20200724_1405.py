# Generated by Django 2.2.2 on 2020-07-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200723_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='userpreferences',
            name='option_1',
        ),
        migrations.RemoveField(
            model_name='userpreferences',
            name='option_2',
        ),
        migrations.RemoveField(
            model_name='userpreferences',
            name='option_3',
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='preferences',
            field=models.ManyToManyField(to='core.Preference'),
        ),
    ]