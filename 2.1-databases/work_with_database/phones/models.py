from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50, verbose_name='Name')
    price = models.IntegerField(blank=True, verbose_name='Price')
    image = models.ImageField(blank=True, verbose_name='Image')
    release_date = models.DateField(blank=True, verbose_name='Release')
    lte_exists = models.BooleanField(verbose_name='LTE')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}, {self.price}, {self.release_date}, {self.lte_exists}'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
