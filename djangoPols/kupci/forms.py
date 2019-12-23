from django import forms
from .models import Tvrtke, Kontakti, TipTvrtke


class KontaktiUnos(forms.ModelForm):
    class Meta:
        model = Kontakti
        fields = '__all__'


class TvrtkeUnos(forms.ModelForm):
    class Meta:
        model = Tvrtke
        fields = '__all__'
