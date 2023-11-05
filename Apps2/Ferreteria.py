import sqlite3
from tkinter import *
from tkinter import messagebox

class FerreAstro:
    '''
    Ferretería Astro:
    inventario con sqlite3 y Python
    CRUD
    '''
# ------------ CONSTRUCTOR ------------
    def __init__(self,root):
        self.root=root
        self.root.title("Ferretería Astro")
        self.root.geometry("500x500")
        self.conn = sqlite3.connect("inventario.db")
        self.crear_tabla() #función para crear la tabla, en caso de que no exista

# ------------ CREACIÓN DE LABELS Y ENTRYS Y UBICACIÓN DE LAS MISMAS ------------

        self.nombre_del_producto_label = Label(root,text="Nombre del producto: ")
        self.nombre_del_producto_label.pack()
        self.nombre_del_producto_entry = Entry(root)
        self.nombre_del_producto_entry.pack()

        self.descripcion_label = Label(root,text="Descripción: ")
        self.descripcion_label.pack()
        self.descripcion_entry = Entry(root)
        self.descripcion_entry.pack()

        self.proveedor_label = Label(root,text="Proveedor: ")
        self.proveedor_label.pack()
        self.proveedor_entry = Entry(root)
        self.proveedor_entry.pack()

        self.precio_de_compra_label = Label(root,text="Precio de compra: ")
        self.precio_de_compra_label.pack()
        self.precio_de_compra_entry = Entry(root)
        self.precio_de_compra_entry.pack()

        self.fecha_de_compra_label = Label(root,text="Fecha de compra: ")
        self.fecha_de_compra_label.pack()
        self.fecha_de_compra_entry = Entry(root)
        self.fecha_de_compra_entry.pack()

        self.precio_de_venta_label = Label(root,text="Precio de venta: ")
        self.precio_de_venta_label.pack()
        self.precio_de_venta_entry = Entry(root)
        self.precio_de_venta_entry.pack()

        self.stock_label = Label(root,text="Stock: ")
        self.stock_label.pack()
        self.stock_entry = Entry(root)
        self.stock_entry.pack()

        self.ubicacion_asignada_label = Label(root,text="Ubicacion asignada: ")
        self.ubicacion_asignada_label.pack()
        self.ubicacion_asignada_entry = Entry(root)
        self.ubicacion_asignada_entry.pack()

        self.punto_de_reorden_label = Label(root,text="Punto de reorden: ")
        self.punto_de_reorden_label.pack()
        self.punto_de_reorden_entry = Entry(root)
        self.punto_de_reorden_entry.pack()

        self.numero_de_serie_label = Label(root,text="Número de serie: ")
        self.numero_de_serie_label.pack()
        self.numero_de_serie_entry = Entry(root)
        self.numero_de_serie_entry.pack()

        self.categoria_label = Label(root,text="Categoria: ")
        self.categoria_label.pack()
        self.categoria_entry = Entry(root)
        self.categoria_entry.pack()

        self.notas_adicionales_label = Label(root,text="Notas adicionales: ")
        self.notas_adicionales_label.pack()
        self.notas_adicionales_entry = Entry(root)
        self.notas_adicionales_entry.pack()

        self.registrar_button = Button(root,text="Registrar",command=self.registrar)
        self.registrar_button.pack()

        self.actualizar_button = Button(root,text="Actualizar",command=self.actualizar)
        self.actualizar_button.pack()

        self.buscar_button = Button(root,text="Buscar",command=self.buscar)
        self.buscar_button.pack()

        self.limpiar_button = Button(root,text="Limpiar campos",command=self.limpiar_campos)
        self.limpiar_button.pack()

        self.eliminar_button = Button(root,text="Eliminar registro",command=self.eliminar_registro)
        self.eliminar_button.pack()

        self.cerrar_button = Button(root,text="Cerrar",command=self.cerrar_programa)
        self.cerrar_button.pack()

