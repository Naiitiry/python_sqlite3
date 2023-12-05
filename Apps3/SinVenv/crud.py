#********************************************************************
# RECORDAR CONECTAR LA BBDD, ANTES DE BUSCAR O CARGAR, SINO DA ERROR
#********************************************************************

from tkinter import *
from tkinter import messagebox
import sqlite3 as sq3
import matplotlib.pyplot as plt

'''
*****************************
*******PARTE FUNCIONAL*******
*****************************
'''
# ******* MENU *******
def conectar():
    global con
    global cur
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    messagebox.showinfo('Status','Conectado a la BBDD.')

def salir():
    resp = messagebox.askquestion('ADVERTENCIA','¿Desea desconectarse de la BBDD?')
    if resp=='yes':
        con.close()
        root.destroy()


# GRÁFICAS
# Por escuelas
def alumnos_en_escuelas():
  query = '''SELECT COUNT(alumnos.legajo) AS "total", escuelas.nombre FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id GROUP BY escuelas.nombre ORDER BY total DESC'''
  cur.execute(query)
  resultado=cur.fetchall()
  #print(resultado)
  
  escuelas=[]
  cantidad=[]
  for r in resultado:
    cantidad.append(r[0])
    escuelas.append(r[1])
  plt.bar(escuelas,cantidad)
  plt.xticks(rotation=90) #labels del eje x
  plt.show()

# Por alumnos
def alumnos_con_notas():
  query = '''SELECT COUNT(legajo) AS "total",nota FROM alumnos GROUP BY nota'''
  cur.execute(query)
  resultado=cur.fetchall()
  #print(resultado)
  
  nota=[]
  cantidad=[]
  for r in resultado:
    cantidad.append(r[0])
    nota.append(r[1])
  plt.bar(nota,cantidad)
  #plt.xticks(rotation=90) #labels del eje x
  plt.show()

def limpiar():
  legajo.set("")
  apellido.set("")
  nombre.set("")
  email.set("")
  calificacion.set("")
  escuela.set("")
  localidad.set("")
  provincia.set("")
  # se debe deshabilitar el legajo para que no se modifique.
  legajo_input.config(state='normal')

def mostrar_licencia():
  msg='''
  Licencia by the perrito salvaje.
  '''
  messagebox.showinfo('Licencia',msg)

def acerca_de():
  messagebox.showinfo("ACERCA DE...","Creado por RFD\npara CaC 4.0 - Big Data\nNoviembre 2023.")

def listar():
    class Tabla():
        def __init__(self,root2):
            nombre_cols = ['Legajo','Apellido','Nombre','Promedio','Escuela']
            # CREAMOS LAS COLUMNAS DE LA NUEVA VENTANA
            for i in range(cant_cols):
                self.e=Entry(frameppal)
                self.e.config(bg='black', fg='white')
                self.e.grid(row=0, column=i)
                self.e.insert(END,nombre_cols[i])
            # CREAMOS LOS REGISTROS DE LA NUEVA VENTANA
            for fila in range(cant_filas):
              for cols in range(cant_cols):
                self.e=Entry(frameppal)
                self.e.grid(row=fila+1,column=cols)
                self.e.insert(END,resultado[fila][cols])
                self.e.config(state='readonly') #para que nadie lo modifique, solo de lectura

    root2=Tk()
    root2.title('Listado de alumnos')
    frameppal = Frame(root2)
    frameppal.pack(fill='both')
    framecerrar = Frame(root2)
    framecerrar.config(bg=color_letra)
    framecerrar.pack(fill='both')

    boton_cerrar = Button(framecerrar, text="CERRAR",command=root2.destroy)
    #Ingresa destroy para cerrar y no crear una función
    boton_cerrar.config(bg=color_boton, fg='white', pady=10, padx=0)
    boton_cerrar.pack(fill='both')

    # obtener los datos para el listado
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    query1 = '''
            SELECT alumnos.legajo, alumnos.apellido, alumnos.nombre, alumnos.nota, escuelas.nombre FROM alumnos INNER JOIN escuelas 
            ON alumnos.id_escuela = escuelas._id LIMIT 30   
            '''
    cur.execute(query1)
    resultado = cur.fetchall()
    cant_filas = len(resultado) # la cantidad de registros para saber cuántas filas
    cant_cols = len(resultado[0])

    tabla = Tabla(frameppal)
    con.close()
    root2.mainloop()

