from db.conexion import Conexion

conexion = Conexion('supermark.db')
def insertar_persona(id, nombre, apellido, dni, condicion):
    conexion.consulta(f'INSERT INTO Persona VALUES({id},"{nombre}","{apellido}",{dni},"{condicion}")')
    conexion.commit()
    conexion.cerrar()

def eliminar_persona(dni):
    conexion.consulta(f'DELETE FROM Persona WHERE dni={dni}')
    conexion.commit()
    conexion.cerrar()

def editar_persona(nombre, apellido, dni, condicion, codigo):
    conexion.consulta(f'UPDATE Persona SET nombre = "{nombre}", apellido = "{apellido}", dni = {dni}, condicion = {condicion} WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def ver_persona(dni):
    conexion.consulta(f'SELECT * FROM Persona WHERE dni={dni}')
    datos = conexion.cursor.fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos