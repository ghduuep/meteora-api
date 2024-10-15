from rest_framework import viewsets
from loja.models import Categoria, Produto
from loja.serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome', 'categoria__nome', 'preco']
