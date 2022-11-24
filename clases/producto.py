from db import productos_db
class Producto:
    def __init__(self, id, nombre, detalle, stock, precio):
        self.__id = id
        self.__nombre = nombre
        self.__detalle = detalle
        self.__stock = stock
        self.__precio = precio
    
    def crear_producto(self):
        productos_db.insertar_producto(self.__nombre, self.__detalle, self.__stock, self.__precio)
    
    def eliminar_producto(self):
        productos_db.eliminar_producto(self.__id)
    
    def editar_producto(self):
        productos_db.editar_producto(self.__nombre, self.__detalle, self.__stock, self.__precio, self.__id)
    
    def ver_producto(self):
        productos_db.ver_producto(self.__id)