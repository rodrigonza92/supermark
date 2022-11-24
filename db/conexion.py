import sqlite3
class Conexion:
    def __init__(self, bd): #bd es el nombre de la base de datos
        self.conexion = sqlite3.connect(bd)
        self.cursor = self.conexion.cursor()

    def consulta(self, consulta):
        self.cursor.execute(consulta)
        
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()

    def crear_db(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Persona(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, dni INTEGER, condicion TEXT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Productos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, detalle TEXT, stock INTEGER, precio FLOAT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Factura(id INTEGER PRIMARY KEY AUTOINCREMENT, id_persona INTEGER NOT NULL, fecha DATE , estado TEXT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Detalles(id INTEGER PRIMARY KEY AUTOINCREMENT, id_factura INTEGER NOT NULL, id_producto INTEGER NOT NULL, cantidad INTEGER, precio FLOAT)')
        self.conexion.commit()
        self.conexion.close()
        # Puede tener el campo total la tabla de factura si es que se quiere