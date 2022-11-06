from  django.urls import path
from django.conf.urls import url
from . import views

app_name= 'main'
urlpatterns = [
    url(r"home",views.index,name="index"),
    url(r"registar_cliente",views.registar_cliente,name="registar_cliente"),
    url(r"listar_clientes",views.listar_clientes,name="listar_clientes"),
    url(r"editar_cliente/(?P<id>[\w-]+)",views.editar_cliente,name="editar_cliente"),
    url(r"eliminar_cliente/(?P<id>[\w-]+)",views.eliminar_cliente,name="eliminar_cliente"),
    url(r"registar_cartao",views.registar_cartao,name="registar_cartao"),#########################3
    url(r"listar_cartoes",views.listar_cartoes,name="listar_cartoes"),
    url(r"gerar_bilhete",views.gerar_bilhete,name="gerar_bilhete"),
    url(r"editar_cartao/(?P<id>[\w-]+)",views.editar_cartao,name="editar_cartao"),
    url(r"eliminar_cartao/(?P<id>[\w-]+)",views.eliminar_cartao,name="eliminar_cartao"),
    url(r"registar_carreira",views.registar_carreira,name="registar_carreira"),####################3
    url(r"listar_carreiras",views.listar_carreiras,name="listar_carreiras"),
    url(r"editar_carreira/(?P<id>[\w-]+)",views.editar_carreira,name="editar_carreira"),
    url(r"eliminar_carreira/(?P<id>[\w-]+)",views.eliminar_carreira,name="eliminar_carreira"),
    url(r"registar_autocarro",views.registar_autocarro,name="registar_autocarro"),####################3
    url(r"listar_autocarros",views.listar_autocarros,name="listar_autocarros"),
    url(r"associar_autocarro_carreira/(?P<id>[\w-]+)",views.associar_autocarro_carreira,name="associar_autocarro_carreira"),
    url(r"editar_autocarro/(?P<id>[\w-]+)",views.editar_autocarro,name="editar_autocarro"),
    url(r"registar_avaria_autocarro",views.registar_avaria_autocarro,name="registar_avaria_autocarro"),
    url(r"listar_avarias",views.listar_avarias,name="listar_avarias"),
    url(r"enviar_autocarro_sub/(?P<id>[\w-]+)",views.enviar_autocarro_sub,name="enviar_autocarro_sub"),
    url(r"eliminar_autocarro/(?P<id>[\w-]+)",views.eliminar_autocarro,name="eliminar_autocarro"),
    url(r"registar_ponto",views.registar_ponto,name="registar_ponto"),####################3
    url(r"editar_pontos/(?P<id>[\w-]+)",views.editar_pontos,name="editar_pontos"),
    url(r"eliminar_ponto/(?P<id>[\w-]+)",views.eliminar_ponto,name="eliminar_ponto"),
    url(r"registar_paragem",views.registar_paragem,name="registar_paragem"),####################3
    url(r"editar_paragem/(?P<id>[\w-]+)",views.editar_paragem,name="editar_paragem"),
    url(r"eliminar_paragem/(?P<id>[\w-]+)",views.eliminar_paragem,name="eliminar_paragem"),
    url(r"registar_percurso",views.registar_percurso,name="registar_percurso"),####################3
    url(r"editar_percurso/(?P<id>[\w-]+)",views.editar_percurso,name="editar_percurso"),
    url(r"eliminar_percurso/(?P<id>[\w-]+)",views.eliminar_percurso,name="eliminar_percurso"),
    url(r"registar_tipo_carreira",views.registar_tipo_carreira,name="registar_tipo_carreira"),####################3
    url(r"editar_tipo_carreira(?P<id>[\w-]+)",views.editar_tipo_carreira,name="editar_tipo_carreira"),
    url(r"eliminar_tipo_carreira/(?P<id>[\w-]+)",views.eliminar_tipo_carreira,name="eliminar_tipo_carreira"),
    url(r"registar_tipo_cartao",views.registar_tipo_cartao,name="registar_tipo_cartao"),####################3
    url(r"editar_tipo_cartao/(?P<id>[\w-]+)",views.editar_tipo_cartao,name="editar_tipo_cartao"),
    url(r"eliminar_tipo_cartao/(?P<id>[\w-]+)",views.eliminar_tipo_cartao,name="eliminar_tipo_cartao"),
    url(r"registar_tipo_autocarro",views.registar_tipo_autocarro,name="registar_tipo_autocarro"),####################3
    url(r"editar_tipo_autocarro/(?P<id>[\w-]+)",views.editar_tipo_autocarro,name="editar_tipo_autocarro"),
    url(r"eliminar_tipo_autocarro/(?P<id>[\w-]+)",views.eliminar_tipo_autocarro,name="eliminar_tipo_autocarro"),
    url(r"registar_entrada_autocarro",views.registar_entrada_autocarro,name="registar_entrada_autocarro"),####################3
    url(r"listar_entrada_autocarro",views.listar_entrada_autocarro,name="listar_entrada_autocarro"),
    url(r"listar_saida_autocarro",views.listar_saida_autocarro,name="listar_saida_autocarro"),
    url(r"registar_saida_autocarro",views.registar_saida_autocarro,name="registar_saida_autocarro"),
    url(r"ver_estatistica",views.ver_estatistica,name="ver_estatistica"),####################3

    #path(r'^ajax/chat/$', views.broadcast,name="broadcast"),
]
