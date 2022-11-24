from db import persona_db
class Persona:
    def __init__(self, id, nombre, apellido, dni, condicion):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__condicion = condicion
    
    def crear_persona(self):
        persona_db.insertar_persona(self.__nombre, self.__apellido, self.__dni, self.__condicion)
    
    def eliminar_persona(self):
        persona_db.eliminar_persona(self.__dni)
    
    def editar_persona(self):
        persona_db.editar_persona(self.__nombre, self.__apellido, self.__dni, self.__condicion, self.__id)
    
    def ver_persona(self):
        persona_db.ver_persona(self.__dni)