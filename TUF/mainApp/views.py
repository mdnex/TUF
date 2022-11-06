from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.forms import *
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views.generic import View
from django.template.loader import get_template
from . utils import render_to_pdf #created in step 4
from django.utils.encoding import smart_str
import io
import simplejson
from accounts.models import *
from .models import *
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import *

def index(request):
    user = request.user
    users = User.objects.all
    contOp = User.objects.filter(tipo='operadora').count()
    contRen = ""
    args = {'title':'Home','user':user,'users':users,'contRen':contRen,'contOp':contOp}
    return render(request,"index.html",args)
#_---------------------------------------------------
def registar_cliente(request):
    form = ClienteForm(request.POST)
    if request.POST:
        print(form.errors)
        form = ClienteForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_cliente'))
            #return HttpResponseRedirect(reverse('main:registar_cliente',args = {id_apolice}))

    args = {'title':'Registar',"form":form}
    return render(request,"registar_cliente.html",args)

def listar_clientes(request):
    clientes = Cliente.objects.all()

    args = {'title':'Listar',"clientes":clientes}
    return render(request,"listar_clientes.html",args)

def editar_cliente(request,id):
    cliente = Cliente.objects.get(id = id)
    form = ClienteForm(instance = cliente)
    if request.POST:
        form = ClienteForm(request.POST,instance = cliente)
        print(form.data["data_nascimento"])
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:listar_clientes'))

    args = {'title':'Editar',"form":form}
    return render(request,"registar_cliente.html",args)

