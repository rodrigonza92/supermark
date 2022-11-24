from db import factura_db
from db import detalle_db

class Factura:
    def __init__(self, id, idPersona, fecha, estado, total):
        self.__id = id
        self.__idPersona = idPersona
        self.__fecha = fecha
        self.__estado = estado
        #self.__total = total
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def idPersona(self):
        return self.__idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self.__idPersona = idPersona
    
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
    
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def condicion(self, estado):
        self.__estado = estado
    
    def crear_factura(self):
        factura_db.insertar_factura(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio)
    
    def editar_factura(self):
        factura_db.editar_factura(self.__idFactura, self.__idProducto, self.__cantidad, self.__precio, self.__id)
    
    def eliminar_factura(self):
        factura_db.eliminar_factura(self.__id)
    
    def ver_factura(self):
        factura_db.ver_factura(self.__id)
    
    def total(self):
        datos = detalle_db.ver_detalle(self.__id)
        #total = 0
        """ for dato in datos:
            total += (dato[4] * dato[5])
        return total """

        suma = sum((dato[4] * dato[5]) for dato in datos) #Sirve para hacer grandes sumas
        return suma