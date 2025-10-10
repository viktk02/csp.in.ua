from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.exceptions import ValidationError
from core.utils import upload_to_factory
from core.validators import validate_file_size

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError('Може існувати тільки один об\'єкт %(class)s')
        return super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class CarouselImage(models.Model):
    image = models.ImageField(
        upload_to=upload_to_factory('carousel'),
        validators=[validate_file_size],
        )
    caption = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Карусель фотографії'
        verbose_name_plural = 'Карусель фотографії'

    def __str__(self):
        return self.caption or f"Image {self.id}"

class PartnerLogo(models.Model):
    ROW_CHOICES = [(1, 'Верхній ряд'), (2, 'Нижній ряд')]
    image = models.ImageField(
        upload_to=upload_to_factory('partners'),
        validators=[validate_file_size],
        )
    name = models.CharField(max_length=100)
    row = models.PositiveSmallIntegerField(choices=ROW_CHOICES)

    class Meta:
        verbose_name = 'Логотипи партнерів'
        verbose_name_plural = 'Логотипи партнерів'

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    text = CKEditor5Field('Text', config_name='default')

    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Про нас'

    def __str__(self):
        return 'Про нас'

class MainPage(SingletonModel):
    text = CKEditor5Field('Text', config_name='default')

    class Meta:
        verbose_name = 'Текст головної сторінки'
        verbose_name_plural = 'Текст головної сторінки'
