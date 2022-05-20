from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class SkillTag(models.Model):
    """Skill tag model"""
    name = models.CharField(max_length=50, verbose_name= 'Название тега')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    def get_users(self):
        """Get users wit this group of skills to display in admin"""
        return "\n".join([p.username for p in self.user.all()])

    class Meta:
        verbose_name = 'Тег навыка'
        verbose_name_plural = 'Теги навыков'


class SkillValue(models.Model):
    """Skill model"""
    name = models.CharField(max_length=50, verbose_name='Название навыка')
    tag = models.ForeignKey(SkillTag, on_delete=models.CASCADE, verbose_name='Тег')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    def get_users(self):
        """Get users with this skill to display in admin"""
        return "\n".join([p.username for p in self.user.all()])

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
