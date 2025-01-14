# Generated by Django 5.1.3 on 2025-01-14 10:14

import django.db.models.deletion
import phonenumber_field.modelfields
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
                ('bio_en', models.TextField(null=True)),
                ('bio_ru', models.TextField(null=True)),
                ('bio_ky', models.TextField(null=True)),
                ('profession', models.CharField(max_length=35)),
                ('profession_en', models.CharField(max_length=35, null=True)),
                ('profession_ru', models.CharField(max_length=35, null=True)),
                ('profession_ky', models.CharField(max_length=35, null=True)),
                ('about_me', models.CharField(max_length=25)),
                ('about_me_en', models.CharField(max_length=25, null=True)),
                ('about_me_ru', models.CharField(max_length=25, null=True)),
                ('about_me_ky', models.CharField(max_length=25, null=True)),
                ('photo', models.ImageField(upload_to='about_me/')),
                ('back_round_img', models.ImageField(upload_to='about_me/')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('title_en', models.CharField(max_length=512, null=True)),
                ('title_ru', models.CharField(max_length=512, null=True)),
                ('title_ky', models.CharField(max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_ky', models.TextField(blank=True, null=True)),
                ('duration', models.CharField(max_length=512)),
                ('duration_en', models.CharField(max_length=512, null=True)),
                ('duration_ru', models.CharField(max_length=512, null=True)),
                ('duration_ky', models.CharField(max_length=512, null=True)),
                ('format', models.CharField(max_length=512)),
                ('format_en', models.CharField(max_length=512, null=True)),
                ('format_ru', models.CharField(max_length=512, null=True)),
                ('format_ky', models.CharField(max_length=512, null=True)),
                ('feedback', models.CharField(help_text='Обратная свзять', max_length=512)),
                ('feedback_en', models.CharField(help_text='Обратная свзять', max_length=512, null=True)),
                ('feedback_ru', models.CharField(help_text='Обратная свзять', max_length=512, null=True)),
                ('feedback_ky', models.CharField(help_text='Обратная свзять', max_length=512, null=True)),
                ('price', models.PositiveSmallIntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='MainWorld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=35)),
                ('profession_en', models.CharField(max_length=35, null=True)),
                ('profession_ru', models.CharField(max_length=35, null=True)),
                ('profession_ky', models.CharField(max_length=35, null=True)),
                ('main_text', models.CharField(max_length=500)),
                ('main_text_en', models.CharField(max_length=500, null=True)),
                ('main_text_ru', models.CharField(max_length=500, null=True)),
                ('main_text_ky', models.CharField(max_length=500, null=True)),
                ('publication', models.PositiveSmallIntegerField(help_text='количества публикации')),
                ('follower', models.CharField(help_text='количества подписчиков', max_length=25)),
                ('follower_en', models.CharField(help_text='количества подписчиков', max_length=25, null=True)),
                ('follower_ru', models.CharField(help_text='количества подписчиков', max_length=25, null=True)),
                ('follower_ky', models.CharField(help_text='количества подписчиков', max_length=25, null=True)),
                ('subscription', models.PositiveSmallIntegerField(help_text='количества людей на которые вы подписаны ')),
                ('main_photo', models.ImageField(blank=True, null=True, upload_to='main_photo/')),
            ],
        ),
        migrations.CreateModel(
            name='My_Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('title_en', models.CharField(max_length=32, null=True)),
                ('title_ru', models.CharField(max_length=32, null=True)),
                ('title_ky', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patterns', models.CharField(choices=[('pattern 1', 'pattern 1'), ('pattern 2 ', 'pattern 2 ')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Public_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.CharField(blank=True, max_length=35, null=True)),
                ('main_en', models.CharField(blank=True, max_length=35, null=True)),
                ('main_ru', models.CharField(blank=True, max_length=35, null=True)),
                ('main_ky', models.CharField(blank=True, max_length=35, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(blank=True, max_length=100, null=True)),
                ('questions_en', models.CharField(blank=True, max_length=100, null=True)),
                ('questions_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('questions_ky', models.CharField(blank=True, max_length=100, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('answer_en', models.TextField(blank=True, null=True)),
                ('answer_ru', models.TextField(blank=True, null=True)),
                ('answer_ky', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('telegram', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(help_text='отзывы моих клиентов', max_length=35)),
                ('feedback_en', models.CharField(help_text='отзывы моих клиентов', max_length=35, null=True)),
                ('feedback_ru', models.CharField(help_text='отзывы моих клиентов', max_length=35, null=True)),
                ('feedback_ky', models.CharField(help_text='отзывы моих клиентов', max_length=35, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Safety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('title_en', models.CharField(blank=True, max_length=250, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=250, null=True)),
                ('title_ky', models.CharField(blank=True, max_length=250, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text_en', models.TextField(blank=True, null=True)),
                ('text_ru', models.TextField(blank=True, null=True)),
                ('text_ky', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SafetyMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety_name', models.CharField(max_length=55)),
                ('safety_name_en', models.CharField(max_length=55, null=True)),
                ('safety_name_ru', models.CharField(max_length=55, null=True)),
                ('safety_name_ky', models.CharField(max_length=55, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation_Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.CharField(max_length=512)),
                ('keys_en', models.CharField(max_length=512, null=True)),
                ('keys_ru', models.CharField(max_length=512, null=True)),
                ('keys_ky', models.CharField(max_length=512, null=True)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='con_keys', to='phisology.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='Public_offerText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('title_en', models.CharField(blank=True, max_length=500, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=500, null=True)),
                ('title_ky', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text_en', models.TextField(blank=True, null=True)),
                ('text_ru', models.TextField(blank=True, null=True)),
                ('text_ky', models.TextField(blank=True, null=True)),
                ('connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phisology.public_offer')),
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
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_services', models.CharField(max_length=255)),
                ('name_services_en', models.CharField(max_length=255, null=True)),
                ('name_services_ru', models.CharField(max_length=255, null=True)),
                ('name_services_ky', models.CharField(max_length=255, null=True)),
                ('text1', models.TextField(blank=True, null=True)),
                ('text1_en', models.TextField(blank=True, null=True)),
                ('text1_ru', models.TextField(blank=True, null=True)),
                ('text1_ky', models.TextField(blank=True, null=True)),
                ('price', models.PositiveSmallIntegerField(default=200)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text2_en', models.TextField(blank=True, null=True)),
                ('text2_ru', models.TextField(blank=True, null=True)),
                ('text2_ky', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('text3_en', models.TextField(blank=True, null=True)),
                ('text3_ru', models.TextField(blank=True, null=True)),
                ('text3_ky', models.TextField(blank=True, null=True)),
                ('text4', models.TextField(blank=True, null=True)),
                ('text4_en', models.TextField(blank=True, null=True)),
                ('text4_ru', models.TextField(blank=True, null=True)),
                ('text4_ky', models.TextField(blank=True, null=True)),
                ('main_img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('my_services', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='phisology.my_services')),
                ('pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phisology.pattern')),
            ],
        ),
        migrations.CreateModel(
            name='ImgServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='services_photo/')),
                ('services_text', models.TextField(blank=True, null=True)),
                ('services_text_en', models.TextField(blank=True, null=True)),
                ('services_text_ru', models.TextField(blank=True, null=True)),
                ('services_text_ky', models.TextField(blank=True, null=True)),
                ('services_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='phisology.services')),
            ],
        ),
        migrations.CreateModel(
            name='Services_Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.CharField(blank=True, max_length=512, null=True)),
                ('keys_en', models.CharField(blank=True, max_length=512, null=True)),
                ('keys_ru', models.CharField(blank=True, max_length=512, null=True)),
                ('keys_ky', models.CharField(blank=True, max_length=512, null=True)),
                ('services_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_keys', to='phisology.services')),
            ],
        ),
    ]
