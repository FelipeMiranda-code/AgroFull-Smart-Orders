from django.urls import path
from .views import (
    agregar_al_pedido,
    actualizar_cantidad,
    eliminar_item,
    PedidoPendienteDetailView,
    ConfirmarPedidoView,
    MisPedidosListView,
    resumen_diario,
    exportar_resumen_excel,
    PedidoDetailView,
    generar_excel_diario,

)

urlpatterns = [
    path('carrito/', PedidoPendienteDetailView.as_view(), name='ver_pedido'),
    path('agregar/<int:producto_id>/', agregar_al_pedido, name="agregar_producto"),
    path('actualizar/<int:detalle_id>/', actualizar_cantidad, name="actualizar_cantidad"),
    path('eliminar/<int:detalle_id>/', eliminar_item, name="eliminar_item"),
    path('confirmar/', ConfirmarPedidoView.as_view(), name='confirmar_pedido'),
    path('detalle/<int:pk>/', PedidoDetailView.as_view(), name='ver_pedido_detalle'),

    path('mis-pedidos/', MisPedidosListView.as_view(), name='mis_pedidos'),

    path('resumen-diario/', resumen_diario, name='resumen_diario'),
    path('resumen-diario/excel/', exportar_resumen_excel, name='exportar_resumen_excel'),

    # ✅ ESTE ERA TU ERROR
    path('generar-excel-diario/', generar_excel_diario, name='generar_excel_diario'),

]
