from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Propono(models.Model):
    class Meta:
        verbose_name_plural = 'proponoj'
    titolo = models.CharField(max_length=128)
    enhavo = models.TextField()
    pub_dato = models.DateTimeField('publikiĝdato')
    fin_dato = models.DateTimeField('findato')
    tipo = models.CharField(
            max_length=128,
            choices= ( ('normala_sekreta', 'Normala sekreta'),
                       ('normala_publika', 'Normala publika'),
                       ('elekto_estraro', 'Elekto de estraro'),
                       ('elekto_komitatano_c', 'Elekto de komitatano C'),
                       ('estraro_sekreta', 'Nur sekreta, por la estraro'),
                       ('estraro_publika', 'Nur publika, por la estraro')
                       )
            )

    def __str__(self):
        return self.titolo

class Elekto(models.Model):
    class Meta:
        verbose_name_plural = 'elektoj'
    enhavo = models.CharField(max_length=128)
    ligita_propono = models.ForeignKey(Propono, on_delete=models.CASCADE)

    def __str__(self):
        return self.enhavo

    def validate_unique(self, exclude=None):
        el = Elekto.objects.filter(enhavo=self.enhavo)
        if el.filter(ligita_propono=self.ligita_propono).exists():
            raise ValidationError("Elektoj ne estu samaj.")

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(Elekto, self).save(*args, **kwargs)

class Vocxdono(models.Model):
    class Meta:
        verbose_name_plural = 'vocxdonoj'
    uzanto = models.ForeignKey(User)
    vocxo = models.ForeignKey(Elekto)
    dato = models.DateTimeField('dato de la voĉdono')

    def __str__(self):
        return self.uzanto + ": " + self.vocxo.__str__()

