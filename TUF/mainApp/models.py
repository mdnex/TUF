from django.db import models
from time import time

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=100)
    contacto = models.CharField(max_length=9)
    data_nascimento = models.DateField()
    num_bi = models.CharField(max_length=14)

    def __str__(self):
        return "{}".format(self.nome_completo)

    def get_short_name(self):
        return "{}".format(self.nome_completo)

class Paragem(models.Model):
    nome = models.CharField(max_length=100)
    localidade = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nome)

class PontoRegisto(models.Model):
    nome = models.CharField(max_length=100)
    paragem = models.ForeignKey(Paragem,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return "{}".format(self.nome)

    def get_nome(self):
        if self == PontoRegisto.objects.first():
            return "{}".format(self.nome)
        else:
            return "-{}".format(self.nome)

class TipoAutocarro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nome)

class Autocarro(models.Model):
    matricula = models.CharField(max_length=100,unique=True)
    lotacao = models.IntegerField()
    tipo_autocarro = models.ForeignKey(TipoAutocarro,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return "{}".format(self.matricula)

class TipoCarreira(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nome)

class Carreira(models.Model):
    tipo_carreira = models.ForeignKey(TipoCarreira,on_delete=models.CASCADE,null = True)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    ponto_inicio = models.ForeignKey(Paragem,on_delete=models.CASCADE,null = True,related_name="ponto_inicio")
    ponto_fim = models.ForeignKey(Paragem,on_delete=models.CASCADE,null = True,related_name="ponto_fim")

    def __str__(self):
        return "CAR_{}|{} - {}|{}".format(self.id,self.ponto_inicio,self.ponto_fim,self.tipo_carreira)

class AutocarroCarreira(models.Model):
    carreira = models.ForeignKey(Carreira,on_delete=models.CASCADE,null = True)
    autocarro = models.ForeignKey(Autocarro,on_delete=models.CASCADE,null = True)


class Percurso(models.Model):
    carreira = models.ForeignKey(Carreira,on_delete=models.CASCADE,null = True)
    tipo_percurso = models.CharField(max_length=10,choices=(("ida","ida"),("Volta","Volta")))
    paragem = models.ManyToManyField(Paragem)

    def __str__(self):
        return "{} {}".format(self.tipo_percurso,self.id)

class TipoCartao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nome)

class Cartao(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null = True)
    carreira = models.ForeignKey(Carreira,on_delete=models.CASCADE,null = True)
    tipo_cartao = models.ForeignKey(TipoCartao,on_delete=models.CASCADE,null = True)

    def __str__(self):
        if self.id<10:
            return "C-TUF-2021-000{}".format(self.id)
        else:
            return "C-TUF-2021-00{}".format(self.id)
class Bilhete(models.Model):
    carreira = models.ForeignKey(Carreira,on_delete=models.CASCADE,null = True)

    def __str__(self):
        if self.id<10:
            return "B-2021-000{}".format(self.id)
        else:
            return "B-2021-00{}".format(self.id)

class EntradaAutocarro(models.Model):
    autocarro = models.ForeignKey(Autocarro,on_delete=models.CASCADE,null = True)
    cartao = models.ForeignKey(Cartao,on_delete=models.CASCADE,null = True)
    bilhete = models.ForeignKey(Bilhete,on_delete=models.CASCADE,null = True)
    ponto_registo = models.ForeignKey(PontoRegisto,on_delete=models.CASCADE,null = True)
    data = models.DateTimeField(auto_now=True)

class SaidaAutocarro(models.Model):
    autocarro = models.ForeignKey(Autocarro,on_delete=models.CASCADE,null = True)
    cartao = models.ForeignKey(Cartao,on_delete=models.CASCADE,null = True)
    bilhete = models.ForeignKey(Bilhete,on_delete=models.CASCADE,null = True)
    ponto_registo = models.ForeignKey(PontoRegisto,on_delete=models.CASCADE,null = True)
    data = models.DateTimeField(auto_now=True)

TIPO_ = (("Avaria","Avaria"),("Substituicao","Substituicao"))
class Avaria(models.Model):
    tipo = models.CharField(max_length=20,choices=TIPO_)
    local = models.CharField(null=False, max_length=100)
    autocarro = models.ForeignKey(Autocarro,on_delete=models.CASCADE,null = True)

# Create your models here.
