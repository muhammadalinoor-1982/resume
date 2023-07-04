# Generated by Django 4.1.7 on 2023-07-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0002_work_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('degree', models.CharField(blank=True, max_length=40, null=True)),
                ('major', models.CharField(blank=True, max_length=25, null=True)),
                ('logo', models.ImageField(blank=True, default='noImg/no_img.jpg', null=True, upload_to='logo/')),
                ('image', models.ImageField(blank=True, default='noImg/no_img.jpg', null=True, upload_to='certificate/')),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
