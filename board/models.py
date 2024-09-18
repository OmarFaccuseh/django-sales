from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import functools


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username


class Instrumento(models.Model):
    name = models.CharField(max_length=250)
    porcentaje_anual = models.FloatField(default=0)
    congelamiento_dias = models.FloatField(default=0)
    monto = models.FloatField(default=0)


    @property
    def gains_mes(self):
        return ((self.monto * self.porcentaje_anual) / 100)/12

    @property
    def gains_anual(self):
        return self.monto * (self.porcentaje_anual/100)


class GainDay(models.Model):
    date = models.CharField(max_length=250)
    mount = models.FloatField(default=0)


class Metricas(models.Model):
    instrumentos = models.ManyToManyField(Instrumento)
    profile = models.ForeignKey(Profile, related_name='metricas_profile', on_delete=models.CASCADE)

    @property
    def gains_mes_total(self):
        return functools.reduce(lambda acc, i: acc + i.gains_mes, self.instrumentos.all(), 0)

    @property
    def gains_anual_total(self):
        return functools.reduce(lambda acc, i : acc + i.gains_anual, self.instrumentos.all(), 0)

    @property
    def total_inversion_total(self):
        return functools.reduce(lambda acc, i: acc + i.monto, self.instrumentos.all(), 0)

    @property
    def prom_porcentaje_anual_total(self):
        return (self.gains_anual_total * 100) / self.total_inversion_total


# # #  Signals  # # #


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


@receiver(post_save, sender=Profile)
def create_metricas(sender, instance, created, **kwargs):
    if created:
        Metricas.objects.create(profile=instance)






