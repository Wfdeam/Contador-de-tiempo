import tkinter as tk
import datetime
import pandas as pd

# Variables
hora_inicio = None
hora_fin = None
df = pd.DataFrame(columns=['Tiempo', 'Descripción'])

def inicio():
    global hora_inicio
    hora_inicio = datetime.datetime.now()

def fin():
    global hora_inicio
    global hora_fin
    if hora_inicio is not None:
        hora_fin = datetime.datetime.now()
        tiempo_transcurrido = hora_fin - hora_inicio
        descripcion = 'Algo'
        global df
        df = pd.concat([df, pd.DataFrame({'Tiempo': [tiempo_transcurrido], 'Descripción': [descripcion]})], ignore_index=True)
        
        hora_inicio = None
    else:
        print("Por favor, primero inicia el tiempo.")

def uiPrimaria():
    root = tk.Tk()
    root.title("Calcula Tiempo")
    root.geometry("500x500")
    
    label = tk.Label(root, text='Ingrese la descripción de la tarea', font=('Arial', 10))
    label.pack(padx=0.1)

    textbox = tk.Text(root, height=1)
    textbox.pack()

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)

    btn1 = tk.Button(buttonframe, text='Inicio', font=('Arial', 10), command=inicio)
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(buttonframe, text='Fin', font=('Arial', 10), command=fin)
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

    buttonframe.pack(fill='x')

    root.mainloop()

uiPrimaria()
