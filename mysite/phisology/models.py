from django.db import models


class AboutMe(models.Model):
    bio = models.TextField()
    profession = models.CharField(max_length=35)
    about_me = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='about_me/')
    back_round_img = models.ImageField(upload_to='about_me/')


class MainWorld(models.Model):
    profession = models.CharField(max_length=35)
    main_text = models.CharField(max_length=100)
    publication = models.PositiveSmallIntegerField(help_text='количества публикации')
    follower = models.CharField(max_length=25,help_text='количества подписчиков')
    subscription = models.PositiveSmallIntegerField(help_text='количества людей на которые вы подписаны ')


class Review(models.Model):

    feedback = models.CharField(max_length=35,help_text='отзывы моих клиентов')


class Img(models.Model):
    img = models.ImageField(upload_to='review_img/')
    review_connect = models.ForeignKey(Review,related_name='photo',on_delete=models.CASCADE)