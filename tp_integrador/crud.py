#********************************************************************
# RECORDAR CONECTAR LA BBDD, ANTES DE BUSCAR O CARGAR, SINO DA ERROR
#********************************************************************
from tkinter import *
from tkinter import messagebox
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
    global cursor
    con=sq3.connect()
    messagebox.showinfo('Status','Conectado a la BBDD.')
def salir():
    resp = messagebox.askquestion('ADVERTENCIA','¿Desea desconectarse de la BBDD?.')
    if resp=='yes':
        con.close()
        root.destroy()
'''
*****************************
******INTERFAZ GRÁFICA*******
*****************************
'''

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


root.mainloop()