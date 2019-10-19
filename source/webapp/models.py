from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=1000, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:20]


class Choice(models.Model):
    variation = models.TextField(max_length=200, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', verbose_name='Вопрос', related_name='poll', on_delete=models.CASCADE)

    def __str__(self):
        return self.variation[:20]


