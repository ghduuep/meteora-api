from django.contrib import admin
from loja.models import Produto, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nome', 'descricao']
    list_display = ['id', 'nome', 'descricao', 'categoria', 'quantidade_estoque']
    list_display_links = ['nome', 'categoria', 'descricao']
    list_per_page = 20
    list_filter = ['preco']

admin.site.register(Produto, ProdutoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nome', 'descricao']
    list_display = ['id', 'nome', 'descricao']
    list_display_links = ['nome', 'descricao']
    list_per_page = 20
    list_filter = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
