from django.db import models


TRUE_FALSE_CHOICES = (
        (True, 'Да'),
        (False, 'Нет')
    )


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


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Вопрос')
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
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    choice_text = models.CharField(max_length=200, verbose_name='Вариант ответа')
    scores = models.FloatField(default=0.0, verbose_name='Баллы')
    vote = models.BooleanField(verbose_name='Ответ', default=False, choices=TRUE_FALSE_CHOICES)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответ'
