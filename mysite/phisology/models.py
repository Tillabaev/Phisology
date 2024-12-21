from enum import unique

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class AboutMe(models.Model):
    bio = models.TextField()
    profession = models.CharField(max_length=35)
    about_me = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='about_me/')
    back_round_img = models.ImageField(upload_to='about_me/')


    def __str__(self):
        return f'{self.profession}'

class MainWorld(models.Model):
    profession = models.CharField(max_length=35)
    main_text = models.CharField(max_length=500)
    publication = models.PositiveSmallIntegerField(help_text='количества публикации')
    follower = models.CharField(max_length=25,help_text='количества подписчиков')
    subscription = models.PositiveSmallIntegerField(help_text='количества людей на которые вы подписаны ')


class Review(models.Model):
    feedback = models.CharField(max_length=35,help_text='отзывы моих клиентов')


class Img(models.Model):
    img = models.ImageField(upload_to='review_img/')
    review_connect = models.ForeignKey(Review,related_name='photo',on_delete=models.CASCADE)


class Consultation(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=512)
    format = models.CharField(max_length=512)
    feedback = models.CharField(max_length=512, help_text='Обратная свзять')
    price = models.PositiveSmallIntegerField(default=100)

    def __str__(self):
        return f'{self.title} - {self.price}'


class Consultation_Keys(models.Model):
    consultation = models.ForeignKey(Consultation, related_name='con_keys', on_delete=models.CASCADE)
    keys = models.CharField(max_length=512)



class My_Services(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.title}'

class Services(models.Model):
    my_services = models.ForeignKey(My_Services, related_name='services', on_delete=models.CASCADE)
    name_services = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveSmallIntegerField(default=200)


    def __str__(self):
        return f'{self.name_services} - {self.price}'



class Registration(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    number = PhoneNumberField(null=True, blank=True)
    telegram = models.CharField(max_length=25,null=True,blank=True)
    country = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.first_name} - {self.email}'
