from django import forms
from django.forms import ModelForm
from .models import Noticia, WhatsAppAccount
from django.contrib.auth.models import User


class NoticiaForm(forms.ModelForm):

    usuarios = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=User.objects.exclude(is_active='False').order_by('first_name'),
            required=True)

    class Meta:
        
        model = Noticia
        fields = ['usuarios', 'titulo', 'texto', 'prioridade',
                  'link_externo', 'link_video', 'link_foto', 'autoria_midia']


class WhatsAppAccountCreateForm(forms.ModelForm):

    class Meta:

        model = WhatsAppAccount
        fields = ['numero_telefone']
        labels = {'numero_telefone':'Número de WhatsApp do Campus'}

    def __init__(self, *args, **kwargs):

        super(WhatsAppAccountCreateForm, self).__init__(*args, **kwargs)
        self.fields['numero_telefone'].widget.attrs.update({'class' : 'numero_telefone', 'placeholder' : 'Ex.: 5561987654321'})

