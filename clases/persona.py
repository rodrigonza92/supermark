from db import persona_db
class Persona:
    def __init__(self, id, nombre, apellido, dni, condicion):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__condicion = condicion
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    
    @property
    def condicion(self):
        return self.__condicion

    @condicion.setter
    def id(self, condicion):
        self.__condicion = condicion

    def crear_persona(self):
        persona_db.insertar_persona(self.__nombre, self.__apellido, self.__dni, self.__condicion)
    
    def eliminar_persona(self):
        persona_db.eliminar_persona(self.__dni)
    
    def editar_persona(self):
        persona_db.editar_persona(self.__nombre, self.__apellido, self.__dni, self.__condicion, self.__id)
    
    def ver_persona(self):
        persona_db.ver_persona(self.__dni)