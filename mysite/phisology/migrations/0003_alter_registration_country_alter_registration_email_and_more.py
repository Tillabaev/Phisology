# Generated by Django 5.1.4 on 2024-12-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phisology', '0002_alter_mainworld_main_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='country',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='last_name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='telegram',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]