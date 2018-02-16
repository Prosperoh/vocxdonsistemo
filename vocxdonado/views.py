from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Propono, Vocxdono

class IndexView(generic.ListView):
    template_name = 'vocxdonado/index.html'
    context_object_name = 'listo_proponoj'

    def get_queryset(self):
        """ Sendas ĉiujn proponojn en datumbazo """
        return Propono.objects.all().order_by('fin_dato')

class DetalojView(LoginRequiredMixin, generic.DetailView):
    login_url='/login/'

    model = Propono
    template_name = 'vocxdonado/detaloj.html'

    def get_queryset(self):
        return Propono.objects.filter(pub_dato__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super(DetalojView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@login_required
def vocxdoni(request, propono_id):
    propono = get_object_or_404(Propono, pk=propono_id)
    try:
        elektitajxo = propono.elekto_set.get(pk=request.POST['elekto'])
    except (KeyError, Elekto.DoesNotExist):
        return render(request, 'vocxdonado/detaloj.html', {
            'propono': propono,
            'error_message': "Bonvole elektu iun el la voĉeblecoj.",
        })
    else:
        vocxdono = Vocxdono(uzanto=None, vocxo=elektitajxo,
                dato=timezone.now())
        vocxdono.save()
        return HttpResponseRedirect(reverse('vocxdonado:detaloj',
            args=(propono.id,)))

