from db.conexion import Conexion
from datetime import datetime

db = 'supermark.db'
def insertar_factura(idPersona, estado, total):
    conexion = Conexion(db)
    fecha = (datetime.now()).date()
    conexion.consulta(f'INSERT INTO Factura VALUES(NULL,{idPersona},"{fecha}","{estado}",{total})')
    conexion.commit()
    conexion.cerrar()

def eliminar_factura(codigo):
    conexion = Conexion(db)
    conexion.consulta(f'DELETE FROM Factura WHERE id={codigo}')
    conexion.commit()
    conexion.cerrar()

def editar_factura(id_persona, estado, codigo):
    conexion = Conexion(db)
    fecha = fecha = (datetime.now()).date()
    conexion.consulta(f'UPDATE Factura SET id_persona = {id_persona}, fecha ="{fecha}", estado = "{estado}" WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def ver_factura(codigo):
    conexion = Conexion(db)
    conexion.consulta(f'SELECT * FROM Factura WHERE id={codigo}')
    datos = conexion.cursor.fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos  

def recuperar_codigo():
    conexion = Conexion(db)
    conexion.consulta('SELECT id FROM Factura ORDER DESC')
    datos = conexion.cursor.fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos