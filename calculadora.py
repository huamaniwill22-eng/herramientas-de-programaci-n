import tkinter as tk
from tkinter import messagebox

# Funciones de lógica de la calculadora
def click_boton(valor):
    # Inserta el valor del botón presionado en la pantalla
    pantalla.insert(tk.END, valor)

def limpiar_pantalla():
    # Borra todo el contenido de la pantalla
    pantalla.delete(0, tk.END)

def calcular_resultado():
    try:
        # Evalúa la expresión matemática en la pantalla
        expresion = pantalla.get()
        resultado = eval(expresion)
        
        limpiar_pantalla()
        pantalla.insert(0, str(resultado))
    except ZeroDivisionError:
        messagebox.onerror("Error", "No se puede dividir entre cero.")
        limpiar_pantalla()
    except Exception:
        messagebox.showerror("Error", "Expresión inválida.")
        limpiar_pantalla()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("350x450")
ventana.configure(bg="#2c3e50") # Color de fondo oscuro

# Pantalla de entrada de datos
pantalla = tk.Entry(ventana, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Configuración de los botones (Texto, Fila, Columna)
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Estilo común para los botones
estilo_botones = {
    "font": ("Arial", 14, "bold"),
    "fg": "#ffffff",
    "bg": "#34495e",
    "activebackground": "#16a085",
    "activeforeground": "#ffffff",
    "borderwidth": 1,
    "relief": "groove"
}

# Crear y colocar los botones en la cuadrícula
for (texto, fila, columna) in botones:
    # Personalizar colores para botones especiales
    if texto == 'C':
        accion = limpiar_pantalla
        color_bg = "#e74c3c" # Rojo
    elif texto == '=':
        accion = calcular_resultado
        color_bg = "#2ecc71" # Verde
    elif texto in ['/', '*', '-', '+']:
        accion = lambda t=texto: click_boton(t)
        color_bg = "#3498db" # Azul
    else:
        accion = lambda t=texto: click_boton(t)
        color_bg = estilo_botones["bg"]

    btn = tk.Button(ventana, text=texto, command=accion, **{**estilo_botones, "bg": color_bg})
    btn.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

# Hacer que las filas y columnas se expandan proporcionalmente al cambiar el tamaño de la ventana
for i in range(5):
    ventana.rowconfigure(i, weight=1)
for j in range(4):
    ventana.columnconfigure(j, weight=1)

# Iniciar el bucle de la aplicación
ventana.mainloop()