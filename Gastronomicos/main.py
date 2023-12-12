import pandas as pd
import numpy as np
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
            cocina = ['Todas']+df['cocina'].unique().tolist()
            # Configuramos valores iniciales de los desplegables
            categoria_entry['values']=categoria
            categoria_entry.set('Todas')

            cocina_entry['values']=cocina
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
    

# ----------------------------------------------
# ------------------ CRUD ----------------------
# ----------------------------------------------

def crear():
    global df


def filtrar_cocina(event):
    categoria_seleccionada = categoria_entry.get()
    
    if categoria_seleccionada == 'Todas':
        # Si se elige 'Todas', mostrar todas las cocinas
        cocina_entry['values'] = ['Todas'] + df['cocina'].unique().tolist()
        cocina_entry.set('Todas')  # Reiniciar la selección
    else:
        # Filtrar las cocinas según la categoría seleccionada
        cocinas_filtradas = ['Todas'] + df[df['categoria'] == categoria_seleccionada]['cocina'].unique().tolist()
        cocina_entry['values'] = cocinas_filtradas
        cocina_entry.set('Todas')  # Reiniciar la selección

def mostrar_resultados():
    global df
    # Crear una ventana de resultados
    ventana_resultados = Toplevel(root)
    ventana_resultados.title('Resultados de búsqueda')

    # Configurar columnas a mostrar
    columnas_mostrar = ['nombre', 'categoria', 'cocina',
                        'telefono', 'direccion_completa','barrio']

    # Crear un treeview para mostrar los resultados
    tree = ttk.Treeview(ventana_resultados,columns=columnas_mostrar,show='headings')

    # Configurar encabezados de columna
    for col in columnas_mostrar:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Ajusta el ancho según sea necesario

    # Paginación
    registros_x_pag = 10
    pagina_actual = 0

    def cargar_registros():
        inicio = pagina_actual * registros_x_pag
        fin = inicio + registros_x_pag

        # Limpiar registros anteriores
        for item in tree.get_children():
            tree.delete(item)
        
        # Inserta datos en el treeview
        for _,row in df.iloc[inicio:fin].iterrows():
            valores_fila = [row[col] for col in columnas_mostrar]
            tree.insert("","end",values=tuple(valores_fila))
    
    def pagina_anterior():
        nonlocal pagina_actual
        if pagina_actual>0:
            pagina_actual -= 1
            cargar_registros()
    
    def pagina_siguiente():
        nonlocal pagina_actual
        total_paginas = -(-len(df)//registros_x_pag)
        if pagina_actual < total_paginas - 1:
            pagina_actual += 1
            cargar_registros()
            
    # Cargargar registros
    cargar_registros()

    tree.pack(expand=YES, fill=BOTH)
    # Botones de paginación
    btn_anterior = Button(ventana_resultados, text='Anterior', command=pagina_anterior)
    btn_anterior.pack(side='left')

    btn_siguiente = Button(ventana_resultados, text='Siguiente', command=pagina_siguiente)
    btn_siguiente.pack(side='right')

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
categoria_entry.bind('<<ComboboxSelected>>',filtrar_cocina)

cocina_label = Label(frame_campos,text='Cocina:')
cocina_label.grid(row=0,column=2,padx=10,pady=10)
cocina=['Todas']
cocina_entry = ttk.Combobox(frame_campos,values=cocina)
cocina_entry.set("Todas")
cocina_entry.grid(row=0,column=3,ipady=5,padx=10)


# BOTONES
btn_mostrar_resultados = Button(frame_campos, text='Mostrar Resultados', command=mostrar_resultados)
btn_mostrar_resultados.grid(row=0, column=5, padx=10)


root.mainloop()