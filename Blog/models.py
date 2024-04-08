from django.db import models

""" Данные о посте """
class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    author = models.CharField('Author', max_length=100)
    date = models.DateField('Date published')
    img = models.ImageField('Image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'