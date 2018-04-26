from django.db import models
from django import forms
from django.contrib.admin import widgets
from django.utils import timezone
import datetime

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
    nombro_eblaj_elektoj = models.PositiveSmallIntegerField(
        'nombro da eblaj elektoj',
        default=1)
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

    def clean(self):
        if self.nombro_eblaj_elektoj >= self.elekto_set.count():
            raise ValidationError(
                "La nombro da elektoj por voĉdoni devas esti malpli ol la entuta kvanto de malsimilaj elektoj"
            )


class ProponoForm(forms.ModelForm):
    class Meta:
        model = Propono
        fields = ['titolo', 'enhavo', 'pub_dato', 'fin_dato', 'tipo',
                  'nombro_eblaj_elektoj']
        localized_fields = ['pub_dato', 'fin_dato']

    def __init__(self, *args, **kwargs):
        super(ProponoForm, self).__init__(*args, **kwargs)
        #self.fields['pub_dato'].widget = forms.SelectDateTimeWidget()
        #self.fields['fin_dato'].widget = forms.SelectDateTimeWidget()
        #self.fields['pub_dato'].widget = widgets.AdminSplitDateTime()
        self.fields['pub_dato'].initial = timezone.localtime()
        self.fields['fin_dato'].initial = timezone.localtime() \
                + datetime.timedelta(days=7)

class Elekto(models.Model):
    class Meta:
        verbose_name_plural = 'elektoj'
    enhavo = models.CharField(max_length=128)
    ligita_propono = models.ForeignKey(Propono, on_delete=models.CASCADE)

    def __str__(self):
        return self.enhavo

class Vocxdono(models.Model):
    class Meta:
        verbose_name_plural = 'voĉdonoj'
    uzanto = models.ForeignKey(User)
    vocxo = models.ForeignKey(Elekto)
    dato = models.DateTimeField('dato de la voĉdono')

    def __str__(self):
        return "{self.uzanto}: {self.vocxo}".format(self=self)