# ******* CRUD *******
# CREAR
def crear():
  id_escuela=int(buscar_escuelas(True)[0])
  datos=id_escuela,legajo.get(),apellido.get(),nombre.get(),calificacion.get(),email.get()
  cur.execute('INSERT INTO alumnos (id_escuela,legajo,apellido,nombre,nota,email) VALUES (?,?,?,?,?,?)',datos)
  con.commit()
  messagebox.showinfo("STATUS","Registro agregado")
  limpiar()

# BUSCAR
def buscar_legajo():
  query2 = 'SELECT alumnos.legajo, alumnos.apellido, alumnos.nombre, alumnos.nota, alumnos.email, escuelas.nombre, escuelas.localidad,     escuelas.provincia FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id WHERE alumnos.legajo='
  cur.execute(query2 + legajo.get())
  resultado = cur.fetchall()
  if resultado == []:
    messagebox.showerror("ERROR","Ese n° de legajo no existe.")
    legajo.set("")
  else:
    for campo in resultado:
      legajo.set(campo[0])
      apellido.set(campo[1])
      nombre.set(campo[2])
      calificacion.set(campo[3])
      email.set(campo[4])
      escuela.set(campo[5])
      localidad.set(campo[6])
      provincia.set(campo[7])
      legajo_input.config(state='disabled') #desahabilitar para que no se modifique

# ACTUALIZAR
def actualizar():
  id_escuela=int(buscar_escuelas(True)[0])
  datos=id_escuela,apellido.get(),nombre.get(),calificacion.get(),email.get()
  cur.execute('UPDATE alumnos SET id_escuela=?,apellido=?,nombre=?,nota=?,email=? WHERE legajo='+legajo.get(),datos)
  con.commit()
  messagebox.showinfo("STATUS","Registro actualizado")
  limpiar()

# ELIMINAR
def borrar():
  resp=messagebox.askquestion("AVISO","¿Desea borrar el registro?")
  if resp=="yes":
    cur.execute('DELETE FROM alumnos WHERE legajo='+legajo.get())
    con.commit()
    messagebox.showinfo("STATUS","Registro eliminado.")
    limpiar()

# ******* OTRAS F(x) *******
def buscar_escuelas(actualiza):
  con=sq3.connect('mi_db.db')
  cur=con.cursor()
  if actualiza:
    cur.execute('SELECT _id, localidad,provincia FROM escuelas WHERE nombre=?',(escuela.get(),)) # se pone coma porque es una TUPLA, elemento fantasma
  else:
    #esta opción es la que llena la lista de escuelas en el desplegable.
    cur.execute('SELECT nombre FROM escuelas')
  resultado = cur.fetchall() #recibe una lista de tuplas de la bbdd.
  retorno=[] #(nombre,)
  for e in resultado:
    if actualiza:
      provincia.set(e[1])
      localidad.set(e[2])
    esc=e[0]
    retorno.append(esc)
  con.close()
  return retorno


'''
*****************************
******INTERFAZ GRÁFICA*******
*****************************
'''

# colores framecampos
color_fondo = 'plum'
color_letra = 'black'
# colores framebotones
fondo_framebotones = 'pink'
color_boton = 'black'
letra_boton = fondo_framebotones

# Root
root = Tk()
root.title('GUI - CRUD')

#----------------------------------------------------------------
#---------------------------BARRA MENÚ---------------------------
#----------------------------------------------------------------
barramenu = Menu(root) # MENÚ
root.config(menu=barramenu)

# MENU BBDD Y COMANDOS
bbddmenu=Menu(barramenu, tearoff=0) # saaca las líneas punteadas
bbddmenu.add_command(label='Conectar con la BBDD',command=conectar)
bbddmenu.add_command(label='Mostrar listado alumnos',command=listar)
bbddmenu.add_command(label='Salir',command=salir)

# MENU ESTADÍSTICAS
estadmenu = Menu(barramenu,tearoff=0)
estadmenu.add_command(label='Cantidad de alumnos por escuela',command=alumnos_en_escuelas)
estadmenu.add_command(label='Desempeño estudiantil',command=alumnos_con_notas)

# MENU LIMPIAR Y COMANDOS
limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label='Limpiar formulario',command=limpiar)

# MENU ACERCA DE... Y COMANDOS
ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia',command=mostrar_licencia)
ayudamenu.add_command(label='Acerca de...',command=acerca_de)

