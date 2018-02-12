from django.contrib import admin
from django import forms

from .models import Propono, Elekto, Vocxdono

# Register your models here.

class ElektoInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        # Kontrolas, ĉu ĉiuj elektoj estas malsamaj unu de la alia
        count_elektoj = {}
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['enhavo'] in count_elektoj:
                    raise forms.ValidationError("Elektoj estus malsamaj unu de la alia.")
                count_elektoj[form.cleaned_data['enhavo']] = 0


class ElektoInline(admin.StackedInline):
    formset = ElektoInlineFormSet
    model = Elekto
    extra = 3

class ProponoForm(forms.ModelForm):
    class Meta:
        model = Propono
        fields = '__all__'

    def clean(self):
        # Datoj
        pub_dato = self.cleaned_data.get('pub_dato')
        fin_dato = self.cleaned_data.get('fin_dato')
        if fin_dato <= pub_dato:
            raise forms.ValidationError("Propono devas fini post publikiĝi, bonvole korektu datojn.",
                    code='invalid')
        return self.cleaned_data

class ProponoAdmin(admin.ModelAdmin):
    form = ProponoForm
    inlines = [ElektoInline]

admin.site.register(Propono, ProponoAdmin)
admin.site.register(Vocxdono)

