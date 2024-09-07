import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import ast
import ventanaPrincipal as VP

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)#Bloque del maximizado

dir_carpetas = os.path.dirname(__file__)
img_carpeta = os.path.join(dir_carpetas,"imagenes")
root.iconbitmap(os.path.join(img_carpeta,"contactos.ico"))

file_path = os.path.join(dir_carpetas, 'user_data.txt')

def singin():#Esta es la funcion de inicio de sesion
    username=user.get()#Tomamos los valores ingresados del usuario
    password=code.get()#Tomamos los valores ingresados de la contraseña

    try:
        with open(file_path, 'r') as file:
            d=file.read()
            r=ast.literal_eval(d)
    except (FileNotFoundError, SyntaxError):
        r = {} #esta funcion lo va a inicializar como diccionacio vacio

#Parte del donde se ingresa sus archivos
    if username in r.keys() and password==r[username]:
        root.destroy()
        VP.ventanaPrincipal()
    else:
        messagebox.showerror('Inválido','Usuario o contraseña incorrecta')

def singup_command():
    windows = Toplevel(root)
    windows.title("Registro")
    windows.geometry('925x500+300+300')
    windows.configure(bg='#fff')
    windows.resizable(False,False)

    dir_folds = os.path.dirname(__file__)
    img_fold = os.path.join(dir_folds,"imagenes")
    windows.iconbitmap(os.path.join(img_fold,"contactos.ico"))

    def signup():
        username = user.get()
        password = code.get()
        conform_password = conform_code.get()

        if password == conform_password:
            try:
                with open(file_path, 'r+') as file:
                    d = file.read()
                    r = ast.literal_eval(d)
                    diccionario = {username: password}
                    r.update(diccionario)
                    file.seek(0)#Cambio del codigo
                    file.write(str(r))#Cambio
                    file.truncate()#camcio

                messagebox.showinfo('Registro', 'Registro de cuenta exitosa')
                windows.destroy()

            except (FileNotFoundError, SyntaxError):# Cambio
                with open(file_path, 'w') as file:
                    pp = str({username: password})
                    file.write(pp)

                messagebox.showinfo('Registro', 'Registro de cuenta exitosa')
                windows.destroy()

    def close_windows():#Para cerrar ventana de inicio de sesion
        windows.destroy()

    img_logup = ImageTk.PhotoImage(Image.open(os.path.join(img_fold, "logup.png")).resize((387,280)))
    img_mostrar_logup = Label(windows, image=img_logup)
    img_mostrar_logup.place(relx=0.1,rely=0.1)

    frame = Frame(windows,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)

    heading=Label(frame,text='Registro',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI ligth',23,'bold'))
    heading.place(x=102,y=5)

    #Campos de entrada
    def create_entry(frame,placeholder, y_position):
        def on_enter(e):
            widget.delete(0,'end')

        def on_leave(e):
            if widget.get()=='':
                widget.insert(0, placeholder)
        
        widget = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
        widget.place(x=30, y=y_position)
        widget.insert(0, placeholder)
        widget.bind("<FocusIn>", on_enter)
        widget.bind("<FocusOut>", on_leave)
        Frame(frame,width=295, height=2, bg='black').place(x=25, y=y_position + 27)
        return widget

    user = create_entry(frame, 'Usuario', 80)
    code = create_entry(frame, 'Contraseña', 150)
    conform_code = create_entry(frame, 'Confirmar Contraseña', 220)

    Button(frame, width=39, pady=7, text='Registrar',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label = Label(frame,text='Ya tengo una cuenta',fg='black',bg='white',font=('Microsoft Yahei UI ligth',9))
    label.place(x=90,y=340)

    signin=Button(frame,width=11,text='Inicio de sesion',border=0,bg='white',cursor='hand2',fg='#57a1f8', command=close_windows)
    signin.place(x=210,y=340)

    windows.mainloop()

#Imagenes
img_logup = ImageTk.PhotoImage(Image.open(os.path.join(img_carpeta, "login.png")).resize((387,280)))
img_mostrar_logup = Label(image=img_logup, border=0)
img_mostrar_logup.place(relx=0.1,rely=0.2)

frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480,y=70)

heading=Label(frame, text='Inicio de Sesión', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Ligth',23,'bold'))
heading.place(x=100,y=5)

#Campos de entrada Login
def create_entry(frame,placeholder, y_position):
    def on_enter(e):
        widget.delete(0,'end')

    def on_leave(e):
        if widget.get()=='':
            widget.insert(0,'Usuario')
    #user = Entry
    widget = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
    widget.place(x=30, y=y_position)
    widget.insert(0, placeholder)
    widget.bind("<FocusIn>", on_enter)
    widget.bind("<FocusOut>", on_leave)
    Frame(frame,width=295, height=2, bg='black').place(x=25, y=y_position + 27)
    return widget

user = create_entry(frame, 'Usuario', 80)
code = create_entry(frame, 'Contraseña', 150)

Button(frame,width=39,pady=7,text='Sing in',bg='#57a1f8',fg='white',border=0, command=singin).place(x=35,y=204)
label=Label(frame,text="¿No tienes una cuenta?",fg='black',bg='white',font=('Microsoft YaHei UI Ligth',9))
label.place(x=75,y=270)

sin_cuenta= Button(frame,width=8,text='Regístrate',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=singup_command)
sin_cuenta.place(x=215,y=270)

root.mainloop()