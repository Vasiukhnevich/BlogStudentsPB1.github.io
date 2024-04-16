from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('НАЗВАНИЕ', max_length=50)
    anons = models.CharField('АНОНС', max_length=250)
    full_text = models.TextField('СТАТЬЯ')
    date = models.DateTimeField('ДАТА ПУБЛИКАЦИИ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'