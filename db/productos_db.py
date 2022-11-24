import db.conexion as conexion

def insertar_producto(nombre, detalle, stock, precio):
    conexion.consulta(f'INSERT INTO Productos VALUES(NULL,"{nombre}","{detalle}",{stock},{precio})')
    conexion.commit()
    conexion.cerrar()

def eliminar_producto(codigo):
    conexion.consulta(f'DELETE FROM Productos WHERE id={codigo}')
    conexion.commit()
    conexion.cerrar()

def editar_producto(nombre, detalle, stock, precio,codigo):
    conexion.consulta(f'UPDATE Productos SET nombre ="{nombre}", detalle = "{detalle}", stock = {stock}, precio = {precio} WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def ver_producto(codigo):
    conexion.consulta(f'SELECT * FROM Productos WHERE id={codigo}')
    datos = conexion.cursor().fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos