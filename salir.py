import tkinter as tk
import os

def salir(ventana_principal):
    """
    Muestra un cartel de confirmación para salir de la aplicación.

    Args:
        ventana_principal: La ventana principal de la aplicación.
    """

    ventana_confirmacion = tk.Toplevel(ventana_principal)
    ventana_confirmacion.title("Confirmación")
    dir_carpetas = os.path.dirname(__file__)
    img_carpeta = os.path.join(dir_carpetas,"imagenes")
    ventana_confirmacion.iconbitmap(os.path.join(img_carpeta,"contactos.ico"))
    ventana_confirmacion.geometry('270x100')
    #ventana_confirmacion.configure(bg="#4B6587")

    etiqueta = tk.Label(ventana_confirmacion, text="¿Deseas cerrar sesión?")
    etiqueta.pack(pady=10)

    boton_aceptar = tk.Button(ventana_confirmacion, text="Aceptar", command=lambda: cerrar_aplicacion(ventana_principal, ventana_confirmacion))
    boton_aceptar.pack(side=tk.LEFT, padx=10)

    boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=ventana_confirmacion.destroy)
    boton_cancelar.pack(side=tk.RIGHT, padx=10)

def cerrar_aplicacion(ventana_principal, ventana_confirmacion):
    """
    Cierra la ventana de confirmación y la ventana principal.

    Args:
        ventana_principal: La ventana principal de la aplicación.
        ventana_confirmacion: La ventana de confirmación.
    """

    ventana_confirmacion.destroy()
    ventana_principal.destroy()

# Ejemplo de uso:
""" if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Mi Aplicación")

    # ... (resto de tu código)


    

    boton_salir = tk.Button(ventana, text="Salir", command=lambda: salir(ventana))
    boton_salir.pack()

    ventana.mainloop() """