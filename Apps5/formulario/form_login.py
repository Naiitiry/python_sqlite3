from tkinter import *
from tkinter import messagebox,ttk
from tkinter.font import BOLD
import util.generic as utl
from formulario.form_master import MasterPanel

class App:

    def verificar(self):
        usu=self.usuario.get()
        passw=self.password.get()
        if(usu=='root' and passw=='1234'):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror('AVISO','¡La contraseña o el usuario ingresado no es correcta!')

    def __init__(self):
        self.ventana=Tk()
        self.ventana.title('Inicio de sesión')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0,height=0)
        utl.centrar_ventana(self.ventana,800,500)

        logo =utl.leer_imagen("../PYTHON_SQLITE3/Apps5/imagenes/logo.jpg", (200, 200))

        # FRAME LOGO
        frame_logo=Frame(self.ventana,bd=0,width=300,relief=SOLID,padx=10,pady=10,bg='#3a7ff6')
        frame_logo.pack(side='left',expand=NO,fill='both')
        label=Label(frame_logo,image=logo,bg='#3a7ff6')
        label.place(x=0,y=0,relwidth=1,relheight=1)
        
        #FRAME FORM
        frame_form=Frame(self.ventana,bd=0,relief=SOLID,bg='#fcfcfc')
        frame_form.pack(side='right',expand=YES,fill='both')
        
        #FRAME FORM TOP
        frame_form_top=Frame(frame_form,height=50,bd=0,relief=SOLID,bg='black')
        frame_form_top.pack(side='top',fill='x')
        title=Label(frame_form_top,text='Inicio de sesión',font=('Times',30),fg='#666a88',bg='#fcfcfc',pady=50)
        title.pack(expand=YES,fill='both')
        #END FRAME FORM TOP

        #FRAME FORM FILL (fram de rellenado)
        frame_form_fill=Frame(frame_form,height=50,bd=0,relief=SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side='bottom',expand=YES,fill='both')

# **************** LABELS & ENTRYS ****************

        etiqueta_usuario=Label(frame_form_fill,text='Usuario',font=('Times',14),fg='#666a88',bg='#fcfcfc',anchor='w')
        etiqueta_usuario.pack(fill='x',padx=20,pady=5)
        self.usuario=Entry(frame_form_fill,font=('Times',14))
        self.usuario.pack(fill='x',padx=20,pady=10)

        etiqueta_password=Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill='x', padx=20,pady=5)
        self.password=Entry(frame_form_fill,font=('Times',14))
        self.password.pack(fill='x',padx=20,pady=10)
        self.password.config(show='*')

        inicio = Button(frame_form_fill,text='Iniciar sesión',font=('Times',15,BOLD),bg='#3a7ff6',bd=0,fg='#fff',command=self.verificar)
        inicio.pack(fill='x',padx=20,pady=20)
        inicio.bind('<Return>',(lambda event:self.verificar()))

        self.ventana.mainloop()