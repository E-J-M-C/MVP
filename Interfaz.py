#Primero se importa la clase Materia que se creo en el archivo Materias
import tkinter as tk
from tkinter import ttk
from Materias import Materia

#Se define el metodo de la interfaz, del cual se desglozan las acciones
def calcularCalificacionFinal():
    parcial1 = 0.0
    parcial2 = 0.0
    parcial3 = 0.0

#Se determinan las precondiciones y se configuran las etiquetas de error   
    try:
        parcial1 = float(input_parcial1.get())
        if parcial1 < 0 or parcial1 > 10:
            etiqueta_error_parcial1.config(text="Solo se permiten valores entre 0 y 10")
            return
        etiqueta_error_parcial1.config(text=f"")
    except ValueError as ve:
        etiqueta_error_parcial1.config(text=f"Ingresa valores validos")
        return
   
    try:
        parcial2 = float(input_parcial2.get())
        if parcial2 < 0 or parcial2 > 10:
            etiqueta_error_parcial2.config(text="Solo se permiten valores entre 0 y 10")
            return
        etiqueta_error_parcial2.config(text=f"")
    except ValueError as ve:
        etiqueta_error_parcial2.config(text=f"Ingresa valores validos")
        return
    
    try:
        parcial3 = float(input_parcial3.get())
        if parcial3 < 0 or parcial3 > 10:
            etiqueta_error_parcial3.config(text="Solo se permiten valores entre 0 y 10")
            return
        etiqueta_error_parcial3.config(text=f"")
    except ValueError as ve: 
        etiqueta_error_parcial3.config(text=f"Ingresa valores validos")
        return

#Se configura el traslado del metodo de la clase a la interfaz, para mostrar resultado  
    calificacion = Materia()
    calificacionFinal = calificacion.calcularPromedioPonderado(parcial1, parcial2, parcial3)
    
    etiqueta_calificacionFinal.config(text=f"Tu calificación final es: {calificacionFinal}")

#Se crea la ventana o interfaz y dentro sus componentes o lo que se observara
ventana = tk.Tk()
ventana.title("Materia")
ventana.config(width=550, height=300)

#Se crean las etiquetas de datos
etiqueta_parcial1 = ttk.Label(text="Ingresa calificación del primer parcial (20%): ")
etiqueta_parcial1.place(x=10, y=20)
etiqueta_parcial2 = ttk.Label(text="Ingresa calificación del segundo parcial (30%): ")
etiqueta_parcial2.place(x=10, y=60)
etiqueta_parcial3 = ttk.Label(text="Ingresa calificación del tercer parcial (50%): ")
etiqueta_parcial3.place(x=10, y=100)
etiqueta_calificacionFinal = ttk.Label(text="")
etiqueta_calificacionFinal.place(x=10, y=180)

#Se asignan casillas para la colocacion de los datos
input_parcial1 = ttk.Entry()
input_parcial1.place(x=260, y=20, width=50)
input_parcial2 = ttk.Entry()
input_parcial2.place(x=260, y=60, width=50)
input_parcial3 = ttk.Entry()
input_parcial3.place(x=260, y=100, width=50)

#Se crean las etiquetas de error
etiqueta_error_parcial1 = ttk.Label(text="")
etiqueta_error_parcial1.place(x=310, y=20)
etiqueta_error_parcial2 = ttk.Label(text="")
etiqueta_error_parcial2.place(x=310, y=60)
etiqueta_error_parcial3 = ttk.Label(text="")
etiqueta_error_parcial3.place(x=310, y=100)

#Se crea el boton para la ejecucion del comando 
boton_calcular = ttk.Button(text="Calcular", command=calcularCalificacionFinal)
boton_calcular.place(x=100, y=140)

#Se cierra la ventana o interfaz
ventana.mainloop()
