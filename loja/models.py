from django.db import models
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=1000, blank=True, null=True)
    preco = models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(0.00)], blank=False, null=False)
    quantidade_estoque = models.IntegerField(blank=False, null=False)
    categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    imagem = models.URLField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome