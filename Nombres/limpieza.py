import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox, ttk, filedialog
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
manualmente, despues trataremos de hacer con tkinter para tener una mejor visualización.
'''
'''
**********************************************************************************
******************************* FUNCIONALIDADES **********************************
**********************************************************************************
'''
# BUSCAMOS EL CSV DESEADO
def csv_connect():
    # abrir cuadro para buscar archivo
    ruta_archivo = filedialog.askopenfilename(title='Seleccione archivo SCV',filetypes=[("Archivo CSV","*.csv")])
    if ruta_archivo:
        # mostramos el Dataframe desde el archivo CSV.
        df = pd.read_csv(ruta_archivo)
        print("Dataframe cargado:")
        print(df)

def salir():
    resp = messagebox.askquestion('ADVERTANCIA','¿Desea salir de la aplicación?')
    if resp == 'yes':
        root.destroy() 

def limpiar():
    pass

def crear():
    pass

def buscar():
    pass

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
csvmenu.add_command(label='Mostrar listado de nombres',command='')
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

boton_buscar = Button(framebotones,text='Buscar',command=buscar)
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