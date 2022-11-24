from db import factura_db
class Factura:
    def __init__(self, id, idPersona, fecha, estado, total):
        self.__id = id
        self.__idPersona = idPersona
        self.__fecha = fecha
        self.__estado = estado
        self.__total = total
    
    def crear_factura(self):
        factura_db.insertar_factura(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio)
    
    def editar_factura(self):
        factura_db.editar_factura(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio, self.__id)
    
    def eliminar_factura(self):
        factura_db.eliminar_factura(self.__id)
    
    def ver_factura(self):
        factura_db.ver_factura(self.__id)