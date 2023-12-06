import pandas as pd
from tkinter import *
from tkinter import messagebox, filedialog

'''
**********************************************************************************
******************************* FUNCIONALIDADES **********************************
**********************************************************************************
'''

def csv_connect():
    global df
    global ruta_archivo
    # abrimos cuadro para buscar el archivo csv
    ruta_archivo = filedialog.askopenfilename(title='Selecciones el archivo CSV',filetypes=[("Archivo CSV","*.csv")])
    try:
        if ruta_archivo:
            df=pd.read_csv(ruta_archivo,sep=",")
            messagebox.showinfo('ÉXITO','csv cargado exitosamente.')
        else:
            messagebox.showerror('ERROR','El archivo cargado es incorrecto.')
    except Exception as e:
        messagebox.showerror('ERROR',f'Ocurrió un error: {str(e)}')


def salir():
    x = messagebox.askquestion('AVISO','¿Desea salir de la aplicación?')
    if x=='yes':
        root.destroy()

def limpiar():
    pass

# ----------------------------------------------
# ------------------ CRUD ----------------------
# ----------------------------------------------

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

# COLORES FRAMECAMPOS
fondo = '#309F1A'
color_letra_fondo = '#FFFFFF'
# COLORES FRAMEBOTONES
fondo_framebotones='#39CDF9'
color_boton = '#091A7A'
color_letra_boton = '#FFFFFF'

# ------------------------------------------------------

root = Tk()
root.title('Ofertas Gastronómicas')

long=DoubleVar()
lat=DoubleVar()
id=IntVar()


root.mainloop()