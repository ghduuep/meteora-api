from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from loja.views import ProdutoViewSet, CategoriaViewSet
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Meteora API",
      default_version='v1',
      description="API voltada para e-commerce de roupas",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
)

router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet, basename='categorias')
router.register('produtos', ProdutoViewSet, basename='produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
