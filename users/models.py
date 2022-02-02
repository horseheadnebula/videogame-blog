from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
        ('n', 'Не указан'),
    )

    user_name = models.CharField('Никнейм', max_length=255, unique=True)
    email = models.EmailField('Электронная почта', max_length=255)

    first_name = models.CharField('Имя', max_length=255, default='')
    last_name = models.CharField('Фамилия', max_length=255, default='')
    middle_name = models.CharField('Отчество', max_length=255, default='')

    gender = models.CharField('Пол', max_length=1, default='n')

    birth_date = models.DateField('Дата рождения', default='')
