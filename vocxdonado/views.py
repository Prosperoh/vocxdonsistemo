from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Propono, Vocxdono

class IndexView(generic.ListView):
    template_name = 'vocxdonado/index.html'
    context_object_name = 'listo_proponoj'

    def get_queryset(self):
        """ Sendas ĉiujn proponojn en datumbazo """
        return Propono.objects.all().order_by('fin_dato')

class DetalojView(generic.DetailView):
    model = Propono
    template_name = 'vocxdonado/detaloj.html'

    def get_queryset(self):
        return Propono.objects.filter(pub_dato__lte=timezone.now())
