# Importaciones
import sqlite3
from tkinter import *
from tkinter import messagebox

class RegistroApp:
    '''
    Generar el constructor con:
    el root, los label y entrys, los datos a ingresar,
    así como los botones para crear, actualizar, leer y borrar.
    '''
    def __init__(self,root):
        self.root = root
        self.root.title("Formulario de Registro")
        self.root.geometry("300x400")
        self.conn = sqlite3.connect("registro.db")
        self.create_table()

        self.nombre_label = Label(root,text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = Entry(root)
        self.nombre_entry.pack()

        self.apellido_label = Label(root,text="Apellido:")
        self.apellido_label.pack()
        self.apellido_entry = Entry(root)
        self.apellido_entry.pack()

        self.dni_label = Label(root,text="DNI:")
        self.dni_label.pack()
        self.dni_entry = Entry(root)
        self.dni_entry.pack()

        self.email_label = Label(root,text="Email: ")
        self.email_label.pack()
        self.email_entry = Entry(root)
        self.email_entry.pack()

        self.contraseña_label = Label(root,text="Contraseña: ")
        self.contraseña_label.pack()
        self.contraseña_entry = Entry(root,show="*")
        self.contraseña_entry.pack()

        self.registrar_buton = Button(root,text="Registrar",command=self.registrar)
        self.registrar_buton.pack()

        self.actualizar_button = Button(root, text="Actualizar datos",command=self.actualizar_datos)
        self.actualizar_button.pack()

        self.buscar_button = Button(root,text="Buscar por DNI",command=self.buscar_por_dni)
        self.buscar_button.pack()

        self.limpiar_button = Button(root,text="Limpiar campos",command=self.limpiar_campos)
        self.limpiar_button.pack()

        self.eliminar_button = Button(root,text="Eliminar registro",command=self.eliminar_registro)
        self.eliminar_button.pack()

        self.cerrar_button = Button(root,text="Cerrar",command=self.confirmar_salida)
        self.cerrar_button.pack()

    
    # Generamos la BD:

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            dni INTEGER,
            email TEXT,
            contraseña TEXT
            )
        ''')
        self.conn.commit()
    
    # Ésta función captura los Entrys y asigna a la bd con sus respectivos valores.
    #   Una vez creados, limpia los mismos para consultar o cargar un nuevo usuario.

    def registrar(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        dni = self.dni_entry.get()
        email = self.email_entry.get()
        contraseña = self.contraseña_entry.get()

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre,apellido,dni,email,contraseña) VALUES (?,?,?,?,?)",(nombre,apellido,dni,email,contraseña))
        self.conn.commit()

        self.nombre_entry.delete(0,END)
        self.apellido_entry.delete(0,END)
        self.dni_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.contraseña_entry.delete(0,END)

    # Realizamos la función búsqueda por DNI.

    def buscar_por_dni(self):
        dni = self.dni_entry.get()
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nombre, apellido, dni, email, contraseña FROM usuarios WHERE dni=?",(dni,))
        result=cursor.fetchone()
        if result:
            self.id_a_modificar = result[0]
            self.nombre_entry.delete(0, END)
            self.apellido_entry.delete(0,END)
            self.dni_entry.delete(0,END)
            self.email_entry.delete(0, END)
            self.contraseña_entry.delete(0, END)
            self.nombre_entry.insert(0, result[1])
            self.apellido_entry.insert(0,result[2])
            self.dni_entry.insert(0, result[3])
            self.email_entry.insert(0, result[4])
            self.contraseña_entry.insert(0, result[5])
        else:
            messagebox.showerror("Error","El usuario no se encuentra en la base de datos.")

    # Generamos la función para la actualización de los datos.

    def actualizar_datos(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        dni = self.dni_entry.get()
        email = self.email_entry.get()
        contraseña = self.contraseña_entry.get()

        cursor = self.conn.cursor()
        cursor.execute("UPDATE usuarios SET nombre = ?,apellido=?,dni=?,email=?,contraseña=? WHERE id =?",(nombre,apellido,dni,email,contraseña,self.id_a_modificar))
        self.conn.commit()
        messagebox.showinfo("Actualizado", "Los datos se han actualizado correctamente.")

    # Ponemos un botón para la limpieza de los campos.
    def limpiar_campos(self):
        self.nombre_entry.delete(0,END)
        self.apellido_entry.delete(0,END)
        self.dni_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.contraseña_entry.delete(0,END)

    # Eliminación de registro con advertencia

    def eliminar_registro(self):
        if hasattr(self, 'id_a_modificar') and self.id_a_modificar is not None:
            cursor = self.conn.cursor()
            cursor.execute("SELECT nombre, apellido FROM usuarios WHERE id = ?", (self.id_a_modificar,))
            result = cursor.fetchone()
            if result:
                nombre, apellido = result
                confirmar = messagebox.askyesno("Advertencia", f"¿Estás seguro de eliminar a {nombre} {apellido}?")
                if confirmar:
                    cursor.execute("DELETE FROM usuarios WHERE id = ?", (self.id_a_modificar,))
                    self.conn.commit()
                    messagebox.showinfo("Eliminado", "El registro ha sido eliminado.")
                    self.limpiar_campos()
            else:
                messagebox.showerror("Error", "No se ha encontrado el registro.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado un registro para eliminar.")

    # Creamos una función para cerrar el programa

    def confirmar_salida(self):
        confirmar = messagebox.askyesno("Cerrar aplicación","¿Estás seguro/a que desea cerrar la aplicación?.")
        if confirmar:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = RegistroApp(root)
    root.mainloop()