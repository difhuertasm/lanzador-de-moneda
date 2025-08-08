import random
import tkinter as tk
from PIL import Image, ImageTk

def open_window1():
    ''' Abre una nueva ventana mostrando gráficamente el resultado, es decir si su lado es cara o sello (cruz) '''
    ventana = tk.Toplevel() #Toplevel abre una ventana de forma independiente dentro del gestor de ventanas.
    ventana.title("Resultado")
    ventana.minsize(width=300, height=150)
    ventana.configure(bg="#F2DBA1")
    lado = ["Cara", "Sello"]
    lado_random = random.choice(lado) 
    l1 = tk.Label(ventana, text="Has sacado:", bg="#F2DBA1", fg= "#491F04", font=("Arial, 12"))
    l1.pack(padx=20, pady=0)
    l2 = tk.Label(ventana, text=lado_random, bg="#F2DBA1", fg= "#491F04", font=("Arial, 14"))
    l2.pack(padx=20, pady=10)

    if lado_random == "Cara":
        imagen1 = Image.open("Cara_100.png")  
        photo1 = ImageTk.PhotoImage(imagen1)

        # Crea un Label y asigna la imagen
        l3 = tk.Label(ventana, image=photo1, bg="#F2DBA1")
        l3.image = photo1 # ← Mantener referencia: garantiza que no se recolecte como basura por el recolector de memoria de Python.
        l3.pack(padx=20, pady=20)
    else:
        imagen2 = Image.open("Sello_100.png")  
        photo2 = ImageTk.PhotoImage(imagen2)

        # Crea un Label y asigna la imagen
        l3 = tk.Label(ventana, image=photo2, bg="#F2DBA1")
        l3.image = photo2 
        l3.pack(padx=20, pady=20)

# Ventana principal
moneda = tk.Tk()
moneda.title("Lanzador de Moneda")
moneda.minsize(width=100, height=65)
moneda.configure(bg="#F2DBA1")
l1 = tk.Label(moneda, text="Generador aleatorio de lados de una moneda", bg="#F2DBA1", fg= "#491F04", font=("Arial, 12"))
l1.pack(padx=20, pady=0)
# Crear botones
btn1 = tk.Button(moneda, text="Generar", command=open_window1, bg ="#491F04", fg= "#F2DBA1", width=20, height=1)
btn1.pack(padx=10, pady=10)

moneda.mainloop()