# Generated by Django 5.1.4 on 2024-12-19 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profession', models.CharField(max_length=35)),
                ('about_me', models.CharField(max_length=25)),
                ('photo', models.ImageField(upload_to='about_me/')),
                ('back_round_img', models.ImageField(upload_to='about_me/')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.CharField(max_length=512)),
                ('format', models.CharField(max_length=512)),
                ('feedback', models.CharField(max_length=512)),
                ('price', models.PositiveSmallIntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='MainWorld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=35)),
                ('main_text', models.CharField(max_length=100)),
                ('publication', models.PositiveSmallIntegerField(help_text='количества публикации')),
                ('follower', models.CharField(help_text='количества подписчиков', max_length=25)),
                ('subscription', models.PositiveSmallIntegerField(help_text='количества людей на которые вы подписаны ')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('number', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(help_text='отзывы моих клиентов', max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation_Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.CharField(max_length=512)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='con_keys', to='phisology.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='review_img/')),
                ('review_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='phisology.review')),
            ],
        ),
    ]
