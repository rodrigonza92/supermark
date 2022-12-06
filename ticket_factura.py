from io import open
import os
from datetime import datetime
import platform
import time
from clases.detalle import Detalle
from clases.factura import Factura
from clases.persona import Persona
from clases.producto import Producto

class Ticket:
    def __init__(self):
        self.__dni = 0
        self.__idPersona = 0
        self.__idFactura = 0

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    
    @property
    def idPersona(self):
        return self.__idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self.__idPersona = idPersona

    @property
    def idFactura(self):
        return self.__idFactura

    @idFactura.setter
    def idFactura(self, idFactura):
        self.__idFactura = idFactura

    def ver_facturas(self, dni):
        per = Persona()
        id = per.ver_persona(dni)
        datos = Factura().ver_todas(id[0])
        print('\n-------------------------------------')
        print('              FACTURAS                 ')
        print('---------------------------------------')
        print(' ID  |   FECHA   |   ESTADO   |  TOTAL ')
        print('---------------------------------------')
        for i in datos:
            print(str(i[0]).center(5, ' ')+'|'+str(i[2]).ljust(11,' ')+'|'+str(i[3]).ljust(12, ' ')+'|'+str(i[4]).ljust(8,' ')+'\n')
            print('---------------------------------------')

    def imprimir_ticket(self):
        per = Persona()
        fac = Factura()
        if self.__idPersona == 0:
            dato_per = [0,'No Registrado','',0,'No Cliente']
        else:
            dato_per = per.ver_persona(self.__dni)
        det = Detalle()
        dato_det = det.ver_detalle(self.__idFactura)
        subtotal = 0
        pro = Producto()

        fichero = open('ticket.txt', 'w')

        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                                               {os.linesep}')
        fichero.write(f'                    SUPERMARK                  {os.linesep}')
        fichero.write(f'                                            {os.linesep}')
        fichero.write(f'                           {(datetime.now()).date()}   {(datetime.now()).hour}:{(datetime.now()).minute}{os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                     CLIENTE                   {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'Cliente: {dato_per[2]} {dato_per[1]}         DNI: {dato_per[3]}{os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                     DETALLE                   {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f' PRODUCTO |    DETALLE    | CANTIDAD | SUBTOTAL {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        for i in dato_det:
            producto = pro.ver_producto(i[2])
            subtotal += i[5]
            fichero.write(producto[1].ljust(10,' ')+'|'+producto[2].ljust(15, ' ')+'|'+str(i[3]).ljust(10,' ')+'|'+str(i[5]).ljust(10, ' ')+'\n')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                      TOTAL                    {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'                     Subtotal: $ {subtotal}      {os.linesep}')
        
        # Estoy aplicando un descuento del 15%
        descuento = subtotal * fac.descuento(self.__idPersona)
        total = subtotal - descuento
        
        fichero.write(f'                    Descuento: $ {descuento}     {os.linesep}')
        fichero.write(f'       Su total a pagar es de: $ {total}         {os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')
        fichero.write(f'-------------¡GRACIAS POR SU COMPRA!-----------{os.linesep}')
        fichero.write(f'-----------------------------------------------{os.linesep}')

        fichero.close()
    
    def cargar_ticket(self, carrito):
        det = Detalle()
        fac = Factura()
        pro = Producto()
        carrito = carrito

        for i in carrito:
            det.crear_detalle(self.__idFactura, i[0], i[1])
            pro.decrementar_stock(i[0], i[1])
        estado = 'pagado'
        total = fac.sum_total(self.__idFactura)
        fac.editar_estado_total(estado, total, self.__idFactura)


    def confirmar_compra(self, carrito):
        fac = Factura()
        print('\n¿Confirmar compra?')
        op = input('Si o No: ') 
        if op == 'Si' or op == 'si' or op == "SI": #Cambio de estado a pagado y actualizacion de total
            fac.crear_factura(self.__dni)
            #Retornar ID de Factura
            self.__idFactura = fac.retornar_idFactura(self.__idPersona)
            self.cargar_ticket(carrito)
            self.imprimir_ticket()
            print('Ticket Generado con Exito!')
    
    def confirmacion(self, carrito):
        print('\n¿Que desea hacer?')
        print('(1) Agregar Producto al carrito')
        print('(2) Quitar Producto del carrito')
        print('(3) Confirmar Compra')
        print('(4) Cancelar Compra')

        op1 = input('Opcion: ')
        if op1 == '1':
            self.agregar_producto(carrito)
            self.vista_previa(carrito)
            self.confirmacion(carrito)

        elif op1 == '2':
            self.quitar_producto(carrito)
            self.vista_previa(carrito)
            self.confirmacion(carrito)
        
        elif op1 == '3':
            self.confirmar_compra(carrito)
            print('Compra Finalizada')
        
        elif op1 == '4':
            print('Compra cancelada')
            pass
    
    def datos_compra(self, dni=0):
        per = Persona()
        fac = Factura()
        self.__dni = dni #Se setea en 0 en caso de ser invitado
        #Retornar ID de Persona
        if self.__dni == 0:
            self.__idPersona = 0
        else:
            datos = per.ver_persona(self.__dni)
            self.__idPersona = datos[0] 
        
        carrito = []
        
        self.agregar_producto(carrito)
        print('\nVerifique su Detalle de Compra')
        self.vista_previa(carrito)
        self.confirmacion(carrito)
        self.clear()

    def agregar_producto(self, list=[]):
        carrito = list
        op = 'si'      
        while op.lower() == 'si':
            self.ver_productos()
            idProducto = int(input('Ingrese codigo de producto: '))
            cantidad = int(input('¿Cuantos articulos desea llevar? '))
            carrito.append((idProducto, cantidad)) #Aqui tengo que hacer la condicion de no comprar mas de 30 productos
            print('Producto Agregado al Carrito')
            print('\n¿Desea ingresar otro Producto?: ')
            op = input('Si o No: ')
        return carrito
    
    def quitar_producto(self,list=[]):
        carrito = list
        orden = int(input('Ingrese el nuemero de orden del producto que desea eliminar: '))
        carrito.pop(orden)
        print('Producto Eliminado\n')

    def ver_productos(self):
        pro = Producto()
        datos_pro = pro.ver_todo()
        print('\n------------------------------------------')
        print('          PRODUCTOS DISPONIBLES             ')
        print('--------------------------------------------')
        print(' CODIGO | PRODUCTO |    DETALLE    | PRECIO ')
        print('--------------------------------------------')
        for i in datos_pro:
            print(str(i[0]).center(8, ' ')+'|'+str(i[1]).center(10, ' ')+'|'+str(i[2]).center(15,' ')+'|'+str(i[4]).center(10, ' ')+'\n')
        print('--------------------------------------------')
        #Falta la opcion de edicion de productos
        #Falta la actualizacion de Stock luego de la compra
        #Falta Aplicar los descuentos para los clientes

    def vista_previa(self, list):
        carrito = list
        pro = Producto()
        orden = -1
        subtotal = 0
        print('\n--------------------------------------------------------')
        print('                      DETALLE DE COMPRA                   ')
        print('--------------------------------------------------------')
        print(' ORDEN | PRODUCTO |    DETALLE    | CANTIDAD | SUBTOTAL ')
        print('--------------------------------------------------------')
        for i in carrito:
            orden += 1
            producto = pro.ver_producto(i[0])
            subtotal = (i[1] * producto[4])
            print(str(orden).center(7, ' ')+'|'+str(producto[1]).center(10, ' ')+'|'+producto[2].center(15,' ')+'|'+str(i[1]).center(10, ' ')+'|'+str(subtotal).rjust(10, ' ')+'\n')

    def ver_usuarios_activos(self):
        fac = Factura()
        datos = fac.ver_todas_activas()

        print('\n--------------------------------------------')
        print('          FACTURAS DE CLIENTES ACTIVOS        ')
        print('----------------------------------------------')
        print(' ID  | ID PERSONA |   FECHA   |   ESTADO   |  TOTAL ')
        print('----------------------------------------------')
        for i in datos:
            print(str(i[0]).center(5, ' ')+'|'+str(i[1]).center(12, ' ')+'|'+str(i[2]).ljust(11,' ')+'|'+str(i[3]).ljust(12, ' ')+'|'+str(i[4]).ljust(8,' ')+'\n')
            print('----------------------------------------------')


    def clear(self):
        time.sleep(2)
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

#t = Ticket()
#t.confirmar_compra()
#t.imprimir_ticket(36811278, 23)
#t.ver_ticket(36811278)
#t.datos_compra()