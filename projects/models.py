from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from core.utils import upload_to_factory
from core.validators import validate_file_size


class Project(models.Model):
    title = models.CharField(max_length=120)
    content = CKEditor5Field('Content', config_name='default')
    date_posted = models.DateTimeField()
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to=upload_to_factory('images/projects'),
        validators=[validate_file_size],
        blank=True,
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.pk)])

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'
