from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django import forms
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib.auth.models import User
from .models import Propono, ProponoForm, Elekto, Vocxdono

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url='/login/'

    template_name = 'vocxdonado/index.html'
    context_object_name = 'listo_proponoj'

    def get_queryset(self):
        """ Sendas ĉiujn proponojn en datumbazo """
        return Propono.objects.all().order_by('fin_dato')

class UzantojView(LoginRequiredMixin, generic.ListView):
    login_url='/login/'

    template_name = 'vocxdonado/uzantoj.html'
    context_object_name = 'listo_uzantoj'

    def get_queryset(self):
        """ Sendas ĉiujn uzantojn en la datumbazo """
        return User.objects.all()

class ProponojView(LoginRequiredMixin, generic.DetailView):
    login_url='/login/'

    model = Propono
    template_name = 'vocxdonado/detaloj.html'

    def get_queryset(self):
        return Propono.objects.filter(pub_dato__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super(ProponojView, self).get_context_data(**kwargs)
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
        vocxdono = Vocxdono(uzanto=request.user, vocxo=elektitajxo,
                dato=timezone.now())
        vocxdono.save()
        return redirect(reverse('vocxdonado:detaloj', args=(propono.id,)))

@login_required
def krei_proponon(request):
    if request.method == 'POST':
        form = ProponoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # do something.
            return redirect(reverse('vocxdonado:index'))
        else:
            return render(request, 'vocxdonado/krei_proponon.html', {'form': form})
    else:
        form = ProponoForm()
        #ElektoInlineFormSet = forms.inlineformset_factory(Propono, Elekto,
        #                                                  fields=('enhavo',))
        return render(request, 'vocxdonado/krei_proponon.html', {'form': form})