# ------------ Generamos la bbdd. ------------

    def crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_del_producto TEXT,
            descripcion TEXT,
            proveedor TEXT,
            precio_de_compra REAL NOT NULL,
            fecha_de_compra DATE,
            precio_de_venta REAL NOT NULL,
            stock INTEGER,
            ubicacion_asignada INTEGER,
            punto_de_reorden INTEGER,
            numero_de_serie TEXT,
            categoria TEXT,
            notas_adicionales TEXT
        )
        ''')
        self.conn.commit()

# ------------ FUNCIONES ------------

    def registrar(self):
        nombre_del_producto = self.nombre_del_producto_entry.get()
        descripcion = self.descripcion_entry.get()
        proveedor = self.proveedor_entry.get()
        precio_de_compra = self.precio_de_compra_entry.get()
        fecha_de_compra = self.fecha_de_compra_entry.get()
        precio_de_venta = self.precio_de_venta_entry.get()
        stock = self.stock_entry.get()
        ubicacion_asignada = self.ubicacion_asignada_entry.get()
        punto_de_reorden = self.punto_de_reorden_entry.get()
        numero_de_serie = self.numero_de_serie_entry.get()
        categoria = self.categoria_entry.get()
        notas_adicionales = self.notas_adicionales_entry.get()
        # ejecutamos las siguientes líneas para que se grabe en la bd
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO inventario (nombre_del_producto,descripcion,proveedor,precio_de_compra,fecha_de_compra,precio_de_venta,stock,ubicacion_asignada,punto_de_reorden,numero_de_serie,categoria,notas_adicionales) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (nombre_del_producto,descripcion,proveedor,precio_de_compra,fecha_de_compra,precio_de_venta,stock,ubicacion_asignada,punto_de_reorden,numero_de_serie,categoria,notas_adicionales))
        # efectua el guardado en la BD.
        self.conn.commit()
        # cada vez que guardamos se limpian los campos automaticamente
        self.nombre_del_producto_entry.delete(0,END)
        self.descripcion_entry.delete(0,END)
        self.proveedor_entry.delete(0,END)
        self.precio_de_compra_entry.delete(0,END)
        self.fecha_de_compra_entry.delete(0,END)
        self.precio_de_venta_entry.delete(0,END)
        self.stock_entry.delete(0,END)
        self.ubicacion_asignada_entry.delete(0,END)
        self.punto_de_reorden_entry.delete(0,END)
        self.numero_de_serie_entry.delete(0,END)
        self.categoria_entry.delete(0,END)
        self.notas_adicionales_entry.delete(0,END)


    def actualizar(self):
        pass

    def buscar(self):
        categoria = self.categoria_entry.get()
        cursor = self.conn.cursor()
        cursor.execute("SELECT id,nombre_del_producto,descripcion,proveedor,precio_de_compra,fecha_de_compra,precio_de_venta,stock,ubicacion_asignada,punto_de_reorden,numero_de_serie,categoria,notas_adicionales WHERE categoria=?",(categoria,))
        resultado = cursor.fetchone()
        if resultado:
            # limpiamos los ENTRYS
            self.id_a_modificar = resultado[0]
            self.nombre_del_producto_entry.delete(0, END)
            self.descripcion_entry.delete(0, END)
            self.proveedor_entry.delete(0, END)
            self.precio_de_compra_entry.delete(0, END)
            self.fecha_de_compra_entry.delete(0, END)
            self.precio_de_venta_entry.delete(0, END)
            self.stock_entry.delete(0, END)
            self.ubicacion_asignada_entry.delete(0, END)
            self.punto_de_reorden_entry.delete(0, END)
            self.numero_de_serie_entry.delete(0, END)
            self.categoria_entry.delete(0, END)
            self.notas_adicionales_entry.delete(0, END)

            # ahora mostramos lo que tenemos guardado

            self.nombre_del_producto_entry.insert(0,resultado[1])
            self.descripcion_entry.insert(0,resultado[2])
            self.proveedor_entry.insert(0,resultado[3])
            self.precio_de_compra_entry.insert(0,resultado[4])
            self.fecha_de_compra_entry.insert(0,resultado[5])
            self.precio_de_venta_entry.insert(0,resultado[6])
            self.stock_entry.insert(0,resultado[7])
            self.ubicacion_asignada_entry.insert(0,resultado[8])
            self.punto_de_reorden_entry.insert(0,resultado[9])
            self.numero_de_serie_entry.insert(0,resultado[10])
            self.categoria_entry.insert(0,resultado[11])
            self.notas_adicionales_entry.insert(0,resultado[12])
        else:
            messagebox.showerror("ERROR","El artículo no se encuentra en la base de datos.")

    def limpiar_campos(self):
        pass

    def eliminar_registro(self):
        pass

    def cerrar_programa(self):
        pass


if __name__ == "__main__":
    root=Tk()
    app=FerreAstro(root)
    root.mainloop()