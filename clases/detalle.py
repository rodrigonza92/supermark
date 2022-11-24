from db import detalle_db
class Detalle:
    def __init__(self, id, idFactura, idProducto, cantidad, precio, subtotal):
        self.__id = id
        self.__idFactura = idFactura
        self.__idProducto = idProducto
        self.__cantidad = cantidad
        self.__precio = precio
        self.__subtotal = subtotal
    
    def crear_detalle(self):
        detalle_db.insertar_detalle(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio)
    
    def editar_detalle(self):
        detalle_db.editar_detalle(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio, self.__id)
    
    def eliminar_detalle(self):
        detalle_db.eliminar_detalle(self.__id)
    
    def ver_detalle(self):
        detalle_db.ver_detalle(self.__id)