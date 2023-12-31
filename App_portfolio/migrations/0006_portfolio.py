# Generated by Django 4.1.7 on 2023-07-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0005_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, max_length=40, null=True)),
                ('gitlink', models.CharField(blank=True, max_length=30, null=True)),
                ('projectURL', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, default='noImg/no_img.jpg', null=True, upload_to='project/')),
            ],
        ),
    ]
