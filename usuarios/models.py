from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):

    ROLES = [
        ('usuario', 'Usuario'),
        ('administrador', 'Administrador'),
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='usuario'
    )

    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):

    if created:
        Perfil.objects.create(usuario=instance)