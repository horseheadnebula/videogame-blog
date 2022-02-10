from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    email = models.EmailField('Электронная почта', max_length=255)

    first_name = models.CharField('Имя', max_length=255, default='')
    last_name = models.CharField('Фамилия', max_length=255, default='')
    middle_name = models.CharField('Отчество', max_length=255, default='')

    birth_date = models.DateField('Дата рождения', default='1900-01-01')
