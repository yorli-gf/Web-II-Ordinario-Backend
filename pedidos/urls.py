from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, PedidoViewSet, DetallePedidoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles', DetallePedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
