# Generated by Django 4.0.5 on 2022-07-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_posts_post_date_alter_posts_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
