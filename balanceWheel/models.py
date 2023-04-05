from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Вопрос')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='id вопроса')
    choice_text = models.CharField(max_length=200, verbose_name='Вариант ответа')
    votes = models.IntegerField(default=0, verbose_name='Выбор')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'выбор'
        verbose_name_plural = 'выбор'
