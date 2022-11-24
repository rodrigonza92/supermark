from db import detalle_db

class Detalle:
    def __init__(self, id, idFactura, idProducto, cantidad, precio):
        self.__id = id
        self.__idFactura = idFactura
        self.__idProducto = idProducto
        self.__cantidad = cantidad
        self.__precio = precio
    
    @property
    def Id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def idFactura(self):
        return self.__idFactura

    @idFactura.setter
    def idFactura(self, idFactura):
        self.__idFactura = idFactura
    
    @property
    def idProducto(self):
        return self.__idProducto

    @idProducto.setter
    def id(self, idProducto):
        self.__idProducto = idProducto
    
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def id(self, precio):
        self.__precio = precio    

    def crear_detalle(self):
        detalle_db.insertar_detalle(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio)
    
    def editar_detalle(self):
        detalle_db.editar_detalle(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio, self.__id)
    
    def eliminar_detalle(self):
        detalle_db.eliminar_detalle(self.__id)
    
    def ver_detalle(self):
        detalle_db.ver_detalle(self.__id)
    
    def subtotal(self):
        return self.__cantidad * self.__precio