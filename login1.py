import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('600x300')
        self.title('Login')
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.resizable(0,0)
        self['bg']= '#9ACD32'

        # configuración del grid
        self.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)
        #self.columnconfigure(1, weight=2)
        # Creamos los componentes
        self._crear_componentes()

    # Definir el método crear_componentes
    def _crear_componentes(self):

        reg_boton = ttk.Button(self, text='Registrarse',command=self._login)
        reg_boton.grid(row=0, column=3,sticky=tk.W, padx=15, pady=15)
        #reg_boton["fg"]="blue"

        lbl1 =ttk.Label(self,text="Bienvenido a Super", font="Arial 25")
        lbl1.grid(row=1, column=1,columnspan=2,padx=25, pady=5)
        # usuario
        usuario_etiqueta = ttk.Label(self, text='Dni:')
        usuario_etiqueta.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

        # password
        #password_etiqueta = ttk.Label(self, text='Contraseña:')
        #password_etiqueta.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)
        #self.password_entrada = ttk.Entry(self, show='*')
        #self.password_entrada.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text='Ingresar', command=self._login)
        login_boton.grid(row=4, column=2, padx=20, pady=15)

        omit_boton = ttk.Button(self, text='Omitir',command=self._login)
        omit_boton.grid(row=5, column=0)

    def _login(self):
        messagebox.showinfo('Datos Login',
            f'usuario: {self.usuario_entrada.get()}, Contraseña: {self.password_entrada.get()}')

# Ejecutar la ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()