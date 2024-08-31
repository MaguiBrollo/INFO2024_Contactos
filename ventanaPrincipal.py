#=======IMPORTACIONES=============================================
import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def ventanaPrincipal():
    #======FUNCIONES==============================================
      def funcion_login():
         messagebox.showwarning("Login", "Aquí se hace Inicio de Sesión")

      def funcion_logout():
         messagebox.showwarning("Logout", "Aqui se hace CERRAR sesión")
         #falta hacer

      def mostrar_contactos():
         messagebox.showwarning("Contactos", "Aquí se muestra todos los contactos, y los botones Crear/Eliminar/Editar") 

      def funcion_exportar():
         messagebox.showwarning("Exportar", "Aquí la opción de Exportar los contactos a EXCEL")


      #=====PROGRAMA PRINCIPAL===============================================
      ventana = Tk()
      lista_contactos = Listbox(ventana)
    

      dir_carpetas = os.path.dirname(__file__)
      img_carpeta = os.path.join(dir_carpetas,"imagenes")
      ventana.iconbitmap(os.path.join(img_carpeta,"contactos.ico"))

      ventana.title('Agenda Personal')
      ventana.geometry('800x600')
      ventana.configure(bg="#4B6587")

      img_logo_ppal = ImageTk.PhotoImage(Image.open(os.path.join(img_carpeta,"contactos.png")).resize((100,100)))
      img_mostrar = Label(image=img_logo_ppal)
      img_mostrar.place(relx=0.8,rely=0.8)

      barra_menu = Menu(ventana)
      ventana.config(menu=barra_menu)
      menu_principal = Menu(barra_menu)
      barra_menu.add_cascade(label ='Menú', menu=menu_principal)
      submenu = Menu(menu_principal)

       
      menu_principal.add_cascade(label = 'Contactos', menu=submenu)
      menu_principal.add_cascade(label = 'Salir', command=funcion_logout)

      submenu.add_cascade(label = 'Actualizar Contactos',command=mostrar_contactos)
      submenu.add_cascade(label = 'Exportar a Excel', command=funcion_exportar) 

      ventana.mainloop()