class Persona:
    def __init__(self, id, nombre, apellido, dni, condicion):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__condicion = condicion
    
class Factura:
    def __init__(self, id, idPersona, fecha, estado, total):
        self.__id = id
        self.__idPersona = idPersona
        self.__fecha = fecha
        self.__estado = estado
        self.__total = total

class Detalle:
    def __init__(self, id, idFactura, idProducto, cantidad, precio, subtotal):
        self.__id = id
        self.__idFactura = idFactura
        self.__idProducto = idProducto
        self.__cantidad = cantidad
        self.__precio = precio
        self.__subtotal = subtotal

class Producto:
    def __init__(self):
        self._id = 0
        self.nombre = ''
        self.detalle = ''
        self.stock = 0
        self.precio = 0.0
    
    def codigo(self):
        return self._codigo
    
    def codigo(self, codigo):
        self._codigo = codigo
    
    def ingresar_datos(self):
        self.nombre = input("Ingresar nombre: ")
        self.detalle = input("Ingrese detalle: ")
        self.stock = int(input("Ingresar cantidad: "))
        self.precio = float(input("Ingresar precio: "))
  
    def definir_producto(self,tupla):
        self._codigo = tupla[0][0]
        self.nombre = tupla[0][1]
        self.detalle = tupla[0][2]
        self.stock = tupla[0][3]
        self.precio = tupla[0][4]
  
    def editar(self):
        print(f"Nombre: {self.nombre}")
        valor = input("Ingresar nombre: ")
        if valor != '':
            self.nombre = valor
        print(f"Detalle: {self.detalle}")
        detalle = input("Ingresar detalle: ")
        if valor != '':
            self.detalle = detalle
        print(f"Stock: {self.stock}")
        try:
            valor = int(input("Ingresar stock: "))
        except:
            valor = 0
        if valor != 0:
            self.stock = valor
        print(f"Precio: ${self.precio}")
        try:
            valor = float(input("Ingresar precio: "))
        except:
            valor = 0
        if valor != 0:
            self.precio = valor
  
    def __str__(self):
        return f"""
        Nombre = {self.nombre}
        Detalle = {self.detalle}
        Stock = {self.stock}
        Precio = {self.precio}
        """
