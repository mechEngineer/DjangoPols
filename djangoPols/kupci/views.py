from django.shortcuts import render
from django.views.generic.edit import CreateView
from kupci.forms import KontaktiUnos, TvrtkeUnos

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Tvrtke, Kontakti


def index_kupci(request):
    return render(request=request,
                  template_name="kupci/index.html",
                  context={"tvrtke": Tvrtke.objects.all, "kontakti": Kontakti.objects.all})


# Create neew Tvrtka
class TvrtkeCreateView(CreateView):
    def get(self, request, id=None):
        if id:
            tvrtka = get_object_or_404(Tvrtke, pk=id)
            tvrtka_form = TvrtkeUnos(instance=tvrtka)
            kontakti = tvrtka.kontakti_set.all()
            kontakti_form = [KontaktiUnos(prefix=str(
                kontakt.id), instance=kontakt) for kontakt in kontakti]
            template = 'kupci/tvrtke_edit.html'
        else:
            tvrtka_form = TvrtkeUnos
            kontakti_form = [KontaktiUnos(prefix=str(
                knt), instance=Kontakti()) for knt in range(3)]
            template = 'kupci/tvrtke_novo.html'
        context = {'tvrtka_form': tvrtka_form, 'kontakti_form': kontakti_form}
        return render(request, template, context)
    # model = Tvrtke
    # fields = '__all__'
    # def post(self, request):
    #     context = {}
    #     tvrtke_form = TvrtkeUnos(request.POST, instance=Tvrtke())
    #     kontakti_form = KontaktiUnos()

    #template_name = ".html"
