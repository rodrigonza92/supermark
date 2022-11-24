import db.conexion as conexion

def insertar_detalle(id_factura, id_producto, cantidad, precio):
    subtotal = cantidad * precio
    conexion.consulta(f'INSERT INTO Detalles VALUES(NULL, {id_factura}, {id_producto}, {cantidad}, {precio}, {subtotal})')
    conexion.commit()
    conexion.cerrar()

def eliminar_detalle(codigo):
    conexion.consulta(f'DELETE FROM Detalles WHERE id={codigo}')
    conexion.commit()
    conexion.cerrar()

def editar_detalle(id_factura, id_producto, cantidad, precio, codigo):
    subtotal = cantidad * precio
    conexion.consulta(f'UPDATE Detalles SET id_factura = {id_factura}, id_producto = {id_producto}, cantidad = {cantidad}, precio = {precio}, subtotal = {subtotal} WHERE id = {codigo}')
    conexion.commit()
    conexion.cerrar()

def ver_detalle(codigo):
    conexion.consulta(f'SELECT * FROM Detalles WHERE id={codigo}')
    datos = conexion.cursor.fetchall()
    conexion.commit()
    conexion.cerrar()
    return datos