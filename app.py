from db.conexion import Conexion
import clases.persona as persona
import clases.producto as producto

conexion = Conexion('supermark.db')
conexion.crear_db()

# Prueba carga de datos de persona aleatorio
listaPersonas = [("Edgar", "Hurtado", 32453897, "cliente"),
("Francisco", "Rosado", 23423533, "cliente"),
("Inés", "Carrillo",20323533,"administrador"),
("Luis", "Huertas",39873897,"administrador"),
("Gloria", "Carrera",32445787,"cliente"),
("Margarita", "Duran",29873533,"administrador"),
("Ramón", "Rivera",23487633,"administrador"),
("Francisco", "Cruz",36473897,"cliente"),
("Valentín", "Aguado",29823533,"cliente"),
("Melisa", "Cueto",36753897,"administrador"),
("Catalina", "Aranda",23424233,"administrador"),
("Ismael", "Peralta",23423763,"administrador"),
("Elisabet", "Carrera",23423233,"cliente"),
("Priscila", "Valdéz",32453889,"administrador"),
("Jose Antonio", "Martinez",24423533,"cliente"),
("Cristina", "Saavedra",32253897,"cliente"),
("Alicia", "Godoy",32453887,"administrador"),
("Leonel", "Goicoechea",23423553,"administrador"),
("Valentina", "Villalobos",23433533,"cliente"),
("Jose", "Alvarado",32453837,"administrador")]

for i in listaPersonas:
    per = persona.Persona(i[0],i[1],i[2],i[3])
    per.crear_persona()

# Prueba de carga de datos de Productos
listaProductos = [("Harina", "000", 30, 150),
("Harina", "0000", 20, 160),
("Arroz", "Perseguido", 50, 130),
("Arroz", "10 Minutos", 45, 130),
("Fideos", "Luchetti", 70, 145.5),
("Fideos", "Marolio", 55, 130),
("Leche", "Sancor", 25, 250)]

for j in listaProductos:
    pro = producto.Producto(j[0], j[1], j[2], j[3])
    pro.crear_producto()

# Prueba funcion eliminar producto
codigo = 2
pro.eliminar_producto(codigo)

# Prueba funcion eliminar persona
dni = 20323533
per.eliminar_persona(dni)
#print('Producto y Persona eliminada')

# Prueba VER PRODUCTO ---- No se porque tira error NoneType
codigo = 5
#dato = pro.ver_producto(codigo)
#print(dato)

pro.ver_todo()