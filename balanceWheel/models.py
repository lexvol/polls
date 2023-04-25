from django.contrib.auth import settings
from django.db import models


TRUE_FALSE_CHOICES = (
        (True, 'Да'),
        (False, 'Нет')
    )

class Poll(models.Model):
    poll_name = models.CharField(max_length=100, verbose_name='Название опроса')
    poll_type = models.CharField(max_length=50, verbose_name='Тип опроса')

    def __str__(self):
        return self.poll_name

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'

class Category(models.Model):
    category_name = models.CharField(max_length=30, verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=30, verbose_name='Подкатегория')

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


class Branch(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    branch_name = models.CharField(max_length=100, verbose_name='Имя ветка')

    def __str__(self):
        return self.branch_name

    class Meta:
        verbose_name = 'ветка'
        verbose_name_plural = 'ветки'


class Question(models.Model):
    poll = models.ForeignKey(Poll,
                                  null=True,
                                  blank=True,
                                  related_name='poll',
                                  on_delete=models.CASCADE,
                                  verbose_name='Название теста')
    question_text = models.CharField(max_length=200, verbose_name='Вопрос')
    branch = models.ForeignKey(Branch,
                               null=True,
                               blank=True,
                               related_name='branch',
                               on_delete=models.CASCADE,
                               verbose_name='Ветка')
    category = models.ForeignKey(Category,
                                 related_name='categoty_name',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')
    subcategory = models.ForeignKey(Subcategory,
                                    related_name='subcategoty_name',
                                    on_delete=models.CASCADE,
                                    verbose_name='Подкатегория')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 verbose_name='Вопрос')
    choice_text = models.CharField(max_length=200, verbose_name='Вариант ответа')
    points = models.FloatField(default=0.0, verbose_name='Баллы')
    value = models.BooleanField(null=True, blank=True, default=None, verbose_name='Значение')
    link = models.ForeignKey(Question,
                             related_name='link',
                             null=True,
                             blank=True,
                             default=None,
                             on_delete=models.SET_NULL,
                             verbose_name='Переход')
    vote = models.BooleanField(default=False, choices=TRUE_FALSE_CHOICES, verbose_name='Ответ')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответ'


class Result(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    result = models.CharField(max_length=150, verbose_name='Результат теста')

    def __str__(self):
        return self.result

    class Meta:
        verbose_name = 'результат'
        verbose_name_plural = 'результаты'
