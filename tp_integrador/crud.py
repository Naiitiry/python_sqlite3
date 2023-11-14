#********************************************************************
# RECORDAR CONECTAR LA BBDD, ANTES DE BUSCAR O CARGAR, SINO DA ERROR
#********************************************************************
from tkinter import *
from tkinter import messagebox, ttk
import sqlite3 as sq3

'''
*****************************
*********BARRA MENÚ**********
*****************************
'''


'''
*****************************
*******PARTE FUNCIONAL*******
*****************************
'''
def conectar():
    global con
    global cur
    con=sq3.connect('netflix_oscar.db')
    cur = con.cursor()
    messagebox.showinfo('Status','¡Conectado a la BBDD!.')

def salir():
    resp = messagebox.askquestion('ADVERTENCIA','¿Desea desconectarse de la BBDD?.')
    if resp=='yes':
        messagebox.showinfo('AVISO','Ha sido desconectado de la BBDD.')
        con.close()
        root.destroy()

# ********** CREAR ********** 
def crear():
    pass

# ********** LEER ********** 
def leer():
    pass

# ********** ACTUALIZAR ********** 
def actualizar():
    pass

# ********** BORRAR  **********
def borrar():
    pass

def lista_campo():
    pass
'''
*****************************
******INTERFAZ GRÁFICA*******
*****************************
'''
#colores framecampos
color_fondo='#b0802e'
color_entry = '#fef9e0'
color_letra = '#374f1d'
#colores framebotones
fondo_framebotones = color_letra
color_boton = color_entry
letra_boton = color_letra

root=Tk()
root.title('Premios OSCAR')

#----------------------------------------------------------------
#---------------------------BARRA MENÚ---------------------------
#----------------------------------------------------------------
barramenu = Menu(root) # MENU
root.config(menu=barramenu)

# MENU BBDD
bbddmenu=Menu(barramenu,tearoff=0)
bbddmenu.add_command(label='conectar a la bbdd')
bbddmenu.add_command(label='Salir')

# CASCADAS
barramenu.add_cascade(label='BBDD',menu=bbddmenu)
barramenu.add_cascade(label='Limpiar')
barramenu.add_cascade(label='Acerca de ...')

#-----------------------------------------------------------------
#---------------------------FRAMECAMPOS---------------------------
#-----------------------------------------------------------------

framecampo = Frame(root)
framecampo.config(bg='')
framecampo.pack(fill='both')

#-----------------------------------------------------------------
#---------------------------ENTRYS--------------------------------
#-----------------------------------------------------------------
'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''

type = StringVar() # LISTA DESPLEGABLE
title_content = StringVar() # INPUT
director = StringVar() # LISTA DESPLEGABLE
country = StringVar() # LISTA DESPLEGABLE
release_year = IntVar() # SLIDER
rating = StringVar() # LISTA DESPLEGABLE
duration = StringVar() # LISTA DESPLEGABLE
listed_in = StringVar() # LISTA DESPLEGABLE

# -------- LOS CONTENEDORES DE CADA LISTA --------
list_type = list_campo('type')
list_title_content = list_campo('title_content')
list_director = list_campo('director')
list_country = list_campo('country')
list_release_year = list_campo('release_year')
list_rating = list_campo('rating')
list_duration = list_campo('duration')
list_listed_in = list_campo('listed_in')

# Definimos posicionamiento de entrys con una FUNCIÓN:
def config_input(mi_input,fila):
    espaciado={'column':1,'padx':10,'pady':10,'ipadx':50}
    mi_input.grid(row=fila,**espaciado)

# ENTRYS
type_option = ttk.Combobox(framecampo,textvariable=type,state='active')


root.mainloop()