def eliminar_cliente(request,id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return HttpResponseRedirect(reverse('main:listar_clientes'))
#_---------------------------------------------------
def registar_cartao(request):
    form = CartaoForm(request.POST)
    if request.POST:
        form = CartaoForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_cartao'))

    args = {'title':'Registar',"form":form}
    return render(request,"registar_cartao.html",args)

def listar_cartoes(request):
    cartoes = Cartao.objects.all()

    args = {'title':'Listar',"cartoes":cartoes}
    return render(request,"listar_cartoes.html",args)

def gerar_bilhete(request):
    form = BilheteForm(request.POST)
    lista = Bilhete.objects.all()
    if request.POST:
        print(form.errors)
        form = BilheteForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:gerar_bilhete'))
    args = {'title':'Gerar',"form":form,'lista':lista}
    return render(request,"gerar_bilhete.html",args)

def editar_cartao(request,id):
    cartao = Cartao.objects.get(id = id)
    form = CartaoForm(instance = cartao)
    if request.POST:
        form = CartaoForm(data = request.POST,files = request.FILES,instance = cartao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:listar_cartoes'))

    args = {'title':'Editar',"form":form}
    return render(request,"registar_cartao.html",args)

def eliminar_cartao(request,id):
    cartao = Cartao.objects.get(id = id)
    cartao.delete()
    return HttpResponseRedirect(reverse('main:listar_cartoes'))
#-----------------------------------------------------------------
def registar_carreira(request):
    form = CarreiraForm(request.POST)
    if request.POST:
        form = CarreiraForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_carreira'))

    args = {'title':'Registar',"form":form}
    return render(request,"registar_carreira.html",args)

def listar_carreiras(request):
    carreiras = Carreira.objects.all()

    args = {'title':'Listar',"carreiras":carreiras}
    return render(request,"listar_carreiras.html",args)

def editar_carreira(request,id):
    carreira = Carreira.objects.get(id = id)
    form = CarreiraForm(instance = carreira)
    if request.POST:
        form = CarreiraForm(data = request.POST,files = request.FILES,instance = cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:listar_carreiras'))

    args = {'title':'Editar',"form":form}
    return render(request,"registar_carreira.html",args)

def eliminar_carreira(request,id):
    carreira = Carreira.objects.get(id = id)
    carreira.delete()
    return HttpResponseRedirect(reverse('main:listar_carreiras'))
#------------------------------------------------------------------
def registar_autocarro(request):
    form = AutocarroForm(request.POST)
    if request.POST:
        form = AutocarroForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_autocarro'))

    args = {'title':'Registar',"form":form}
    return render(request,"registar_autocarro.html",args)

def listar_autocarros(request):
    autocarros = Autocarro.objects.all()

    args = {'title':'Listar',"autocarros":autocarros}
    return render(request,"listar_autocarros.html",args)

def associar_autocarro_carreira(request,id):
    autocarro = Autocarro.objects.get(id = id)

    if AutocarroCarreira.objects.filter(autocarro = autocarro):
        autocarro_carreira = AutocarroCarreira.objects.get(autocarro = autocarro)
        form = AutocarroCarreiraForm(instance = autocarro_carreira)
    else:
        form = AutocarroCarreiraForm(data = request.POST)

    if request.POST:
        if AutocarroCarreira.objects.filter(autocarro = autocarro):
            autocarro_carreira = AutocarroCarreira.objects.get(autocarro = autocarro)
            form = AutocarroCarreiraForm(data = request.POST,instance = autocarro_carreira)
        else:
            form = AutocarroCarreiraForm(data = request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.autocarro = autocarro
            f.save()
            return HttpResponseRedirect(reverse('main:listar_autocarros'))

    args = {'title':'Associar',"form":form}
    return render(request,"associar_autocarro_carreira.html",args)

def editar_autocarro(request,id):
    autocarro = Carreira.objects.get(id = id)
    form = AutocarroForm(instance = autocarro)
    if request.POST:
        form = AutocarroForm(data = request.POST,files = request.FILES,instance = autocarro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:listar_autocarros'))

    args = {'title':'Editar',"form":form}
    return render(request,"registar_autocarro.html",args)

def eliminar_autocarro(request,id):
    autocarro = Autocarro.objects.get(id = id)
    autocarro.delete()
    return HttpResponseRedirect(reverse('main:listar_autocarros'))

def registar_avaria_autocarro(request):
    form = AvariaForm(request.POST)
    avarias = Avaria.objects.all()
    if request.POST:
        form = AvariaForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_avaria_autocarro'))

    args = {'title':'Registar',"form":form,'avarias':avarias}
    return render(request,"registar_autocarro.html",args)

def listar_avarias(request):
    avarias = Avaria.objects.all()

    args = {'title':'Listar',"avarias":avarias}
    return render(request,"listar_avarias.html",args)

def enviar_autocarro_sub(request,id):
    carreira = Carreira.objects.get(id = id)

    if AutocarroCarreira.objects.filter(carreira = carreira):
        autocarro_carreira = AutocarroCarreira.objects.get(carreira = carreira)
        form = CarreiraAutocarroForm(instance = autocarro_carreira)
    else:
        form = CarreiraAutocarroForm(data = request.POST)

    if request.POST:
        if AutocarroCarreira.objects.filter(carreira = carreira):
            autocarro_carreira = AutocarroCarreira.objects.get(carreira = carreira)
            form = CarreiraAutocarroForm(data = request.POST,instance = autocarro_carreira)
        else:
            form = CarreiraAutocarroForm(data = request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.carreira = carreira
            f.save()
            return HttpResponseRedirect(reverse('main:listar_carreiras'))

    args = {'title':'Enviar',"form":form}
    return render(request,"associar_autocarro_carreira.html",args)
#-----------------------------------------------------------------------
def registar_paragem(request):
    form = ParagemForm(request.POST)
    paragens = Paragem.objects.all()
    if request.POST:
        form = ParagemForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_paragem'))

    args = {'title':'Registar',"form":form,"paragens":paragens}
    return render(request,"registar_paragem.html",args)

def editar_paragem(request,id):
    paragem = Paragem.objects.get(id = id)
    paragens = Paragem.objects.all()
    form = ParagemForm(instance = paragem)
    if request.POST:
        form = ParagemForm(data = request.POST,files = request.FILES,instance = paragem)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_paragem'))

    args = {'title':'Editar',"form":form,"paragens":paragens}
    return render(request,"registar_paragem.html",args)

def eliminar_paragem(request,id):
    paragem = Paragem.objects.get(id = id)
    paragem.delete()
    return HttpResponseRedirect(reverse('main:registar_paragem'))
#-----------------------------------------------------------------------
def registar_percurso(request):
    form = PercursoForm(request.POST)
    percursos = Percurso.objects.all()
    if request.POST:
        form = PercursoForm(data = request.POST,files = request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_percurso'))

    args = {'title':'Registar',"form":form,"percursos":percursos}
    return render(request,"registar_percurso.html",args)

def editar_percurso(request,id):
    percurso = Percurso.objects.get(id = id)
    percursos = Percurso.objects.all()
    form = PercursoForm(instance = ponto)
    if request.POST:
        form = PercursoForm(data = request.POST,files = request.FILES,instance = percurso)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_percurso'))

    args = {'title':'Editar',"form":form,"percursos":percursos}
    return render(request,"registar_percurso.html",args)

def eliminar_percurso(request,id):
    percurso = Percurso.objects.get(id = id)
    percurso.delete()
    return HttpResponseRedirect(reverse('main:registar_percurso'))
#-----------------------------------------------------------------------
def registar_tipo_carreira(request):
    form = TipoCarreiraForm(request.POST)
    tipo_carreiras = TipoCarreira.objects.all()
    if request.POST:
        form = TipoCarreiraForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_tipo_carreira'))

    args = {'title':'Registar',"form":form,"tipo_carreiras":tipo_carreiras}
    return render(request,"registar_tipo_carreira.html",args)

def editar_tipo_carreira(request,id):
    tipo_carreira = TipoCarreira.objects.get(id = id)
    tipo_carreiras = TipoCarreira.objects.all()
    form = TipoCarreiraForm(instance = ponto)
    if request.POST:
        form = TipoCarreiraForm(data = request.POST,files = request.FILES,instance = tipo_carreira)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_tipo_carreira'))

    args = {'title':'Editar',"form":form,"tipo_carreiras":tipo_carreiras}
    return render(request,"registar_tipo_carreira.html",args)

def eliminar_tipo_carreira(request,id):
    tipo_carreira = TipoCarreira.objects.get(id = id)
    tipo_carreira.delete()
    return HttpResponseRedirect(reverse('main:registar_tipo_carreira'))
#-----------------------------------------------------------------------
def registar_tipo_cartao(request):
    form = TipoCartaoForm(request.POST)
    tipo_cartoes = TipoCartao.objects.all()
    if request.POST:
        form = TipoCartaoForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_tipo_cartao'))

    args = {'title':'Registar',"form":form,"tipo_cartoes":tipo_cartoes}
    return render(request,"registar_tipo_cartao.html",args)

def editar_tipo_cartao(request,id):
    tipo_cartoes = TipoCartao.objects.get(id = id)
    tipo_cartao = TipoCartao.objects.all()
    form = TipoCartaoForm(instance = ponto)
    if request.POST:
        form = TipoCartaoForm(data = request.POST,files = request.FILES,instance = tipo_cartao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_tipo_cartao'))

    args = {'title':'Editar',"form":form,"tipo_cartoes":tipo_cartoes}
    return render(request,"registar_tipo_cartao.html",args)

def eliminar_tipo_cartao(request,id):
    tipo_cartao = TipoCartao.objects.get(id = id)
    tipo_cartao.delete()
    return HttpResponseRedirect(reverse('main:registar_tipo_cartao'))
#-----------------------------------------------------------------------
def registar_tipo_autocarro(request):
    form = TipoAutocarroForm(request.POST)
    tipo_autocarros = TipoAutocarro.objects.all()
    if request.POST:
        form = TipoAutocarroForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_tipo_autocarro'))

    args = {'title':'Registar',"form":form,"tipo_autocarros":tipo_autocarros}
    return render(request,"registar_tipo_autocarro.html",args)

def editar_tipo_autocarro(request,id):
    tipo_autocarro = TipoAutocarro.objects.get(id = id)
    tipo_autocarros = TipoAutocarro.objects.all()
    form = TipoAutocarroForm(instance = tipo_autocarro)
    if request.POST:
        form = TipoAutocarroForm(data = request.POST,files = request.FILES,instance = tipo_autocarro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_tipo_autocarro'))

    args = {'title':'Editar',"form":form,"tipo_autocarros":tipo_autocarros}
    return render(request,"registar_tipo_autocarro.html",args)

def eliminar_tipo_autocarro(request,id):
    tipo_autocarro = TipoCartao.objects.get(id = id)
    tipo_autocarro.delete()
    return HttpResponseRedirect(reverse('main:registar_tipo_autocarro'))
#-----------------------------------------------------------------------_____________________________
def registar_ponto(request):
    form = PontoRegistoForm(request.POST)
    pontos = PontoRegisto.objects.all()
    if request.POST:
        form = PontoRegistoForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_ponto'))

    args = {'title':'Registar',"form":form,"pontos":pontos}
    return render(request,"registar_ponto.html",args)

def editar_pontos(request,id):
    ponto = PontoRegisto.objects.get(id = id)
    form = PontoRegistoForm(instance = ponto)
    pontos = PontoRegisto.objects.all()
    if request.POST:
        form = PontoRegistoForm(data = request.POST,files = request.FILES,instance = ponto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:listar_pontos'))

    args = {'title':'Editar',"form":form,"pontos":pontos}
    return render(request,"registar_ponto.html",args)

def eliminar_ponto(request,id):
    ponto = Ponto.objects.get(id = id)
    ponto.delete()
    return HttpResponseRedirect(reverse('main:registar_ponto'))
#--------------------------------------------------------------------------
def registar_entrada_autocarro(request):
    form = EntradaAutocarroForm(request.POST)

    if request.POST:
        form = EntradaAutocarroForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_entrada_autocarro'))

    args = {'title':'Registar',"form":form,}
    return render(request,"registar_entrada_autocarro.html",args)

def listar_entrada_autocarro(request):
    form = EntradaAutocarroForm(request.POST)
    lista = EntradaAutocarro.objects.all()

    args = {'title':'Listar',"form":form,"lista":lista}
    return render(request,"listar_entrada_autocarro.html",args)

def registar_saida_autocarro(request):
    form = SaidaAutocarroForm(request.POST)
    if request.POST:
        form = SaidaAutocarroForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:registar_saida_autocarro'))

    args = {'title':'Registar',"form":form,}
    return render(request,"registar_paragem.html",args)

def listar_saida_autocarro(request):
    form = ParagemForm(request.POST)
    lista = SaidaAutocarro.objects.all()

    args = {'title':'Listar',"form":form,"lista":lista}
    return render(request,"listar_saida_autocarro.html",args)
#-------------------------------------------------------------------------
def ver_estatistica(request):
    lista = []
    carreiras = Carreira.objects.all()
    autocarro = Autocarro.objects.all()
    clientes = Cliente.objects.all()
    entrada = Autocarro.objects.all()
    saida = Cliente.objects.all()
    if request.GET:
        carreira = request.GET.get('carreira',False)
        data = request.GET.get('data',False)
        tipo = request.GET.get('tipo',"entrada")
        if tipo == "entrada":
            lista = EntradaAutocarro.objects.all()
        else:
            lista  = SaidaAutocarro.objects.all()

        print(lista)

        if data:
            print(data.split("-")[1])
            print(data.split("-")[2])
            lista = lista.filter(data__day = data.split("-")[2],data__month = data.split("-")[1])

        print(lista.values_list("autocarro__autocarrocarreira__carreira"))

        if carreira:
            lista = lista.filter(autocarro__autocarrocarreira__carreira__id = carreira)
            print(lista)

    args = {'title':'Ver',"lista":lista,'carreiras':carreiras,"autocarro":autocarro,"entrada":entrada,"saida":saida,"clientes":clientes}
    return render(request,"ver_estatistica.html",args)
"""#-----------------------------------------------------------------------
def registar_tipo_cliente(request):
    form = TipoClienteForm(request.POST)
    tipo_cliente = TipoCliente.objects.all()
    if request.POST:
        form = TipoClienteForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()

    args = {'title':'title',"form":form,"tipo_clientes":tipo_clientes}
    return render(request,"registar_tipo_cliente.html",args)

def editar_tipo_cliente(request,id):
    tipo_clientes = TipoCliente.objects.get(id = id)
    tipo_cliente = TipoCliente.objects.all()
    form = TipoClienteForm(instance = ponto)
    if request.POST:
        form = TipoClienteForm(data = request.POST,files = request.FILES,instance = tipo_cliente)
        if form.is_valid():
            form.save()

    args = {'title':'title',"form":form,"tipo_clientes":tipo_clientes}
    return render(request,"registar_tipo_cliente.html",args)
"""
