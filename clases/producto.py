from db import productos_db
class Producto:
    def __init__(self, nombre, detalle, stock, precio):
        self.__nombre = nombre
        self.__detalle = detalle
        self.__stock = stock
        self.__precio = precio
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def detalle(self):
        return self.__detalle

    @detalle.setter
    def detalle(self, detalle):
        self.__detalle = detalle
    
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock
    
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def crear_producto(self):
        productos_db.insertar_producto(self.__nombre, self.__detalle, self.__stock, self.__precio)
    
    def eliminar_producto(self, codigo):
        productos_db.eliminar_producto(codigo)
    
    def editar_producto(self, codigo):
        productos_db.editar_producto(self.__nombre, self.__detalle, self.__stock, self.__precio, codigo)
    
    def ver_producto(self, codigo):
        productos_db.ver_producto(codigo)
    
    def ver_todo(self):
        productos_db.ver_todos()