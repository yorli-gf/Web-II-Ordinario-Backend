from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Producto, Pedido, DetallePedido
from .serializers import ProductoSerializer, PedidoSerializer, DetallePedidoSerializer, DetallePedidoWriteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class DetallePedidoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = DetallePedido.objects.all()
        pedido_id = self.request.query_params.get('pedido')
        if pedido_id:
            queryset = queryset.filter(pedido_id=pedido_id)
        return queryset

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return DetallePedidoWriteSerializer
        return DetallePedidoSerializer

# Create your views here.
