from django.db import models


class AboutMe(models.Model):
    bio = models.TextField()
    profession = models.CharField(max_length=35)
    about_me = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='about_me/')


class MainWorld(models.Model):
    profession = models.CharField(max_length=35)
    main_text = models.CharField(max_length=100)
    publication = models.PositiveSmallIntegerField(help_text='количества публикации')
    follower = models.CharField(max_length=25,help_text='количества подписчиков')
    subscription = models.PositiveSmallIntegerField()

