import subprocess
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _

class Language(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name=_('Language Code'))
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')

@receiver(post_save, sender=Language)
def create_language_handler(sender, instance, created, **kwargs):
    if created:
        # Ativar o idioma correspondente
        activate(instance.code)
        # Executar o comando makemessages
        subprocess.run(['python', 'manage.py', 'makemessages', '--noinput'])
