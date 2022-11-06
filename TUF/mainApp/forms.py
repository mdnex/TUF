from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(input_formats=['%d/%m/%Y','%d-%m-%Y','%Y-%m-%d'])
    class Meta:
        model =Cliente
        fields = ('nome_completo','contacto','data_nascimento','num_bi')
        labels = {
        'data_nascimento':"Data de Nascimento",
        'num_bi':"Nº de B.I.",
        }
        widgets = {
        'data' : forms.TextInput(
         attrs={'class':'form-control', 'type':'date', 'maxlength': 9}),
        'nome_completo': forms.TextInput(attrs={'class':'form-control',}),
        'contacto': forms.TextInput(attrs={'class':'form-control',}),
        'num_bi': forms.TextInput(attrs={'class':'form-control',}),
        }

class ParagemForm(forms.ModelForm):
    class Meta:
        model =Paragem
        fields = ('nome','localidade')
        widgets = {
        'localidade': forms.TextInput(attrs={'class':'form-control',}),
        'nome': forms.TextInput(attrs={'class':'form-control',}),
        }

class PontoRegistoForm(forms.ModelForm):
    class Meta:
        model =PontoRegisto
        fields = ('nome','paragem')
        widgets = {
        'paragem': forms.Select(attrs={'class':'form-control',}),
        'nome': forms.TextInput(attrs={'class':'form-control',}),
        }

class PercursoForm(forms.ModelForm):
    class Meta:
        model =Percurso
        fields = ('carreira','tipo_percurso','paragem')
        labels = {
        'tipo_percurso':"Tipo de Percurso",
        }
        widgets = {
        'carreira': forms.Select(attrs={'class':'form-control',}),
        'paragem': forms.SelectMultiple(attrs={'class':'form-control',}),
        'tipo_percurso': forms.Select(attrs={'class':'form-control',}),
        }

class CarreiraForm(forms.ModelForm):
    class Meta:
        model =Carreira
        fields = ('tipo_carreira','horario_inicio','horario_fim','ponto_inicio','ponto_fim')
        labels = {
        'tipo_carreira':"Tipo de Carreira",
        'horario_inicio':"Horario de Inicio",
        'horario_fim':"Horario de Fim",
        'ponto_inicio':"Ponto de Inicio",
        'ponto_fim':"Ponto de Termino",
        }
        widgets = {
        'tipo_carreira': forms.Select(attrs={'class':'form-control',}),
        'horario_inicio': forms.TimeInput(attrs={'class':'form-control',}),
        'horario_fim': forms.TimeInput(attrs={'class':'form-control',}),
        'ponto_inicio': forms.Select(attrs={'class':'form-control',}),
        'ponto_fim': forms.Select(attrs={'class':'form-control',}),
        }

class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = ('cliente','carreira','tipo_cartao')
        labels = {
        'tipo_cartao':"Tipo de Cartão",
        }
        widgets = {
        'cliente': forms.Select(attrs={'class':'form-control',}),
        'carreira': forms.Select(attrs={'class':'form-control',}),
        'tipo_cartao': forms.Select(attrs={'class':'form-control',}),
        }

class BilheteForm(forms.ModelForm):
    class Meta:
        model = Bilhete
        fields = ('carreira',)
        widgets = {
        'carreira': forms.Select(attrs={'class':'form-control',}),
        }

class AutocarroForm(forms.ModelForm):
    class Meta:
        model =Autocarro
        fields = ('matricula','lotacao','tipo_autocarro')
        labels = {
        'Tipo de Autocarro':"Tipo de Autocarro",
        }
        widgets = {
        'matricula': forms.TextInput(attrs={'class':'form-control',}),
        'lotacao': forms.NumberInput(attrs={'class':'form-control',}),
        'tipo_autocarro': forms.Select(attrs={'class':'form-control',}),
        }

class AutocarroCarreiraForm(forms.ModelForm):
    class Meta:
        model =AutocarroCarreira
        fields = ('carreira',)
        labels = {
        'Tipo de Autocarro':"Tipo de Autocarro",
        }
        widgets = {
        'autocarro': forms.Select(attrs={'class':'form-control',}),
        'carreira': forms.Select(attrs={'class':'form-control',}),
        }

class CarreiraAutocarroForm(forms.ModelForm):
    class Meta:
        model =AutocarroCarreira
        fields = ('autocarro',)
        labels = {
        'Tipo de Autocarro':"Tipo de Autocarro",
        }
        widgets = {
        'autocarro': forms.Select(attrs={'class':'form-control',}),
        'carreira': forms.Select(attrs={'class':'form-control',}),
        }

class TipoAutocarroForm(forms.ModelForm):
    class Meta:
        model =TipoAutocarro
        fields = ('nome',)
        widgets = {
        'nome': forms.TextInput(attrs={'class':'form-control',}),
        }

class TipoCarreiraForm(forms.ModelForm):
    class Meta:
        model =TipoCarreira
        fields = ('nome',)
        widgets = {
        'nome': forms.TextInput(attrs={'class':'form-control',}),
        }

class TipoCartaoForm(forms.ModelForm):
    class Meta:
        model =TipoCartao
        fields = ('nome',)
        widgets = {
        'nome': forms.TextInput(attrs={'class':'form-control',}),
        }

class EntradaAutocarroForm(forms.ModelForm):
    class Meta:
        model =EntradaAutocarro
        fields = ('autocarro','cartao','ponto_registo')
        widgets = {
        'autocarro': forms.Select(attrs={'class':'form-control',}),
        'cartao': forms.Select(attrs={'class':'form-control',}),
        'bilhete': forms.Select(attrs={'class':'form-control',}),
        'ponto_registo': forms.Select(attrs={'class':'form-control',}),
        }

class SaidaAutocarroForm(forms.ModelForm):
    class Meta:
        model =SaidaAutocarro
        fields = ('autocarro','cartao','ponto_registo')
        widgets = {
        'autocarro': forms.Select(attrs={'class':'form-control',}),
        'cartao': forms.Select(attrs={'class':'form-control',}),
        'bilhete': forms.Select(attrs={'class':'form-control',}),
        'ponto_registo': forms.Select(attrs={'class':'form-control',}),
        }

class AvariaForm(forms.ModelForm):
    class Meta:
        model =Avaria
        fields = ('local','autocarro',)
        widgets = {
        'local': forms.TextInput(attrs={'class':'form-control',}),
        'autocarro': forms.Select(attrs={'class':'form-control',}),
        }
