from django.db import models
from django.dispatch import receiver
from django.db.models import signals
from django.utils.text import slugify


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default='slug')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


@receiver(signals.pre_save, sender=MenuItem)
def populate_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
