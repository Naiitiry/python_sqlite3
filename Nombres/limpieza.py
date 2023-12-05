import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog, simpledialog, scrolledtext
'''
# LEEMOS EL CSV
df = pd.read_csv('C:/Users/Tangalanga/Desktop/Practicas de Python/python_sqlite3/Nombres/nombres_permitidos.csv',sep=';')

# CONTAR CUANTOS REGISTROS TIENEN INFORMACIÓN EN ORIGEN Y SIGNIFICADO

# tomamos los datos de significado
df_significado = df['SIGNIFICADO'].value_counts()

# contamos la cantidades de cada columna
df_conteo_ss = df_significado.get('S/S',0)
df_conteo_or = df_significado.sum() - df_conteo_ss
df_count = len(df)

# print(f'Hay en SIGNIFICADO: {df_conteo_ss} y en ORIGEN: {df_conteo_or}, con un total de {df_count}')
'''

'''
Uno de los problemas principales es que ORIGEN y SIGNIFICADO están incompletos, vincular con otra bbdd, csv o pdf es complicado ya 
que no hay nada en internet (o por lo menos no encontré sobre ello). Por eso se hará con inputs para ser ingresado los datos
manualmente, despues trataremos de hacer con tkinter una interfaz para tener una mejor visualización.
'''
'''
**********************************************************************************
******************************* FUNCIONALIDADES **********************************
**********************************************************************************
'''
# BUSCAMOS EL CSV DESEADO
def csv_connect():
    global df
    global ruta_archivo
    # abrir cuadro para buscar archivo
    ruta_archivo = filedialog.askopenfilename(title='Seleccione archivo SCV',filetypes=[("Archivo CSV","*.csv")])
    if ruta_archivo:
        # mostramos el Dataframe desde el archivo CSV.
        df = pd.read_csv(ruta_archivo,sep=';')
        messagebox.showinfo('ÉXITO','CSV cargado correctamente')

def salir():
    resp = messagebox.askquestion('ADVERTENCIA','¿Desea salir de la aplicación?')
    if resp == 'yes':
        root.destroy() 

def limpiar():
    nombre.set("")
    sexo.set("")
    origen.set("")
    significado.set("")
    #deshabilitamos el nombre para que no sufra modificaciones (por ahora)
    nombre_input.config(state='normal')

