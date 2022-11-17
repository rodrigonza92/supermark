import json
from datetime import datetime

import pandas as pd

from conexion import Conexion_BD

conexion_producto = Conexion_BD('super.db')
try:
    conexion_producto.consulta('CREATE TABLE Persona(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, dni INTEGER, condicion TEXT)')
    conexion_producto.consulta('CREATE TABLE Productos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, detalle TEXT, stock INTEGER, precio FLOAT)')
    conexion_producto.consulta('CREATE TABLE Factura(id INTEGER PRIMARY KEY AUTOINCREMENT, fecha DATE , estado TEXT, total FLOAT)')
    conexion_producto.consulta('CREATE TABLE Detalles(id INTEGER PRIMARY KEY AUTOINCREMENT, id_factura INTEGER, id_producto INTEGER, cantidad INTEGER, precio FLOAT, subtotal FLOAT)')
    conexion_producto.commit()
except:
      print("las Tablas ya fueron creadas")