# Generated by Django 4.1.7 on 2023-07-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0008_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('designation', models.CharField(blank=True, max_length=60, null=True)),
                ('relation', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=35, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
