import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Для создания табл в БД созд класс и откуда он всё наследует

class Articles(models.Model):
    # Каждое поле как отдельное поле в табл
    title = models.CharField('Название', max_length=50)     # Тип данных после . - огр по симв
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')                  # Тип данных после . - без огр по симв
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Статьи: {self.title}'     # При помощи какой информаии будет вводиться каждый объект

    def get_absolute_url(self):             # Переадресовка при обновлении или удалении
        return f'/news/{self.id}'

    @admin.display(
        boolean=True,
        ordering='date',
        description='Опубликовано недавно?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
