# Generated by Django 4.1.7 on 2023-07-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0009_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image2',
            field=models.ImageField(blank=True, default='noImg/no_img.jpg', null=True, upload_to='project/'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image3',
            field=models.ImageField(blank=True, default='noImg/no_img.jpg', null=True, upload_to='project/'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image4',
            field=models.ImageField(blank=True, default='noImg/no_img.jpg', null=True, upload_to='project/'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image5',
            field=models.ImageField(blank=True, default='noImg/no_img.jpg', null=True, upload_to='project/'),
        ),
    ]
