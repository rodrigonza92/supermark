import os, platform, time
#import carga_datos as carga_datos
from db.conexion import Conexion
from clases import persona, producto, detalle, factura
from db import detalle_db, persona_db, factura_db, productos_db
import ticket_factura


conexion = Conexion('supermark.db')
conexion.crear_db()
#carga_datos

class Menu():
    def __init__(self) -> None:
        self.__dni = 0
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    print('Bienvenido a SUPERMARK\n')
    
    def login(self):
        print('--LOGIN--')
        print('Seleccione una opcion: ')
        print('(1) Soy Administrador')
        print('(2) Soy Cliente')
        print('(3) No soy Cliente')
        
        op = input('Opcion: ')
        if op == '1':
            dni = int(input('\nIngrese DNI: ')) #Como ingreso un espacio en blanco en DNI?
            self.__dni = dni
            password = input('Ingrese contraseña: ') #Por default es 'admin'

            datos = persona_db.ver_persona(dni)
            if datos[4] == "administrador" and password == 'admin':                
                print('Logueo Exitoso\n')
                #print("Panel Administrador")
                self.clear()
                self.panel_admin()
            else:
                print('Datos invalidos\n')
                self.clear()
                self.login()
        
        elif op == '2':
            dni = int(input('Ingrese DNI: '))
            self.__dni = dni
            datos = persona_db.ver_persona(dni)

            if datos[4] == "cliente":
                verificacion = f'{datos[1]} {datos[2]}'
                print(f'¿Usted es {verificacion}?')
                op = input('Si o No: ')
                if op.lower() == 'si':
                    print('Logueo Exitoso!')
                    self.clear()
                    print(f'Bienvenido {verificacion}\n')
                    self.panel_cli()
                else:
                    print('Datos invalidos\n')
                    self.clear()
                    self.login()
            else:
                print('\n"El DNI no corresponde a un cliente"')
                self.clear()
                self.login()

        elif op == '3':
            self.clear()
            self.panel_invitado()   
        
        else:
            self.clear()
            self.login()
        
    def panel_admin(self):
        print('--PANEL ADMINISTRADOR--')
        print('Seleccione una opcion: ')
        print('(1) Registrar Cliente')
        print('(2) Ingresar Producto')
        print('(3) Modificar datos de un Producto')
        print('(4) Actualizar STOCK de producto')
        print('(5) Ver Usuarios que realizaron una compra')
        print('(6) Salir')
        op = input('Opcion: ')

        if op == '1':
            self.clear()
            print('--REGISTRAR CLIENTE--')
            nombre = input('Ingrese nombre: ')
            apellido = input('Ingrese apellido: ')
            dni = int(input('Ingrese DNI: '))
            condicion = input('¿Es "administrador" o "cliente"?: ')
            persona.Persona().crear_persona(nombre, apellido, dni, condicion)
            print('Nuevo Cliente Registrado!')
            self.clear()
            self.panel_admin()
        
        elif op == '2':
            self.clear()
            print('--INGRESAR PRODUCTO--')
            nombre = input('Ingrese nombre de producto: ')
            detalle = input('Ingrese detalle del producto: ')
            stock = int(input('Ingrese cantidad de Stock: '))
            precio = float(input('Ingrese precio unitario: '))
            producto.Producto().crear_producto(nombre, detalle, stock, precio)
            print('Nuevo Producto Agregado con Exito!')
            self.clear()
            self.panel_admin()
        
        elif op == '3':
            self.clear()
            print('--MODIFICAR PRODUCTO--')
            idProducto = int(input('Ingrese ID del Producto que desea modificar: '))
            nombre = input('Ingrese nombre de producto: ')
            detalle = input('Ingrese detalle del producto: ')
            stock = int(input('Ingrese cantidad de Stock: '))
            precio = float(input('Ingrese precio unitario: '))
            producto.Producto().editar_producto(nombre, detalle, stock, precio,idProducto)
            print('Producto Modificado con Exito!')
            self.clear()
            self.panel_admin()

        elif op == '4':
            self.clear()
            print('--ACTUALIZAR STOCK PRODUCTO--')
            print('(1) Incrementar stock de un producto')
            print('(2) Decrementar stock de un producto')
            print('(3) Salir')
            op1 = input()
            if op1 == '1':
                idProducto = int(input('Ingrese ID del Producto: '))
                cantidad = int(input('Ingrese cuanto Stock desea ingresar: '))
                producto.Producto().incrementar_stock(idProducto, cantidad)
                print('\nActualizacion de Stock Exitosa')
                self.clear()
                self.panel_admin()
            elif op1 == '2':
                idProducto = int(input('Ingrese ID del Producto: '))
                cantidad = int(input('Ingrese cuanto Stock desea sacar: '))
                producto.Producto().decrementar_stock(idProducto, cantidad)
                print('\nActualizacion de Stock Exitosa')
                self.clear()
                self.panel_admin()
            elif op1 == '3':
                self.clear()
                self.panel_admin()
            else:
                print('\nOpcion Inválida')
                self.clear()
                self.panel_admin()

        elif op == '5':
            print('--Usuarios que Compraron--')
            ticket_factura.Ticket().ver_usuarios_activos()
            print('\n(1) Volver al Menu Anterior')
            print('(0) Salir')

            op1 = input('Opcion: ')
            if op1 == '1':
                self.clear()
                self.panel_admin()
            elif op1 == '2':
                self.clear()
                self.login()

        elif op == '6':
            print('\nGracias por usar Nuestro Servicio!')
            self.clear()
            self.login()
        
        else:
            print('\nOpcion Inválida')
            self.clear()
            self.panel_admin()
    
    def panel_cli(self):
        print('--PANEL CLIENTE--')
        print('Seleccione una opcion: ')
        print('(1) Hacer una Compra')
        print('(2) Ver Productos')
        print('(3) Ver todas mis facturas')
        print('(4) Salir')
        op = input('Opcion: ')

        if op == '1':
            self.clear()
            print('--CARRITO DE COMPRA--')
            ticket_factura.Ticket().datos_compra(self.__dni)
            self.clear()
            self.panel_cli()
        
        elif op == '2':
            self.clear()
            print('--VER PRODUCTOS--')
            ticket_factura.Ticket().ver_productos()
            print('\n(1) Volver al Menu Anterior')
            print('(0) Salir')

            op1 = input('Opcion: ')
            if op1 == '1':
                self.clear()
                self.panel_cli()
            elif op1 == '2':
                self.clear()
                self.login()
            else:
                print('La opcion ingresada es inválida')
                self.clear()
                self.panel_invitado()

        elif op == '3':
            self.clear()
            ticket_factura.Ticket().ver_facturas(self.__dni)
            print('\n(1) Volver al Menu Anterior')
            print('(0) Salir')

            op1 = input('Opcion: ')
            if op1 == '1':
                self.clear()
                self.panel_cli()
            elif op1 == '2':
                self.clear()
                self.login()

        elif op == '4':
            print('\nGracias por usar Nuestro Servicio!')
            self.clear()
            self.login()

        else:
            print('\nOpcion Inválida')
            self.clear()
            self.panel_cli()

    def panel_invitado(self):
        print('--PANEL INVITADO--')
        print('Seleccione una opcion: ')
        print('(1) Hacer una Compra')
        print('(2) Ver productos disponibles')
        print('(3) Salir')
        op = input('Opcion: ')
        
        if op == '1':
            self.clear()
            print('--CARRITO DE COMPRA--')
            ticket_factura.Ticket().datos_compra()
            self.clear()
            self.panel_invitado()

        elif op == '2':
            self.clear()
            print('--VER PRODUCTOS--')
            ticket_factura.Ticket().ver_productos()
            print('\n(1) Volver al Menu Anterior')
            print('(0) Salir')

            op1 = input('Opcion: ')
            if op1 == '1':
                self.clear()
                self.panel_invitado()
            elif op1 == '2':
                self.clear()
                self.login()
            else:
                print('La opcion ingresada es inválida')
                self.clear()
                self.panel_invitado()

        elif op == '3':
            print('Gracias por usar Nuestro Servicio!')
            self.clear()
            self.login()

        else:
            print('Opcion Inválida')
            self.clear()
            self.panel_invitado()
    
    def clear(self):
        time.sleep(1)
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


Menu().login()