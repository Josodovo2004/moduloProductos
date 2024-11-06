from django.urls import path
from .views import (
    SegmentoProductoListCreateView,
    SegmentoProductoRetrieveUpdateDestroyView,
    FamiliaProductoListCreateView,
    FamiliaProductoRetrieveUpdateDestroyView,
    ClaseProductoListCreateView,
    ClaseProductoRetrieveUpdateDestroyView,
    ProductoListCreateView,
    ProductoRetrieveUpdateDestroyView,
    TipoPrecioListCreateView,
    TipoPrecioRetrieveUpdateDestroyView,
    UnidadMedidaListCreateView,
    UnidadMedidaRetrieveUpdateDestroyView,
    ItemListCreateView,
    ItemRetrieveUpdateDestroyView,
    ItemImpuestoListCreateView,
    ItemImpuestoRetrieveUpdateDestroyView,
    CategoriaListCreateView,
    CategoriaRetrieveUpdateDestroyView,
    ConjuntoItemListCreateView,
    ConjuntoListCreateView,
    ConjuntoRetrieveUpdateDestroyView,
    ConjuntoItemRetrieveUpdateDestroyView,
    resumenItems,
    ajustarStock,
    GeneratePresignedUrlView,
)

urlpatterns = [
    path('segmento-productos/', SegmentoProductoListCreateView.as_view(), name='segmento-producto-list-create'),
    path('segmento-productos/<pk>/', SegmentoProductoRetrieveUpdateDestroyView.as_view(), name='segmento-producto-detail'),
    
    path('familia-productos/', FamiliaProductoListCreateView.as_view(), name='familia-producto-list-create'),
    path('familia-productos/<pk>/', FamiliaProductoRetrieveUpdateDestroyView.as_view(), name='familia-producto-detail'),
    
    path('clase-productos/', ClaseProductoListCreateView.as_view(), name='clase-producto-list-create'),
    path('clase-productos/<pk>/', ClaseProductoRetrieveUpdateDestroyView.as_view(), name='clase-producto-detail'),
    
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<pk>/', ProductoRetrieveUpdateDestroyView.as_view(), name='producto-detail'),
    
    path('tipo-precios/', TipoPrecioListCreateView.as_view(), name='tipo-precio-list-create'),
    path('tipo-precios/<pk>/', TipoPrecioRetrieveUpdateDestroyView.as_view(), name='tipo-precio-detail'),
    
    path('unidad-medidas/', UnidadMedidaListCreateView.as_view(), name='unidad-medida-list-create'),
    path('unidad-medidas/<pk>/', UnidadMedidaRetrieveUpdateDestroyView.as_view(), name='unidad-medida-detail'),
    
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),

    path('item-impuesto/', ItemImpuestoListCreateView.as_view(), name='item-tax-list-create'),
    path('item-impuesto/<pk>/', ItemImpuestoRetrieveUpdateDestroyView.as_view(), name='item-tax-detail'),

    path('categoria/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categoria/<pk>/', CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-detail'),
    
    path('conjuntos/', ConjuntoListCreateView.as_view(), name='conjunto-list-create'),
    path('conjuntos/<int:pk>/', ConjuntoRetrieveUpdateDestroyView.as_view(), name='conjunto-detail'),

    path('conjunto-items/', ConjuntoItemListCreateView.as_view(), name='conjuntoitem-list-create'),
    path('conjunto-items/<int:pk>/', ConjuntoItemRetrieveUpdateDestroyView.as_view(), name='conjuntoitem-detail'),
    
    path('generate-presigned-url/', GeneratePresignedUrlView.as_view(), name='generate-presigned-url'),
    path('ajustar_stock/', ajustarStock, name='ajustar-stock'),

    path('resumen/', resumenItems, name='resumen')
]
