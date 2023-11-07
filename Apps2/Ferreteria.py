import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
        self.labelyentry=Frame(root)
        self.labelyentry.config(bg='sienna1')
        self.labelyentry.grid(row=0,column=0, columnspan=4)
        self.buttoncopy = Frame(root)
        self.buttoncopy.config(bg='black')
        self.buttoncopy.grid(row=1, column=0, columnspan=4)
        self.creditos=Frame(root)
        self.creditos.config(bg="khaki1")
        self.creditos.grid(row=2,column=0,columnspan=4, sticky="nsew")
        self.conn = sqlite3.connect("inventario.db")
        self.crear_tabla() #función para crear la tabla, en caso de que no exista

# -------------------------------------------------------------------------------
# ------------ CREACIÓN DE LABELS Y ENTRYS Y UBICACIÓN DE LAS MISMAS ------------
# -------------------------------------------------------------------------------

        self.nombre_del_producto_label = Label(self.labelyentry,text="Nombre del producto: ",bg='sienna1')
        self.nombre_del_producto_label.grid(row=0,column=0,padx=10,pady=10)
        self.nombre_del_producto_entry = Entry(self.labelyentry,width=50)
        self.nombre_del_producto_entry.grid(row=0,column=1,columnspan=3,ipady=5,padx=10)

        self.descripcion_label = Label(self.labelyentry,text="Descripción: ",bg='sienna1')
        self.descripcion_label.grid(row=1,column=0,padx=10,pady=10)
        self.descripcion_entry = Entry(self.labelyentry,width=50)
        self.descripcion_entry.grid(row=1,column=1,columnspan=3,ipady=5,padx=10)

        self.proveedor_label = Label(self.labelyentry,text="Proveedor: ",bg='sienna1')
        self.proveedor_label.grid(row=2,column=0,padx=10,pady=10)
        self.proveedor_entry = Entry(self.labelyentry,width=50)
        self.proveedor_entry.grid(row=2,column=1,columnspan=3,ipady=5,padx=10)

        self.precio_de_compra_label = Label(self.labelyentry,text="Precio de compra: ",bg='sienna1')
        self.precio_de_compra_label.grid(row=3,column=0,padx=10,pady=10)
        self.precio_de_compra_entry = Entry(self.labelyentry,width=50)
        self.precio_de_compra_entry.grid(row=3,column=1,columnspan=3,ipady=5,padx=10)

        self.fecha_de_compra_label = Label(self.labelyentry,text="Fecha de compra: ",bg='sienna1')
        self.fecha_de_compra_label.grid(row=4,column=0,padx=10,pady=10)
        self.fecha_de_compra_entry = Entry(self.labelyentry,width=50)
        self.fecha_de_compra_entry.grid(row=4,column=1,columnspan=3,ipady=5,padx=10)

        self.precio_de_venta_label = Label(self.labelyentry,text="Precio de venta: ",bg='sienna1')
        self.precio_de_venta_label.grid(row=5,column=0,padx=10,pady=10)
        self.precio_de_venta_entry = Entry(self.labelyentry,width=50)
        self.precio_de_venta_entry.grid(row=5,column=1,columnspan=3,ipady=5,padx=10)

        self.stock_label = Label(self.labelyentry,text="Stock: ",bg='sienna1')
        self.stock_label.grid(row=6,column=0,padx=10,pady=10)
        self.stock_entry = Entry(self.labelyentry,width=50)
        self.stock_entry.grid(row=6,column=1,columnspan=3,ipady=5,padx=10)

        self.ubicacion_asignada_label = Label(self.labelyentry,text="Ubicacion asignada: ",bg='sienna1')
        self.ubicacion_asignada_label.grid(row=7,column=0,padx=10,pady=10)
        self.ubicacion_asignada_entry = Entry(self.labelyentry,width=50)
        self.ubicacion_asignada_entry.grid(row=7,column=1,columnspan=3,ipady=5,padx=10)

        self.punto_de_reorden_label = Label(self.labelyentry,text="Punto de reorden: ",bg='sienna1')
        self.punto_de_reorden_label.grid(row=8,column=0,padx=10,pady=10)
        self.punto_de_reorden_entry = Entry(self.labelyentry,width=50)
        self.punto_de_reorden_entry.grid(row=8,column=1,columnspan=3,ipady=5,padx=10)

        self.numero_de_serie_label = Label(self.labelyentry,text="Número de serie: ",bg='sienna1')
        self.numero_de_serie_label.grid(row=9,column=0,padx=10,pady=10)
        self.numero_de_serie_entry = Entry(self.labelyentry,width=50)
        self.numero_de_serie_entry.grid(row=9,column=1,columnspan=3,ipady=5,padx=10)

        self.categoria_label = Label(self.labelyentry,text="Categoria: ",bg='sienna1')
        self.categoria_label.grid(row=10,column=0,padx=10,pady=10)
        self.categoria_entry = Entry(self.labelyentry,width=50)
        self.categoria_entry.grid(row=10,column=1,columnspan=3,ipady=5,padx=10)

        self.notas_adicionales_label = Label(self.labelyentry,text="Notas adicionales: ",bg='sienna1')
        self.notas_adicionales_label.grid(row=11,column=0,padx=10,pady=10)
        self.notas_adicionales_entry = Entry(self.labelyentry,width=50)
        self.notas_adicionales_entry.grid(row=11,column=1,columnspan=3,ipady=5,padx=10)

        self.registrar_button = Button(self.buttoncopy,text="Registrar",command=self.registrar,bg='black',fg='sienna1')
        self.registrar_button.grid(row=0,column=0,padx=5,pady=10,ipadx=12)

        self.actualizar_button = Button(self.buttoncopy,text="Actualizar",command=self.actualizar,bg='black',fg='sienna1')
        self.actualizar_button.grid(row=0,column=1,padx=25,pady=10,ipadx=12)

        self.buscar_button = Button(self.buttoncopy,text="Buscar",command=self.buscar,bg='black',fg='sienna1')
        self.buscar_button.grid(row=0,column=2,padx=5,pady=10,ipadx=12)

        self.buscar_categoria_button = Button(self.buttoncopy, text="Buscar por Categoría", command=self.buscar_por_categoria,bg='black',fg='sienna1')
        self.buscar_categoria_button.grid(row=0,column=3,padx=5,pady=10,ipadx=12)

        self.limpiar_button = Button(self.buttoncopy,text="Limpiar campos",command=self.limpiar_campos,bg='black',fg='sienna1')
        self.limpiar_button.grid(row=1,column=0,padx=5,pady=10,ipadx=12)

        self.eliminar_button = Button(self.buttoncopy,text="Eliminar registro",command=self.eliminar_registro,bg='black',fg='sienna1')
        self.eliminar_button.grid(row=1,column=1,padx=5,pady=10,ipadx=12)

        self.cerrar_button = Button(self.buttoncopy,text="Cerrar",command=self.cerrar_programa,bg='black',fg='sienna1')
        self.cerrar_button.grid(row=1,column=2,padx=5,pady=10,ipadx=12)

        self.creador = Label(self.creditos,text="Creador: Román Danchuk",bg='khaki1')
        self.creador.grid(row=0,column=0,columnspan=3,pady=10,ipadx=12)

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

    # ------------ FUNCION REGISTRAR ------------

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

    # ------------ FUNCION ACTUALIZAR ------------

    def actualizar(self):
        pass

    # ------------ FUNCION BUSCAR ------------

    def buscar(self):
        nombre_del_producto = self.nombre_del_producto_entry.get()
        cursor = self.conn.cursor()
        cursor.execute("SELECT id,nombre_del_producto,descripcion,proveedor,precio_de_compra,fecha_de_compra,precio_de_venta,stock,ubicacion_asignada,punto_de_reorden,numero_de_serie,categoria,notas_adicionales FROM inventario WHERE nombre_del_producto=?",(nombre_del_producto,))
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

    def buscar_por_categoria(self):
        categoria = self.categoria_entry.get()
        cursor = self.conn.cursor()
        cursor.execute("SELECT nombre_del_producto FROM inventario WHERE categoria=?",(categoria,))
        productos = cursor.fetchall()
        if productos:
            # CREAR NUEVA VENTANA
            lista_window = Toplevel(self.root)
            lista_window.title("Productos de la categoría")
            # WIDGET PARA MOSTRAR LOS PRODUCTOS
            lista = ttk.Treeview(lista_window,columns=("Producto"))
            lista.heading("#1",text="Producto")
            lista.pack()
            # Agrega los productos a la lista
            for producto in productos:
                lista.insert("","end",values=(producto[0]))
            
            # FUNCIÓN PARA MANEJAR SELECCIÓN DE UN PRODUCTO
            def mostrar_producto(event):
                item=lista.selection()[0]
                nombre_producto = lista.item(item,"values")[0]
                cursor=self.conn.cursor()
                cursor.execute("SELECT * FROM inventario WHERE nombre_del_producto=?",(nombre_producto,))
                producto=cursor.fetchone()
                if producto:
                    # 1.- Limpia los campos existentes en la ventana principal:
                    self.limpiar_campos()
                    # 2.- Rellena los campos con los detalles del producto seleccionado:
                    self.nombre_del_producto_entry.insert(0, producto[1])
                    self.descripcion_entry.insert(0, producto[2])
                    self.proveedor_entry.insert(0, producto[3])
                    self.precio_de_compra_entry.insert(0, producto[4])
                    self.fecha_de_compra_entry.insert(0, producto[5])
                    self.precio_de_venta_entry.insert(0, producto[6])
                    self.stock_entry.insert(0, producto[7])
                    self.ubicacion_asignada_entry.insert(0, producto[8])
                    self.punto_de_reorden_entry.insert(0, producto[9])
                    self.numero_de_serie_entry.insert(0, producto[10])
                    self.categoria_entry.insert(0, producto[11])
                    self.notas_adicionales_entry.insert(0, producto[12])
                else:
                    messagebox.showerror("ERROR","No se encontró información detallada para este producto.")
            lista.bind("<Double-1>",mostrar_producto)
        else:
            messagebox.showerror("ERROR","No se encontraron productos en esta categoría.")

    # ------------ FUNCION LIMPIAR ------------

    def limpiar_campos(self):
        # se puede poner .set(""), son parecidos.
        self.id_a_modificar = None
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

    # ------------ FUNCION ELIMINAR ------------

    def eliminar_registro(self):
        if hasattr(self,'id_a_modificar') and self.id_a_modificar is not None:
            cursor = self.conn.cursor()
            cursor.execute('SELECT nombre_del_producto FROM inventario WHERE nombre_del_producto=?',(self.nombre_del_producto_entry))
            resultado = cursor.fetchone()
            if resultado:
                nombre_del_producto = resultado
                confirmar = messagebox.askyesno("ADVERTENCIA",f'Está seguro de eliminar a {nombre_del_producto}?.')
                if confirmar:
                    cursor.execute("DELETE FROM inventario WHERE id=?",(self.id_a_modificar))
                    self.conn.commit()
                    messagebox.showinfo("ELIMINADO","El registro ha sido eliminado.")
                    self.limpiar_campos()
            else:
                messagebox.showerror("ERROR","No se ha encontrado ningún registro.")
        else:
            messagebox.showerror("ERROR","No se ha seleccionado ningún registro para eliminar.")

    # ------------ FUNCION CERRAR ------------

    def cerrar_programa(self):
        confirmar = messagebox.askyesno("Cerrar aplicación","¿Desea, realmente, cerrar la aplicación?.")
        if confirmar:
            self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    root.config(bg="sienna1")
    app=FerreAstro(root)
    root.mainloop()