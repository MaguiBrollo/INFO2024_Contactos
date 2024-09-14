#=======IMPORTACIONES=============================================
import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 
import salir as SL
import tabla_de_contactos as TB 

def ventanaPrincipal(us):
    #======FUNCIONES==============================================
      def funcion_login():
         messagebox.showwarning("Login", "Aquí se hace Inicio de Sesión")

      def funcion_logout(ventana):
         SL.salir(ventana)
       
      def mostrar_contactos():
          TB.tabla_contactos()

      def funcion_exportar():
          pass
         # EE.funcion_exportar()


      #=====PROGRAMA PRINCIPAL===============================================
      ventana = Tk()
      lista_contactos = Listbox(ventana)
    

      dir_carpetas = os.path.dirname(__file__)
      img_carpeta = os.path.join(dir_carpetas,"imagenes")
      ventana.iconbitmap(os.path.join(img_carpeta,"contactos.ico"))

      ventana.title('Agenda Personal')
      ventana.geometry('800x600')
      ventana.configure(bg="#4B6587")

      datos_usu=Label(ventana, text="Usuario: "+us, fg='white',bg="#4B6587",font=('Microsoft YaHei UI Ligth',14,'bold'))
      datos_usu.place(relx=0.1,rely=0.9)

      img_logo_ppal = ImageTk.PhotoImage(Image.open(os.path.join(img_carpeta,"contactos.png")).resize((100,100)))
      img_mostrar = Label(image=img_logo_ppal)
      img_mostrar.place(relx=0.8,rely=0.8)

      barra_menu = Menu(ventana)
      ventana.config(menu=barra_menu)
      menu_principal = Menu(barra_menu)
      barra_menu.add_cascade(label ='Menú', menu=menu_principal)
      submenu = Menu(menu_principal)

      menu_principal.add_cascade(label = 'Contactos', command=mostrar_contactos)
      menu_principal.add_cascade(label = 'Salir', command=lambda: funcion_logout(ventana))

      ventana.mainloop()