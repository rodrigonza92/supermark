import db.detalle_db as detalle_db
import db.factura_db as factura_db
import db.persona_db as persona_db
from clases import detalle

class Factura:
    def __init__(self):
        self.__idPersona = 0
        # self.__fecha = fecha ---> no la coloco porque se coloca automaticamente
        self.__estado = ""
        self.__total = 0
    
    @property
    def idPersona(self):
        return self.__idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self.__idPersona = idPersona
    
    """ @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha """
    
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado
    
    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total  
    
    def crear_factura(self, dni): #Ingresa su DNI la persona y se recuperan sus datos para hacer la factura
        dp = persona_db.ver_persona(dni)
        self.__idPersona = dp[0][0]
        self.__estado = dp[0][4]
        self.__total = self.sum_total()
        factura_db.insertar_factura(self.__idPersona, self.__estado, self.__total)
    
    def editar_factura(self, idPersona, fecha, estado, codigo):
        factura_db.editar_factura(idPersona, fecha, estado, codigo)
    
    def eliminar_factura(self, codigo):
        factura_db.eliminar_factura(codigo)
    
    def ver_factura(self, codigo):
        return factura_db.ver_factura(codigo)
    
    
    def sum_total(self):
        datos = detalle_db.ver_detalle(1)
        """ total = 0
        for dato in datos:
            total += (dato[4] * dato[5])
        return total """
        
        total = sum((dato[5]) for dato in datos) #Sirve para hacer grandes sumas
        return total
    