'''
Para poder hacer un listado con todos los nombres, junto a todos sus demás campos,
creamos una función, que contenga una clase para abrir una ventana con toda la info
que buscamos.
'''
def listar():
    class Tabla():
        def __init__(self,root2,registro_x_pag=10):
            self.registro_x_pag=registro_x_pag
            self.pagina_actual=0
            self.frameppal = frameppal
            self.nombre_col = ['NOMBRE','SEXO','ORIGEN','SIGNIFICADO']
            # CREAMOS LAS COLUMNAS PARA LA NUEVA VENTANA
            for i in range(cant_cols):
                self.e=Entry(frameppal)
                self.e.config(bg='black',fg='white')
                self.e.grid(row=0,column=i)
                self.e.insert(END,self.nombre_col[i])
            
            # ------- PAGINACIÓN -------
                        
            # BOTONES DE PAGINACIÓN
            self.frame_botones = Frame(root2)
            self.frame_botones.pack(fill='both')

            boton_anterior = Button(self.frame_botones,text='Anterior',command=self.pagina_anterior)
            boton_anterior.pack(side='left')

            boton_siguiente = Button(self.frame_botones,text='Siguiente',command=self.pagina_siguiente)
            boton_siguiente.pack(side='right')

            # CARGAMOS REGISTROS INICIALES
            self.cargar_registros()

        def cargar_registros(self):
            inicio = self.pagina_actual * self.registro_x_pag
            fin = inicio + self.registro_x_pag

            self.limpiar_registros()

            # CREAMOS LOS REGISTROS DE LA NUEVA VENTANA
            for fila in range(cant_filas):
                if inicio <= fila < fin:
                    for col in range(cant_cols):
                        if fila==0:
                            self.e=Entry(frameppal)
                            self.e.grid(row=fila,column=col)
                            self.e.insert(END,self.nombre_col[col])
                            self.e.config(state='readonly')
                        else:
                            self.e=Entry(frameppal)
                            self.e.grid(row=fila-inicio+1,column=col)
                            self.e.insert(END,resultado[fila,col])
                            self.e.config(state='readonly')

        # DECLARAMOS LAS FUNCIONES DE LOS BOTONES
        def pagina_anterior(self):
            if self.pagina_actual>0:
                self.pagina_actual -= 1
                self.limpiar_registros()
                self.cargar_registros()
                
        def pagina_siguiente(self):
            #redondeamos hacía arriba
            total_paginas = -(-cant_filas//self.registro_x_pag)
            if self.pagina_actual < total_paginas -1:
                self.pagina_actual += 1
                self.limpiar_registros()
                self.cargar_registros()
        
        def limpiar_registros(self):
            for widget in self.frameppal.winfo_children():
                widget.destroy()

    # obtenemos los datos para el listado
    resultado = df.to_numpy()
    cant_filas, cant_cols = resultado.shape

    root2=Tk()
    root2.title('Listado de nombres')
    frameppal = Frame(root2)
    frameppal.pack(fill='both')
    framecerrar = Frame(root2)
    framecerrar.config(bg=fondo_letra)
    framecerrar.pack(fill='both')
    # creamos el botón de cerrar con la función destroy
    boton_cerrar = Button(framecerrar,text='CERRAR',command=root2.destroy)
    boton_cerrar.config(bg=color_boton,fg='white',pady=10,padx=0)
    boton_cerrar.pack(fill='both')

    tabla = Tabla(root2,registro_x_pag=10)

    root2.mainloop()

# ----------------------------------------------
# ------------------ CRUD ----------------------
# ----------------------------------------------

def crear():
    global df  # Asegúrate de declarar df como global

    # Obtener datos del usuario de los entrys
    nuevo_nombre = nombre.get().upper()
    nuevo_sexo = sexo.get()
    nuevo_origen = origen.get()
    nuevo_significado = significado.get()

    # Verificar que los datos no estén vacíos
    if nuevo_nombre and nuevo_sexo and nuevo_origen and nuevo_significado:
        # Crear una nueva fila con los datos ingresados
        nueva_fila = pd.DataFrame([[nuevo_nombre, nuevo_sexo, nuevo_origen, nuevo_significado]],
                                    columns=['NOMBRE', 'SEXO', 'ORIGEN', 'SIGNIFICADO'])

        # Agregar la nueva fila al DataFrame existente
        df = pd.concat([df, nueva_fila], ignore_index=True)

        # Guardar el DataFrame actualizado en el archivo CSV
        df.to_csv(ruta_archivo, sep=';', index=False)

        # Mensaje informativo
        messagebox.showinfo('Éxito', 'Nuevo nombre agregado correctamente.')

        # Limpiar los campos después de la creación
        limpiar()
    else:
        messagebox.showwarning('Campos Vacíos', 'Todos los campos son obligatorios. Por favor, complete la información.')


resultados_busqueda=None
def buscar_nombre():
    global resultados_busqueda
    buscando_nombre = simpledialog.askstring('Buscar por nombre','Ingrese el nombre a buscar:')
    if buscando_nombre is not None and buscando_nombre in df['NOMBRE'].values:
        resultados_busqueda = df[df['NOMBRE']==buscando_nombre]
        mostrar_resultados()
    else:
        messagebox.showinfo('SIN RESULTADOS','No se encontraron resultados para la búsuqeda.')

def mostrar_resultados():
    root_resultado = Tk()
    root_resultado.title('Resultados de búsqueda')
    texto_resultados = Listbox(root_resultado,selectmode=SINGLE)
    texto_resultados.pack(expand=True,fill='both')

    #Agregamos resultados a la lista
    for _,row in resultados_busqueda.iterrows():
        texto_resultados.insert(END, f"{row['NOMBRE']}, {row['SEXO']}, {row['ORIGEN']}, {row['SIGNIFICADO']}")

    def on_select(event):
        #Obtener índice seleccionado
        index=texto_resultados.curselection()[0]
        #Obtener el resultado correspondiente
        resultado_seleccionado = resultados_busqueda.iloc[index]
        #Actualizar campos en la pantalla principal
        nombre.set(resultado_seleccionado['NOMBRE'])
        sexo.set(resultado_seleccionado['SEXO'])
        origen.set(resultado_seleccionado['ORIGEN'])
        significado.set(resultado_seleccionado['SIGNIFICADO'])
    
    # Configurar la función de llamada cuando se selecciona un resultado
    texto_resultados.bind("<<ListboxSelect>>",on_select)

    root_resultado.mainloop()

def actualizar():
    pass

def eliminar():
    pass

'''
**********************************************************************************
******************************* INTERFAZ GRÁFICA *********************************
**********************************************************************************
'''
# Colores framecampos:
fondo = 'gray9'
fondo_letra = 'MediumPurple3'
# Colores framebotones
fondo_framebotonoes = 'gray15'
color_boton = 'MediumPurple3'
letra_boton = fondo_framebotonoes

# ----------------------------------

root = Tk()
root.title('Nombres permitidos en Argentina')

#--------------------------------------------
#----------------BARRA MENÚ------------------
#--------------------------------------------

barramenu = Menu(root)
root.config(menu=barramenu)

# MENU CSV Y COMANDOS
csvmenu = Menu(barramenu,tearoff=0) # Saca las líneas punteadas
csvmenu.add_command(label='Buscar CSV',command=csv_connect)
csvmenu.add_command(label='Mostrar listado de nombres',command=listar)
csvmenu.add_command(label='Salir',command=salir)

# MENU LIMPIAR Y COMANDOS
limpiarmenu = Menu(barramenu,tearoff=0)
limpiarmenu.add_command(label='Limpiar casillas',command=limpiar)

# CASCADAS
barramenu.add_cascade(label='CSV',menu=csvmenu)
barramenu.add_cascade(label='Limpieza',menu=limpiarmenu)

#-----------------------------------------------------------------
#---------------------------FRAMECAMPOS---------------------------
#-----------------------------------------------------------------

# UBICACIÓN ENTRYS Y LABELS
framecampos = Frame(root)
framecampos.config(bg=fondo)
framecampos.pack(fill='both')

#-----------------------------------------------------------------
#---------------------------ENTRYS--------------------------------
#-----------------------------------------------------------------
'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''

nombre = StringVar()
sexo = StringVar()
origen = StringVar()
significado = StringVar()

def config_input(mi_input,fila):
    espaciado = {'column':1,'padx':10,'pady':10,'ipadx':50}
    mi_input.grid(row=fila,**espaciado)

nombre_input=Entry(framecampos,textvariable=nombre)
config_input(nombre_input,0)

sexo_input=Entry(framecampos,textvariable=sexo)
config_input(sexo_input,1)

origen_input=Entry(framecampos,textvariable=origen)
config_input(origen_input,2)

significado_input=Entry(framecampos,textvariable=significado)
config_input(significado_input,3)

# ------------------ LABELS ------------------
'''
"STICKY"
    n
  nw ne
w       e
  sw se
    s
'''
def config_label(mi_label,fila):
    espaciado_label={'column':0,'sticky':'e','padx':10,'pady':10}
    colores={'bg':fondo,'fg':fondo_letra}
    mi_label.grid(row=fila,**espaciado_label)
    mi_label.config(**colores)

nombre_label = Label(framecampos,text='Nombre:')
config_label(nombre_label,0)

sexo_label = Label(framecampos,text='Sexo:')
config_label(sexo_label,1)

origen_label = Label(framecampos,text='Origen:')
config_label(origen_label,2)

significado_label = Label(framecampos,text='Significado:')
config_label(significado_label,3)

#----------------------------------------------------------------------
#---------------------------FRAMEBOTONES-------------------------------
#----------------------------------------------------------------------

framebotones = Frame(root)
framebotones.config(bg=fondo_framebotonoes)
framebotones.pack(fill='both')

def config_buttons(mi_button,columna):
    espaciado_buttons={'row':0,'padx':5,'pady':5,'ipadx':12}
    mi_button.config(bg=color_boton,fg=letra_boton)
    mi_button.grid(column=columna,**espaciado_buttons)

boton_crear = Button(framebotones,text='Crear',command=crear)
config_buttons(boton_crear,0)

boton_buscar = Button(framebotones,text='Buscar',command=buscar_nombre)
config_buttons(boton_buscar,1)

boton_actualizar = Button(framebotones,text='Actualizar',command=actualizar)
config_buttons(boton_actualizar,2)

boton_eliminar = Button(framebotones,text='Eliminar',command=eliminar)
config_buttons(boton_eliminar,3)

#--------------------------------------------------------------------
#---------------------------FRAME COPY-------------------------------
#--------------------------------------------------------------------

framecopy = Frame(root)
framecopy.config(bg='black')
framecopy.pack(fill='both')

copylabel = Label(framecopy,text='Todos los derechos y zurdos bien puestos.')
copylabel.config(bg='black',fg='white')
copylabel.grid(row=0,column=0,padx=10,pady=10)

root.mainloop()