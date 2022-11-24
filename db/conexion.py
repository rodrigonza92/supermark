import sqlite3

def __init__(self,bd): #bd es el nombre de la base de datos
    self.conexion = sqlite3.connect(bd)
    self.cursor = self.conexion.cursor()

def consulta(self, consulta):
    self.cursor.execute(consulta)
    
def commit(self):
    self.conexion.commit()

def cerrar(self):
    self.conexion.close()

def crear_db(self):
    conexion = conexion('supermark.db')

    try:
        conexion.consulta('CREATE TABLE IF NOT EXISTS Persona(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, dni INTEGER, condicion TEXT)')
        conexion.consulta('CREATE TABLE IF NOT EXISTS Productos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, detalle TEXT, stock INTEGER, precio FLOAT)')
        conexion.consulta('CREATE TABLE IF NOT EXISTS Factura(id INTEGER PRIMARY KEY AUTOINCREMENT, id_persona INTEGER NOT NULL, fecha DATE , estado TEXT, total FLOAT, FOREING KEY (id_persona) REFERENCES Persona (id))')
        conexion.consulta('CREATE TABLE IF NOT EXISTS Detalles(id INTEGER PRIMARY KEY AUTOINCREMENT, id_factura INTEGER NOT NULL, id_producto INTEGER NOT NULL, cantidad INTEGER, precio FLOAT, subtotal FLOAT, FOREING KEY (id_factura) REFERENCES Factura (id), FOREING KEY (id_producto) REFERENCES Producto (id))')
        conexion.commit()
    except:
        print("las Tablas ya fueron creadas") #Imprimir un msj
