import pandas as pd
from tkinter import *
from tkinter import messagebox, filedialog, ttk

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
            # Actualizamos las opciones del desplegable
            categoria = ['Todas']+df['categoria'].unique().tolist()
            cocina = ['Todas']+df['cocina'].unique().tolist
            categoria_entry['values']=categoria
            categoria_entry.set('Todas')
            cocina_entry['values']=categoria
            cocina_entry.set('Todas')
        else:
            messagebox.showerror('ERROR','El archivo cargado es incorrecto.')
    except Exception as e:
        messagebox.showerror('ERROR',f'Ocurrió un error: {str(e)}')


def salir():
    x = messagebox.askquestion('AVISO','¿Desea salir de la aplicación?')
    if x=='yes':
        root.destroy()

def limpiar():
    id.set("")
    long.set("")
    lat.set("")
    nombre.set("")
    categoria.set("")
    cocina.set("")
    ambientacion.set("")
    telefono.set("")
    mail.set("")
    horario.set("")
    calle_nombre.set("")
    calle_altura.set("")
    calle_cruce.set("")
    barrio.set("")
    comuna.set("")
    codigo_postal_arg.set("")
    

def listar():
    pass

# ----------------------------------------------
# ------------------ CRUD ----------------------
# ----------------------------------------------

def crear():
    global df


def buscar_categoria():
    global ruta_archivo
    categoria_seleccionada = categoria_entry.get()
    cocina_seleccionada = cocina_entry.get()

    # Filtramos DataFrame
    df_filtrado = ruta_archivo
    if categoria_seleccionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['categoria']==categoria_seleccionada]
    if cocina_seleccionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['cocina'] == cocina_seleccionada]

    # Actualizar la lista de resultados
    texto_resultado.config(state='normal')
    texto_resultado.delete("1.0",END)
    texto_resultado.insert(END,df_filtrado.to_string(index=False))
    texto_resultado.config(state='disabled')


def buscar_cocina():
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
fondo = '#BD9240'
color_letra_fondo = '#FFFFFF'
# COLORES FRAMEBOTONES
fondo_framebotones='#39CDF9'
color_boton = '#091A7A'
color_letra_boton = '#FFFFFF'

# ------------------------------------------------------

root = Tk()
root.title('Ofertas Gastronómicas')

#--------------------------------------------
#----------------BARRA MENÚ------------------
#--------------------------------------------

barramenu = Menu(root)
root.config(menu=barramenu)

# MENU CSV Y COMANDOS
csv_menu = Menu(barramenu,tearoff=0) #tearoff sacamos las líneas puntuadas
csv_menu.add_command(label='Abrir CSV',command=csv_connect)
csv_menu.add_command(label='Mostrar listado de restaurant/bar',command=listar)

# MENU PARA LIMPIAR Y COMANDOS
limpiar_menu = Menu(barramenu,tearoff=0)
limpiar_menu.add_command(label='Limpiar casillas',command=limpiar)

# CASCADAS
barramenu.add_cascade(label='CSV',menu=csv_menu)
barramenu.add_cascade(label='Limpieza',menu=limpiar_menu)

#-----------------------------------------------------------------
#---------------------------FRAMECAMPOS---------------------------
#-----------------------------------------------------------------

# UBICACIÓN DE ENTRYS Y LABELS

frame_campos = Frame(root)
frame_campos.config(bg=fondo)
frame_campos.pack(fill='both')

#-----------------------------------------------------------------
#---------------------------ENTRYS--------------------------------
#-----------------------------------------------------------------

'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''
long=DoubleVar()
lat=DoubleVar()
id=IntVar()
nombre=StringVar()
categoria=StringVar()
cocina=StringVar()
ambientacion=StringVar()
telefono=IntVar()
mail=StringVar()
horario=StringVar()
calle_nombre = StringVar()
calle_altura=IntVar()
calle_cruce=StringVar()
barrio = StringVar()
comuna=IntVar()
codigo_postal=IntVar()
codigo_postal_arg = StringVar()

# ENTRYS Y LABELS

categoria_label = Label(frame_campos,text='Categoria:')
categoria_label.grid(row=0,column=0,padx=10,pady=10)
categoria=['Todas']
categoria_entry = ttk.Combobox(frame_campos,values=categoria)
categoria_entry.set("Todas")
categoria_entry.grid(row=0,column=1,ipady=5,padx=10)

cocina_label = Label(frame_campos,text='Cocina:')
cocina_label.grid(row=0,column=2,padx=10,pady=10)
cocina=['Todas']
cocina_entry = ttk.Combobox(frame_campos,values=cocina)
cocina_entry.set("Todas")
cocina_entry.grid(row=0,column=3,ipady=5,padx=10)



root.mainloop()