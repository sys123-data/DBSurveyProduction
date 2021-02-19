# Generated by Django 3.1.6 on 2021-02-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env', models.CharField(default='Production', max_length=50)),
                ('Q1', models.CharField(blank=True, default='', max_length=50)),
                ('Q2', models.CharField(blank=True, default='', max_length=50)),
                ('Q3', models.CharField(blank=True, default='', max_length=50)),
                ('Q4', models.CharField(blank=True, default='', max_length=50)),
                ('LQA', models.CharField(default='Q1', max_length=50)),
                ('Status', models.CharField(default='a', max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
