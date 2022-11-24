import db.conexion as conexion
from datetime import datetime

def insertar_factura(estado, id_factura):
    fecha = (datetime.now()).date()
    conexion.consulta(f'INSERT INTO Factura VALUES(NULL,"{fecha}","{estado}""')
    conexion.commit()
    conexion.cerrar()

def eliminar_factura(codigo):
    conexion.consulta(f'DELETE FROM Factura WHERE id={codigo}')
    conexion.commit()
    conexion.cerrar()

def editar_factura(id_persona, estado, codigo):
    fecha = fecha = (datetime.now()).date()
    conexion.consulta(f'UPDATE Factura SET id_persona = {id_persona}, fecha ="{fecha}", estado = "{estado}" WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def ver_factura(codigo):
    conexion.consulta(f'SELECT * FROM Factura WHERE id={codigo}')
    datos = conexion.cursor.fetchone()
    conexion.commit()
    conexion.cerrar()
    return datos