# CASCADAS
barramenu.add_cascade(label='BBDD',menu=bbddmenu)
barramenu.add_cascade(label='Gráficas',menu=estadmenu)
barramenu.add_cascade(label='Limpiar',menu=limpiarmenu)
barramenu.add_cascade(label='Acerca de...',menu=ayudamenu)

#-----------------------------------------------------------------
#---------------------------FRAMECAMPOS---------------------------
#-----------------------------------------------------------------

# donde van los entrys y labels
framecampos = Frame(root)
framecampos.config(bg=color_fondo)
framecampos.pack(fill='both') #para que ocupe toda la pantalla

#-----------------------------------------------------------------
#---------------------------ENTRYS--------------------------------
#-----------------------------------------------------------------
'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''

legajo=StringVar()
apellido=StringVar()
nombre=StringVar()
email=StringVar()
escuela=StringVar()
localidad=StringVar()
provincia=StringVar()
calificacion=DoubleVar()

#entrys y posicionamiento con función
def config_input(mi_input,fila):
  espaciado={'column':1,'padx':10,'pady':10,'ipadx':50}
  mi_input.grid(row=fila,**espaciado)


# entrys y posicionamiento a mano
legajo_input=Entry(framecampos,textvariable=legajo)
#legajo_input.grid(row=0,column=1,padx=10,pady=10,ipadx=50)
config_input(legajo_input,0)

apellido_input=Entry(framecampos,textvariable=apellido)
config_input(apellido_input,1)

nombre_input=Entry(framecampos,textvariable=nombre)
config_input(nombre_input,2)

email_input=Entry(framecampos,textvariable=email)
config_input(email_input,3)

#escuela_input=Entry(framecampos,textvariable=escuela)
#config_input(escuela_input,4)
lista=buscar_escuelas(False)
escuela.set('Seleccione')
escuela_option=OptionMenu(framecampos,escuela,*lista)
# se agrega "*" al principio sino salen todas las escuelas como 1 solo objeto y no como un desplegable normal.
escuela_option.grid(row=4,column=1,padx=10,pady=10,sticky='w',ipadx=50)


localidad_input=Entry(framecampos,textvariable=localidad)
config_input(localidad_input,5)

provincia_input=Entry(framecampos,textvariable=provincia)
config_input(provincia_input,6)

calificacion_input=Entry(framecampos,textvariable=calificacion)
config_input(calificacion_input,7)

#-----------------------------------------------------------------
#---------------------------LABELS--------------------------------
#-----------------------------------------------------------------
'''
"STICKY"
    n
  nw ne
w       e
  sw se
    s
'''
def config_label(mi_label,fila):
  espaciado_labels={'column':0,'sticky':'e','padx':10,'pady':10}
  colores = {'bg':color_fondo,'fg':color_letra}
  mi_label.grid(row=fila,**espaciado_labels)
  mi_label.config(**colores)

legajo_label = Label(framecampos,text='N° de legajo:')
config_label(legajo_label,0)

apellido_label = Label(framecampos,text='Apellido:')
config_label(apellido_label,1)

nombre_label = Label(framecampos,text='Nombre:')
config_label(nombre_label,2)

email_label = Label(framecampos,text='Email:')
config_label(email_label,3)

escuela_label = Label(framecampos,text='Escuela:')
config_label(escuela_label,4)

localidad_label = Label(framecampos,text='Localidad:')
config_label(localidad_label,5)

provincia_label = Label(framecampos,text='Provincia:')
config_label(provincia_label,6)

calificacion_label = Label(framecampos,text='Calificacion:')
config_label(calificacion_label,7)

#----------------------------------------------------------------------
#---------------------------FRAMEBOTONES-------------------------------
#----------------------------------------------------------------------

framebotones = Frame(root)
framebotones.config(bg=fondo_framebotones)
framebotones.pack(fill='both')

def config_buttons(mi_button,columna):
  espaciado_buttons={'row':0,'padx':5,'pady':5,'ipadx':12}
  mi_button.config(bg=color_boton,fg=letra_boton)
  mi_button.grid(column=columna,**espaciado_buttons)

boton_crear=Button(framebotones,text='Crear',command=crear)
config_buttons(boton_crear,0)

boton_buscar=Button(framebotones,text='Buscar',command=buscar_legajo)
config_buttons(boton_buscar,1)

boton_actualizar=Button(framebotones,text='Actualizar',command=actualizar)
config_buttons(boton_actualizar,2)

boton_eliminar=Button(framebotones,text='Eliminar',command=borrar)
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
