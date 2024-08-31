#=======IMPORTACIONES=============================================

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import contactos 

#======FUNCIONES==============================================
def funcion_login():
   messagebox.showwarning("Login", "Aquí se hace Inicio de Sesión")

def funcion_logout():
   messagebox.showwarning("Logout", "Aqui se hace CERRAR sesión")

def mostrar_contactos():
   messagebox.showwarning("Contactos", "Aquí se muestra todos los contactos, y los botones Crear/Eliminar/Editar") 

def funcion_exportar():
   messagebox.showwarning("Exportar", "Aquí la opción de Exportar los contactos a EXCEL")



#=====PROGRAMA PRINCIPAL===============================================
ventana = tk.Tk()
lista_contactos = tk.Listbox(ventana)
login = False

dir_carpetas = os.path.dirname(__file__)
img_carpeta = os.path.join(dir_carpetas,"imagenes")
root.iconbitmap(os.path.join(img_carpeta,"contactos.ico"))

def singin():#Esta es la funcion de inicio de sesion
    username=user.get()#Tomamos los valores ingresados del usuario
    password=code.get()#Tomamos los valores ingresados de la contraseña

    file=open('user_data.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    ## print(r.keys())
    ## print(r.values())

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Parte Del Codigo de Contactos @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    if username in r.keys() and password==r[username]:
        root.destroy()
        VP.ventanaPrincipal()
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Fin de La Parte del Codigo de contactos @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    else:
        messagebox.showerror('Inválido','Usuario o contraseña incorrecta')


######/////////////////////En esta parte va a estar el codigo donde vamos a ejecutar la ventana del registro de sesion

def singup_command():

    windows=Toplevel(root)

    windows.title("Logup")
    windows.geometry('925x500+300+300')
    windows.configure(bg='#fff')
    windows.resizable(False,False)

    def signup():
      username=user.get()
      password=code.get()
      conform_password=conform_code.get()

      if password==conform_password:
            try:
                file=open('user_data.txt', 'r+')
                d=file.read()
                r= ast.literal_eval(d)

                diccionario={username:password}
                r.update(diccionario)
                file.truncate(0)
                file.close()

                file=open('user_data.txt', 'w')
                w=file.write(str(r))

                messagebox.showinfo('Registro','Registro de cuenta exitosa')
                windows.destroy()

            except:
                file=open('user_data.txt', 'w')
                pp=str({'Usuario':'contrasenia'})
                file.write(pp)
                file.close()
                
      else:
         messagebox.showerror('Invalido',"Ambas contraseñas deben coincidir")

    def sing():
        windows.destroy()


    img = PhotoImage(Image.open(os.path.join(img_carpeta,"logup.png")))

    Label(windows,image=img,border=0,bg='white').place(x=50,y=90)

    frame = Frame(windows,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)

    heading=Label(frame,text='Inicio de sesion',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI ligth',23,'bold'))
    heading.place(x=100,y=5)

    ####------------------------------------------------------------
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Usuario')


    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI ligth',11))
    user.place(x=30,y=80)
    user.insert(0, 'Usuario')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    ####--------------------------------------------------

    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Contraseña')

    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI ligth',11))
    code.place(x=30,y=150)
    code.insert(0, 'Contraseña')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    ####--------------------------------------------------
    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Confirma Contraseña')

    conform_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI ligth',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0, 'Confirma Contraseña')
    conform_code.bind("<FocusIn>", on_enter)
    conform_code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    #---------------------------------------------
    Button(frame,width=39,pady=7,text='Inicio de sesion',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label = Label(frame,text='Ya tengo una cuenta',fg='black',bg='white',font=('Microsoft Yahei UI ligth',9))
    label.place(x=90,y=340)

    signin=Button(frame,width=11,text='Inicio de sesion',border=0,bg='white',cursor='hand2',fg='#57a1f8', command=sing)
    signin.place(x=210,y=340)

    windows.mainloop()


##################################//////////////////////////////
frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480,y=70)

heading=Label(frame, text='Sing in', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Ligth',23,'bold'))
heading.place(x=100,y=5)


#------------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Usuario')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Ligth',11))
user.place(x=30,y=80)
user.insert(0,'Usuario')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


###########################-----------------------------------------------------------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Contraseña')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Ligth',11))
code.place(x=30,y=150)
code.insert(0,'Contraseña')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#################################################
Button(frame,width=39,pady=7,text='Sing in',bg='#57a1f8',fg='white',border=0, command=singin).place(x=35,y=204)
label=Label(frame,text="¿No tienes una cuenta?",fg='black',bg='white',font=('Microsoft YaHei UI Ligth',9))
label.place(x=75,y=270)

sin_cuenta= Button(frame,width=8,text='Inicia sesión',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=singup_command)
sin_cuenta.place(x=215,y=270)

root.mainloop()